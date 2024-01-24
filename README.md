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
    <em>Final Output</em>
</p> 















<p align="center">
  <img width="1000" height="600" src="https://github.com/ankurkohli007/Experimental_Robotics_Laboratory_Assignment_I/blob/55355f42813136c9b120566bc441f17bf19d1ced/v14k.gif">
</p>

<p align="center">
    <em>Final Output</em>
</p> 









