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

Below is the Software Architucture depicted.

<p align="center">
  <img width="1000" height="900" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/70717950b0374cae2869bba79ce96d50fbd25d3c/uml_diag.png">
</p>

<p align="center">
    <em>Software Archutecture</em>
</p> 

**The above Software Architecture comprises of the following components:**

* **robot-state:** The ``robot-state`` serves as a node consolidating shared knowledge among components. It offers two services for robot position (``state/set_pose`` and ``state/get_pose``) and two for battery level (``state/set_battery_level`` and ``state/get_battery_level``).
* **motion planner:** 
    <ul>
      <li>The planner node employs an action server ``named motion/planner``, utilizing the ``SimpleActionServer class`` and ``Plan action`` message. It relies on the ``state/get_pose`` 
          service from the ``robot-state`` node and a ``target`` point provided as a goal.</li>
      <li>The planner generates a plan consisting of ``via_points``, with a small delay to avoid conflicts with the robot's real situation.</li> 
      <li>The ``planner_client`` node receives the ``target point`` from the ``finite_state_machine`` node and forwards it to the ``planner server`` as an action goal. The resulting 
        plan is published to the ``/path`` topic for use by the ``controller_client`` node.</li>
    </ul>
        
* **motion controller:** The controller node establishes an action server named motion/controller using the SimpleActionServer class and Control action message. It requires the state/set_pose service from the robot-state node and a plan in the form of via_points from the planner. The controller iterates through each via_point, simulating the time taken to move the robot to that location. The waiting time is computed based on the robot speed and Euclidean distance between points. At each via_point, the state/set_pose service is invoked, and feedback is provided. The controller reads the robot battery level using state/get_battery_level and updates it through state/set_battery_level after decrementing. The controller_client node subscribes to the /path topic to obtain via_points and sends them to the controller server as an action goal.
* **finite state machine - aRMOR:** This component defines states and transitions for the finite state machine of the topological map. It utilizes the topological_map.py helper script to update the ontology during runtime. It determines the target room based on last visit times, sending the target room pose to the planner_client through /target_point to find the path.













<p align="center">
  <img width="1000" height="600" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/55355f42813136c9b120566bc441f17bf19d1ced/v14k.gif">
</p>

<p align="center">
    <em>Final Output</em>
</p> 









