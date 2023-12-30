[Experimental Robotics Laboratory](https://corsi.unige.it/en/off.f/2022/ins/60244)<br>
**Programmer:** [Ankur Kohli](https://github.com/ankurkohli007)<br>
[M.Sc Robotics Engineering](https://corsi.unige.it/corsi/10635)<br>
[University of Genoa (UniGe), Italy](https://unige.it/en)<br>
**Supervisor:** [Prof. Carmine Tommaso Recchiuto](https://rubrica.unige.it/personale/UkNDWV1r) & [Prof. Luca Buoncompagni](https://rubrica.unige.it/personale/VkRGWFJq)

# Assignment 1: Adaptive Autonomous Surveillance Robot for Indoor Environments with Energy Management

## Abstract

This assignment introduces an **Autonomous Surveillance Robot** designed for efficient navigation in a 2D indoor environment comprising four rooms and three corridors. Commencing in Phase 1, the robot initiates operations at the "E" location, awaiting instructions to construct a comprehensive topological map that delineates the spatial relationships between corridors (C1, C2), rooms (R1, R2, R3), and doors (D1...D6). This map serves as a foundational guide for the subsequent phases. In Phase 2, the robot executes a perpetual loop of movement and surveillance, adhering to a policy that prioritizes corridor traversal and periodic room exploration based on a predefined duration since the last visit. An autonomous robot return to the "E" location is triggered when the robot's battery level falls below a set threshold, enabling recharge before recommencing surveillance. By integrating adaptive topological mapping, energy management, and a surveillance policy, this autonomous surveillance robot emerges as a comprehensive solution for effective indoor security and surveillance applications, offering dynamic and responsive navigation capabilities within a controlled environment.

## Introduction

In the evolving landscape of robotics and artificial intelligence, the deployment of autonomous surveillance systems holds immense potential for enhancing security and monitoring capabilities. This project addresses the design and implementation of an autonomous surveillance robot specifically crafted for navigating a 2D indoor environment comprising four rooms and three corridors. The robot's primary mission is to strategically traverse this space, adhering to a surveillance policy that emphasizes corridor exploration while periodically visiting unexplored rooms. An intelligent battery management system ensures the robot's autonomy, prompting a return to a designated location for recharging when the battery level reaches a critical threshold. The simulation of the robot's movements and responses, including low battery scenarios, follows an approach outlined in a provided GitHub repository provide by [Prof. Luca Buoncompagni](https://rubrica.unige.it/personale/VkRGWFJq) of [Topological Map](https://github.com/buoncubi/arch_skeleton). By integrating adaptive topological mapping, energy management, and a targeted surveillance policy, the envisioned autonomous surveillance robot presents a sophisticated solution for ensuring effective and dynamic surveillance in indoor environments. The amalgamation of these elements aims to create a responsive and intelligent system capable of fulfilling surveillance objectives while navigating the intricacies of the designated environment.

The contents of this repository feature a software solution built on the Robot Operating System (ROS), simulating the intricate behavioral architecture of a mobile robot as it dynamically moves through different rooms. This assignment leverages the [ROS SMACH](https://wiki.ros.org/smach) state machine and employs the [armor_py_api](https://github.com/EmaroLab/armor_py_api/blob/master/scripts/armor_api/armor_manipulation_client.py), a tool provided by the [EMARO Lab](https://github.com/EmaroLab) at the [University of Genoa (UniGe), Italy](https://unige.it/en), to construct a comprehensive ontology. Notably, a critical focal point of this exercise revolves around achieving optimal synchronization between the robot's actions and user interactions. The design places paramount importance on minimizing any waiting time for the user, ensuring a seamless experience, with the exception of necessary intervals when the robot is in the process of recharging its battery. Below is the figure shows the scenario how the robot works in the 2D environment: 

<p align="center">
  <img width="600" height="600" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/0a58201b93abaf209ae51218e42a83f1819e6c0d/environment.png">
</p>

<p align="center">
    <em>2D Environment</em>
</p> 

The above scenario highlights that:

* The robot is located in room E and loads a map.
* If the map is successfully loaded, the robot initiates movement within the corridors; otherwise, it remains within room E.
* When the robot's battery is at full capacity, it proceeds to explore the various rooms; otherwise, it returns to room E for recharging.
* After completing the recharging process, the robot resumes its exploration of the rooms.

## Architecture 

To model the robot's movements and stimuli in a simulation, the methodology adopted is based on the [arch_skeleton](https://github.com/buoncubi/arch_skeleton) example, though with modifications such as adjustments to the planner and controller delay times, as well as variations in the battery level.

The core of the software architecture involves a finite state machine, leveraging [SMACH](https://wiki.ros.org/smach) to provide a clear representation of process states and their transitions. Additionally, [aRMOR](https://github.com/EmaroLab/armor) is employed for utilizing the ontology of the topological map to control the robot within the Robot Operating System (ROS) environment.

Below is the Software Architucture Component Diagram.

<p align="center">
  <img width="1000" height="900" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/70717950b0374cae2869bba79ce96d50fbd25d3c/uml_diag.png">
</p>

<p align="center">
    <em>Software Archutecture Component Diagram</em>
</p> 

**The above Software Architecture comprises of the following components:**

* **robot-state:** The ``robot-state`` serves as a node consolidating shared knowledge among components. It offers two services for robot position (``state/set_pose`` and ``state/get_pose``) and two for battery level (``state/set_battery_level`` and ``state/get_battery_level``).
* **motion planner:** The planner node employs an action server ``named motion/planner``, utilizing the ``SimpleActionServer class`` and ``Plan action`` message. It relies on the ``state/get_pose`` service from the ``robot-state`` node and a ``target`` point provided as a goal. The planner generates a plan consisting of ``via_points``, with a small delay to avoid conflicts with the robot's real situation. The ``planner_client`` node receives the ``target point`` from the ``finite_state_machine`` node and forwards it to the ``planner server`` as an action goal. The resulting plan is published to the ``/path`` topic for use by the ``controller_client`` node.
           
* **motion controller:** The ``controller`` node establishes an action server named ``motion/controller`` using the ``SimpleActionServer`` class and ``Control`` action message. It requires the ``state/set_pose`` service from the ``robot-state`` node and a plan in the form of ``via_points`` from the ``planner``. The controller iterates through each ``via_point``, simulating the time taken to move the robot to that location. The waiting time is computed based on the robot speed and Euclidean distance between points. At each ``via_point``, the ``state/set_pose`` service is invoked, and feedback is provided. The controller reads the robot battery level using ``state/get_battery_level`` and updates it through ``state/set_battery_level`` after decrementing. The ``controller_client`` node subscribes to the ``/path`` topic to obtain via_points and sends them to the controller server as an action goal.
* **finite_state_machine - aRMOR:** This component defines states and transitions for the ``finite_state_machine`` of the ``topological map``. It utilizes the ``topological_map.py`` ``helper`` script to update the ``ontology`` during runtime. It determines the target room based on last visit times, sending the target room pose to the ``planner_client`` through ``/target_point`` to find the path.

The temporal interaction among the software components is illustrated in the figure below. 

<p align="center">
  <img width="1000" height="800" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/d14051236ca6884a79e4342b03e8ad0a26847621/temporal_diagram.png">
</p>

<p align="center">
    <em>Temporal Diagram</em>
</p> 

The low battery signal takes precedence as the highest-priority signal. Therefore, upon receiving the low battery signal, the software terminates all other requests, directing the robot to transition to the **RECHARGING** state.

In the next section, a detailed description of all the components depicted in the diagrams is provided.

### Component

#### ``finite_statemachine`` node & ``helper`` node

This node initializes the finite_statemachine (FSM) and outlines its behavior. To maintain a lightweight code structure, the author opted to implement a ``helper.py`` script, accessible [from here](https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/main/scripts/helper.py), where the majority of the reasoning is executed. The script comprises three classes, each dedicated to a specific helper:

* **ActionClientHelper:** Streamlines the implementation of a client for ROS action servers.
* **InterfaceHelper:** Manages synchronization with subscribers and action servers.
* **KnowledgeGraphHelper:** Communicates with the aRMOR server by sending queries, primarily concerning robot position, reachable locations, and urgent locations.

This approach allows users to comprehend the FSM's state transitions in the ``finite_statemachine.py`` script which can be accessible [here](https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/main/scripts/finite_statemachine.py), while insights into the FSM's reasoning for actions like changing location or initiating a recharge are available in the ``helper.py`` script.

#### ``robot_states`` node

This node incorporates two services, namely ``state/set_pose`` and ``state/get_pose``, facilitating the setting and retrieval of the current robot position—a shared knowledge with the ``planner`` and ``controller`` nodes:

* The service ``state/set_pose`` necessitates the input of a ``Point`` and does not return any values.
* The service ``state/get_pose`` requires no input and returns a ``Point``.
  
Additionally, the node features a publisher of battery percentage on the ``state/battery_low`` topic. This representing changes in battery status. If the battery is low, the message display battery low status, and vice versa. Users have the flexibility to modify the battery time value by adjusting the constant variable ``BATTERY_TIME`` in the [``architecture_name_matter.py``](https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/main/utilities/assignment_1/architecture_name_mapper.py) script.

























<p align="center">
  <img width="1000" height="600" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/55355f42813136c9b120566bc441f17bf19d1ced/v14k.gif">
</p>

<p align="center">
    <em>Final Output</em>
</p> 









