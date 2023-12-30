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

## Component

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

#### ``load_environment`` node

This scriot will load the map of nvironment to the robot which is initially at location ``E``.

#### ``planner`` node & ``controller`` node

The reader or user can find a detailed decription of these two nodes in the [README](https://github.com/buoncubi/arch_skeleton/blob/main/README.md) of the [arch_skeleton](https://github.com/buoncubi/arch_skeleton) repository of [Prof. Luca Buoncompagni](https://rubrica.unige.it/personale/VkRGWFJq).

### Briefing about the node defined in the assignment

* ``finite_statemachine.py``: A finite state machine is a computational model that represents an entity's behaviour through a finite number of states and transitions between them. Also, Python module for implementing the Finite State Machine.
* ``robot_states.py``: robot_states typically refers to a component or module in a robotic system responsible for managing and updating various states and information related to the robot, such as its pose, battery level, and operational status. Also, a Python module responsible for publishing the state of the battery, typically utilizing a ROS publisher to broadcast this information.
* ``helper.py``: A node equipped with Interface Helper and ActionClient Helper to facilitate the Finite State Machine by providing information about the action client's status and executing battery-related stimuli.
* ``load_environment.py``: "load_environment" typically refers to a process of loading or importing ontological data(environment), often used in knowledge management systems or semantic web applications. Also, This node helps to load the environmental map to the robot.

## Installation & Running

### Installation

To utilize this software effectively, the user should adhere to the following steps for installing the necessary packages and repositories.

* As the author opted to utilize the files [``planner.py``](https://github.com/buoncubi/arch_skeleton/blob/main/scripts/planner.py) and [``controller.py``](https://github.com/buoncubi/arch_skeleton/blob/main/scripts/controller.py) from the [arch_skeleton](https://github.com/buoncubi/arch_skeleton) repository, along with the [topological_map.owl](https://github.com/buoncubi/topological_map/blob/main/topological_map.owl) file from the [topological_map](https://github.com/buoncubi/topological_map) repository— both authored by [Prof. Luca Buoncompagni](https://rubrica.unige.it/personale/VkRGWFJq) and the user is required to clone the aforementioned repositories along with the current one into the ROS workspace.
* This package, being dependent on [aRMOR](https://github.com/EmaroLab/armor), must be installed according to the instructions outlined in the provided link as a prerequisite for running this package.
* Additionally, it has a dependency on [SMACH](https://wiki.ros.org/smach), which can be installed by using the following commands:

```bashscript
sudo apt-get install ros-<distro>-executive-smach*
```
```bashscript
sudo apt-get install ros-<distro>-smach-viewer
```

Here, ``ros-<distro>-`` depends to denote a package or component associated with a specific ROS distribution. For instance, **"ros-noetic"**, **"ros-melodic"**, and so on.

* Also, clone the [armor_py_api](https://github.com/EmaroLab/armor_py_api) repository in your ROS workspace.
* Once the dependencies are met, the package can be installed as it follows:

```bashscript
mkdir -p ros_ws/src
```
```bashscript
cd ros_ws/src
```
```bashscript
git clone https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I.git
```
```bashscript
cd ..
```
```bashscript
source /opt/ros/<distro>/setup.bash
```

Here, again the ``<distro>`` denotes a package or component associated with a specific ROS distribution

* Execute ``chmod +x <file_name>`` for each file inside the folder ``scripts`` of the assignment package which was cloned in the last step.
* Execute ``catkin_make`` from the root of your ROS workspace.

**Note:** If the error incurs while the installation of ``aRMOR`` package follow the tutorial to overcome the issue from [here](https://github.com/EmaroLab/armor/issues/7). Moreover, The author [Prof. Luca Buoncompagni](https://rubrica.unige.it/personale/VkRGWFJq) found some issues with the function proposed in the script [``armor_manipulation_client.py``](https://github.com/EmaroLab/armor_py_api/blob/master/scripts/armor_api/armor_manipulation_client.py) to disjoint the individuals of the ontology. Hence, another function was created in the script as:

```py
def disj_inds(self, inds):
    try:
        res = self._client.call('DISJOINT', 'IND', '', inds)

    except rospy.ROSException:
        raise ArmorServiceCallError("Cannot reach ARMOR client: Timeout Expired. Check if ARMOR is running.")

    if res.success:
        return res.is_consistent
    else:
        raise ArmorServiceInternalError(res.error_description, res.exit_code)
```

The user should copy and add the above function in the script to make the software work correctly.

### Running 

To initialize the software architecture in conjunction with the finite state machine representation, first install ``xterm`` if it is not installed by the command ``sudo apt-get install -y xterm`` and then execute the following commands:

```bashscript
source devel/setup.bash
```
```bashscript
roslaunch assignment1 exprob_assig1.launch
```

## Result

GIF below shows the final outcome of the given task. It shows that how the robot's behaviour as it starting from the location ``E``, and looking for the corridors and reaches to the room, and charging the battery when it's starts depleting, performing the task, and so on.

<p align="center">
  <img width="900" height="600" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/bb80070754ca2a7f89bacf31a598de06439e91e3/final_outcome.gif">
</p>

<p align="center">
    <em>Final Output: Task Performance</em>
</p> 

To visualize the change in states of the above robot, execute ``smach_viewer`` using the command given below:

```bashscript
rosrun smach_viewer smach_viewer.py
```

**Note:** For the video of the task performance [click here](final_outcome.mov)

``smach_viewer`` graph is diplayed below, which shows the robot behaviors using a finite state machine (FSM) approach. in SMACH, states represent specific robot actions or behaviors, transitions define conditions for state changes, and hierarchical structures facilitate the organization of complex behaviors. Integrated with ROS, SMACH uses ROS services, topics, and actions for seamless communication with the robot's environment. Developers define state machines in Python, allowing for modular and reusable components. SMACH is suitable for various robotic applications, offering tools like the SMACH Viewer for visualization and debugging. The development workflow involves installing ROS packages, creating Python scripts, and referring to SMACH documentation and tutorials for effective implementation.

<p align="center">
  <img width="900" height="600" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/339364df33b623844613e3e7e93e254ecb2bfa30/smach_viewer.png">
</p>

<p align="center">
    <em>Graphical View of smach_viewer</em>
</p> 

The figure above explains the visual representation of SMACH state machines, aiding in understanding of robot behaviors in 2d indoor environment. It allows developers to inspect state transitions and hierarchical structures graphically, enhancing the workflow in designing and refining robot actions. Also, helpful to viewers for the understanding of the task. The tool facilitates a more intuitive approach to managing and optimizing SMACH-based systems.

<p align="center">
  <img width="900" height="600" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/4da6a79d4b6e63a301af5995da55322c4feb3416/smach_viewer_tree.png">
</p>

<p align="center">
    <em>Tree View of smach_viewer</em>
</p> 

The figure above offering a visual breakdown of states and transitions in tree view format. Let's breakdown this tree view, first is ``SM_ROOT`` which ``LOADING_MAP``. Furthermore, it is ``DETERMINING_CORRIDOR_OR_ROOM``. This followed by ``ON_CORRIDOR_MOVE`` and this followed by ``ON_URGENT_MOVE``. Lastly, the ``RECHARGING_STATION``.

In the depicted figure, viewer can observe all pertinent components, illustrating the performance and goal of the task.

<p align="center">
  <img width="900" height="600" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/8d58431f347a41c8cf77cb1b81ed9e1068d50e75/finite_states.png">
</p>

<p align="center">
    <em>finite_statemachine</em>
</p> 

The above describes that, when the launch file is launched than the functions of the task comes into an action. It starts creating **"ontology"**, it stars **"LOADING_MAP"**. Also, it shows the initial position of the robot, followed byt the reachable positions where robot can reach easily. Moreover, it also highlights the target to reach.

The figure below explains, robot_states i.e. the status of robot's battery. It displays the percentatge of robot's battery, and also battery status such battery low and when the charging completes.

<p align="center">
  <img width="900" height="600" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/8d58431f347a41c8cf77cb1b81ed9e1068d50e75/robot_states.png">
</p>

<p align="center">
    <em>robot_states</em>
</p> 

## Working Hypothesis

To achieve the objectives outlined in the introduction, the author established several hypotheses:

* In the absence of urgent rooms, the robot consistently monitors the corridors.
* Corridors are exempt from urgency checks as the robot primarily remains in the corridor, and each time it inspects a room, it inherently needs to examine the connected corridor.
* Robot's return to room E (starting point) when there no target to reach. The author deemed it essential for accurate simulation, ensuring the algorithm appropriately focuses on corridor checks until a room becomes urgent. When recharging is required, and room E is not directly accessible, the robot moves randomly until room E becomes reachable.
* For simulation purposes, modification can be done in the [topological_map.owl](https://github.com/buoncubi/topological_map/blob/main/topological_map.owl) file, was set to 50 seconds. This adjustment ensures that the robot does not become persistently stuck in a corridor by continuously inspecting connected rooms if the threshold is too small.
* Additionally, system features shows that the topological map is configured with dimensions of 10x10. Upon selecting a room as the target room from the ontology, the associated point is communicated to the planner as a ``PlanGoal``.

## Limitation & Improvements

### Limitation

The planner stands out as a primary limitation in this ROS package, focusing solely on the starting and target points. Another constraint arises from the robot's behavior, where the battery level influences its choice, often prioritizing the charging room "E" over the target room derived from the last visit times.

Furthermore, a related issue emerges as the robot currently reaches the recharging room randomly. While this is acceptable in the present environment, where each room connects to only one corridor and each corridor links to the recharging room, it could pose problems in scenarios where not all corridors connect to the recharging room. A potential enhancement could involve computing a direct path from the robot's position to the recharging room.

### Improvements

In future, the system, can be improved by entailing and making the robot aware of more urgent rooms, even if they aren't directly reachable. This awareness could guide the robot to those rooms using a method similar to reaching the recharging room.

Another, Enhancements to the planner node are also conceivable, focusing on more precise consideration of walls. Additionally, a more realistic implementation of the battery level could contribute to refining the overall system.

## Conclusion

In conclusion, this assignment introduces a robust Autonomous Surveillance Robot tailored for effective navigation and surveillance within a 2D indoor environment. Leveraging ROS, SMACH state machines, and armor_py_api for ontology construction, the robot employs an adaptive topological map to strategically explore four rooms and three corridors. The surveillance policy, emphasizing corridor traversal and periodic room visits, ensures a dynamic and responsive approach to security monitoring. The integration of energy management, low-battery triggers, and autonomous recharging enhances the robot's autonomy. Despite some identified limitations in the current planner and battery management, the overall system represents a comprehensive solution for indoor surveillance, promising intelligent and adaptive navigation in controlled environments.

## Author & Contact

* Ankur Kohli
* Contact: ankurkohli1997007@gmail.com

aRMOR realted query contact: 

* [Prof. Carmine Tommaso Recchiuto](https://rubrica.unige.it/personale/UkNDWV1r); carmine.recchiuto@dibris.unige.it
* [Prof. Luca Buoncompagni](https://rubrica.unige.it/personale/VkRGWFJq); luca.buoncompagni@edu.unige.it























