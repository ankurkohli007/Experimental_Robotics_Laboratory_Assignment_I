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

The contents of this repository feature a software solution built on the Robot Operating System (ROS), simulating the intricate behavioral architecture of a mobile robot as it dynamically moves through different rooms. This assignment leverages the [ROS SMACH](https://wiki.ros.org/smach) state machine and employs the [armor_py_api](https://github.com/EmaroLab/armor_py_api/blob/master/scripts/armor_api/armor_manipulation_client.py), a tool provided by the [EMARO Lab](https://github.com/EmaroLab) at the [University of Genoa (UniGe), Italy](https://unige.it/en), to construct a comprehensive ontology. Notably, a critical focal point of this exercise revolves around achieving optimal synchronization between the robot's actions and user interactions. The design places paramount importance on minimizing any waiting time for the user, ensuring a seamless experience, with the exception of necessary intervals when the robot is in the process of recharging its battery.

In this scenario, the robot's behavior unfolds as follows:

* The robot begins in room E and initiates the map-loading process.
* If the map is successfully loaded, the robot commences its movement through the corridors; otherwise, it remains within room E.
* The robot evaluates its battery status, and if it is fully charged, the robot explores other rooms. However, if the battery is not at full capacity, the robot returns to room E for recharging.
* Once the battery is completely charged, the robot resumes its exploration of the various rooms.

The above scenario is shown below:

<p align="center">
  <img width="600" height="600" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/0a58201b93abaf209ae51218e42a83f1819e6c0d/environment.png">
</p>

<p align="center">
    <em>2D Environment</em>
</p> 

## Software Architecture

**1. [aRMOR](https://github.com/EmaroLab/armor)**
aRMOR is employed for loading the topological map and managing manipulation and query classes. The finite state machine is implemented within the ROS environment, utilizing the [ROS SMACH](https://wiki.ros.org/smach) package.

**2. [Protege](https://protege.stanford.edu/)**
Protégé is used to construct the topological map and establish the logical component. Its flexible plug-in architecture allows for customization to develop ontology-based applications of varying complexity. By combining Protégé's results with rule systems or other problem-solving tools, developers can create diverse intelligent systems.

**3. [arch_skeleton](https://github.com/buoncubi/arch_skeleton)**
This repository aims to simulate a behavioral architecture using ROS-based software. It serves a dual purpose by providing examples of ROS software and offering guidelines for bootstrapping robotics software architecture.

**4. State Machine**
The SMACH state machine controls the robot's state based on topological ontology map reasoning and the robot's battery status. The robot's states include:

* **Load Map:** The initial state involves building a semantic map for the robot. The robot arm moves along desired trajectories, and the state exits when sufficient room IDs are detected, returning the status of map_loaded.
* **Moving in Corridors:** The robot moves to a desired location with enabled battery consumption. The ontology is updated as the robot moves. If the battery drops below a threshold, the target room is canceled.
* **Discover Room:** The state where the robot explores the target room, enabling the robot arm's movement.
* **Moving for Charging:** This state occurs when the battery is low, and the robot moves towards the charger. The ontology is updated during movement until the robot reaches the charger.
* **Charging Station:** The state activates when the robot reaches the charging station and recharges the battery. The battery level is updated over time, and the state transitions to "charged."

## Component Diagarm 

The component diagram delineates the architecture of the mobile robot system, showcasing key components and their interactions. At the core is the ROS SMACH state machine, orchestrating the robot's behavior through modular states and transitions. The integration of [armor_py_api](https://github.com/EmaroLab/armor_py_api/blob/master/scripts/armor_api/armor_manipulation_client.py) and ontology construction contributes to the system's semantic understanding, guiding state transitions based on encoded information. External user interaction is represented, emphasizing the system's responsiveness to user input and the minimization of wait times. The `smach_viewer` is illustrated as an external tool, providing a graphical representation of the state machine for enhanced visualization. A dedicated state for battery recharge indicates the system's autonomy in managing energy resources. Collectively, the component diagram offers a succinct depiction of the mobile robot's architecture, highlighting the synergy among components for dynamic and user-responsive functionality. The figure below depicts the component diagram of the assignment:

<p align="center">
  <img width="1000" height="1000" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/66667b3e2128ea0f33df81780acd4ae365ae6b5b/uml_diag.png">
</p>

<p align="center">
    <em>Component Diagram</em>
</p> 

Here, the structure of the ROS nodes can be seen, along with the topics, services and action servers that link them together.

### `robot_states`
This component serves as the interface between the robot's state and other nodes. Specifically, it shares information about the robot's pose, the next goal, and the battery status. Additionally, it accepts pose updates to keep the ontology's current pose accurate and responds to requests to change the battery mode, either to charging or discharging.

### `controller`
This module accepts the plan via an action server, which, in this simulation, consists of a single goal. The plan is relayed from the behavior component, which, in turn, receives it from the planner component. The module then guides the robot through the plan. It notifies the behavior module upon reaching the final destination or in case of failure.

Additionally, this module oversees the management of the robot's battery charging.

In the simulated program, only adjacent locations are deemed reachable. Consequently, the controller always has just one waypoint to navigate towards. As a result, this component simulates its operations using busy waiting.

### `planner`

This module accepts the subsequent goal from the behavior component, which, in turn, obtains it from the owl_interface component. It then computes the shortest path to achieve the goal, generating a set of via points. These via points are subsequently transmitted to the controller component through the behavior module.

Given the constraints of the simulated program, where solely adjacent movements are allowed, the planner module doesn't actively perform computations. Instead, it simulates its operations using busy waiting.

## Temporal Diagram

In the figure below it highlights the temporal interaction between the software components:

<p align="center">
  <img width="800" height="500" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/2caa4f12cce65654235b60202409a757a4040b90/temporal_diagram.png">
</p>

<p align="center">
    <em>Component Diagram</em>
</p> 

In the event of a low battery signal, which holds the highest priority, the software within the Finite State Machine (FSM) promptly cancels all other requests. This cancellation ensures that the robot seamlessly transitions to the RECHARGING state, prioritizing the critical need to address the low battery condition.

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

Here, again the ``<distro>`` denotes a package or component associated with a specific ROS distribution.

* Execute ``chmod +x <file_name>`` for each file inside the folder ``scripts`` of the assignment package which was cloned in the last step.
* Execute ``catkin_make`` from the root of your ROS workspace.

#### Note: 

The author of the **aRMOR** developer found some issues with the function proposed in the script [armor_manipulation_client.py](https://github.com/sarasgambato/ExpRoLab_Assignment1/blob/master/scripts/armor_manipulation_client.py) to disjoint the individuals of the ontology. Hence, another function was created in the script as:
  
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
The executer should copy and add this function in the script to make the software work correctly.

### Running 

To initialize the software architecture in conjunction with the finite state machine representation, first install ``xterm`` if it is not installed by the command ``sudo apt-get install -y xterm`` and then execute the following commands:

```bashscript
source devel/setup.bash
```
```bashscript
roslaunch assignment_1 exprob_assg1.launch
```

## Final Outcome

The gif below shows the code perfomance and the final outcome of the assignment.

<p align="center">
  <img width="1000" height="800" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/b551b080ca777d71fb59df6c00a52037cc033372/final_outcome.gif">
</p>

<p align="center">
    <em>Final Output</em>
</p> 




























