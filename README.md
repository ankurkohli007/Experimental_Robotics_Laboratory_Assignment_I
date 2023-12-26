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

The contents of this repository feature a software solution built on the Robot Operating System (ROS), simulating the intricate behavioral architecture of a mobile robot as it dynamically moves through different rooms. This assignment leverages the [ROS SMACH](https://wiki.ros.org/smach) state machine and employs the [armor_py_api](https://github.com/EmaroLab/armor_py_api/blob/master/scripts/armor_api/armor_manipulation_client.py), a tool provided by the [Emaro Lab](https://github.com/EmaroLab) at the [University of Genoa (UniGe), Italy](https://unige.it/en), to construct a comprehensive ontology. Notably, a critical focal point of this exercise revolves around achieving optimal synchronization between the robot's actions and user interactions. The design places paramount importance on minimizing any waiting time for the user, ensuring a seamless experience, with the exception of necessary intervals when the robot is in the process of recharging its battery.












