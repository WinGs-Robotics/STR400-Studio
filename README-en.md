---
### Table of Contents

1. [Version Info & Change Log](#version-info--change-log)
2. [Download & Installation](#download--installation)
3. [UI Interface Description](#ui-interface-description)
4. [STR400 Robot Arm Kinematics Model & Motion Planning](#str400-robot-arm-kinematics-model--motion-planning)
5. [Python API Examples](#python-api-examples)
---

### Version Info & Change Log

<a name="version-info--change-log"></a>

This update is the first release, with a version number of v0.253.

---

### Download & Installation

<a name="download--installation"></a>

#### 1. Software Download

Visit the [WinGs Robotics STR400 Studio Github page](https://github.com/WinGs-Robotics/STR400-Studio/tree/main/APP) and download the entire folder. This includes the executable file and its associated configuration files.

**System Compatibility Tested**:

- Windows 10 (x86)
- Ubuntu 22.04 (x86)

**Recommended Hardware Configuration**:

- **CPU**: 11th gen Intel(R) Core(TM) i5-1135G7 @ 2.8Ghz 1.69Hz
- **RAM**: 8GB
- **Graphics**: Intel UHD Graphic

#### 2. Connect Device

Ensure the power source is connected and the USB data cable is properly plugged in. Check if your computer has successfully recognized the USB data port.

#### 3. Launch Application

Locate the executable file appropriate for your OS (Windows, Mac (Intel), or Linux) and launch it. Upon successful start, you will see the window as shown:

![Terminal Window](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/terminal.png)

Next, open a web browser and navigate to [http://localhost:8080](http://localhost:8080) to access the APP interface.

> **Note**: If you want to access this service on other devices within the same local network, ensure the STR400 Studio background service is running on the PC. Additionally, you will need to know the IP address of the PC running `str-studio.exe` and ensure that the 8080 port firewall protection is disabled.

---

### UI Interface Description

<a name="ui-interface-description"></a>

---

#### 1. Serial Port Connection

Once the application is successfully launched and you've accessed its front-end interface through your browser, you'll encounter the interface as shown:

![Connection Interface](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/connectionPage.png)

- **1**: Displays communication speed, currently supporting only a 2.25M baud rate. The refresh button on the right can help you re-detect all USB connection statuses.
- **2**: Click to attempt connecting to the corresponding serial port.
- **3**: Options to toggle between interface languages.

#### 2. Dashboard

Upon successful connection, you will enter the main interface of the STR Studio:

![Dashboard](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/mainPage.png)

- **1**: Function selection area, where you can access the dashboard, Teaching feature, W Script, and Configuration settings of the robot arm.
- **2**: A 3D model display of the robot arm. Use your mouse to rotate, move, and zoom into the model.
- **3**: QR code for mobile control. Scan this QR code with your phone to access the robot arm's control interface on your mobile device.
- **4**: Common shortcut operations, including emergency stop, passive mode, reset to zero, and two preset positions.
- **5**: This section displays the current status of the robot arm and the status and progress of the ongoing task.

#### 3. Mobile Controller

By scanning the QR code on the dashboard with your phone, you can have a similar control interface on your mobile device, enabling you to control the robot arm from any position within the same local network.

![Mobile Control Interface](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/mainPage.png)

#### 4. Teaching Feature

The teaching feature allows users to manually rotate the robot arm joints and record their joint angles or Cartesian coordinates to create a series of keypoints. These keypoints are integrated into a "Track" which can be played back later.

The **Track List Window** is as shown:

![Track List](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/mainPage.png)

- **1**: From left to right, the function keys respectively represent: edit track, delete track, play track once, and play track in a loop.
- **2**: By clicking the "add track" button, you can add and edit a new trajectory.

When you click "edit" or "add track", you'll navigate to the detailed track editing interface:

![Track Edit](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/teachingEditPage.png)

- **1**: Edit the name of the track.
- **2**: Save the current track and return to the previous menu.
- **3**: Add new actions here. You can opt to record the current position or add a "wait" action. When selecting to record the current position, you can decide whether to use **MoveJ**, **MoveL**, or **MoveS** to move to that keypoint. These three commands serve the same purpose as **A:MoveJ**, **A:MoveL**, and **A:MoveS** in the WScript section that follows.
- **4**: Set the time needed to move to the recorded point, with a default value of 2 seconds.
- **5**: You can delete key points or adjust their order in the list, either moving them up or down.

#### 5. Running WScript

![WScript Interface](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/WScriptPage.png)

- **1**: From left to right on the toolbar, the functions respectively represent: execute once, repeat execution specified times, and save Script. Note that unsaved changes will be lost when switching pages.
- **2**: Simply type the specified commands into the textbox to program the robot arm easily. WScript integrates trajectory planning functionality, ensuring that the robot arm's end position, speed, and acceleration are all continuous throughout the trajectory, guaranteeing smooth operation and preventing vibrations caused by sudden stops.

Current main commands provided by WScript include:

- **A:MOVEJ** - Move from the current position to a given absolute rotation joint angle within the specified time.
- **A:MOVEL** - Move from the current end position to a given absolute Cartesian coordinate position within the specified time.
- **A:MOVES** - Move from the current end position through a series of given absolute Cartesian coordinate positions within the specified time.
- **R:MOVEJ** - Move from the current position to a given relative rotation joint angle within the specified time.
- **R:MOVEL** - Move from the current end position to a given relative Cartesian coordinate position within the specified time.
- **R:MOVES** - Move from the current end position through a series of given relative Cartesian coordinate positions within the specified time.
- **WAIT** - Wait for the specified time.

**Note**: The "A" prefix denotes absolute positions, while "R" signifies relative positions. In Cartesian coordinates, absolute positions are relative to the robot arm's base coordinates, while relative positions are in relation to the end position's coordinates at the start of the action.

Each line can have one command. By combining these commands, you can implement more complex actions. However, if the specified action cannot be executed by the robot arm, such as moving outside its working space, the software will not execute the specified trajectory. In this case, pressing the start button will have no effect, and the terminal will display an error message. If the trajectory is verified to be executable, pressing the start button will initiate the movement immediately. Ensure there are no obstructions around the robot arm.

#### 6. Parameter Settings

![Server Settings Interface](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/serverSettingPage.png)

The image above showcases the common server settings. Of particular note, the "end effector length" signifies the distance from the output shaft of the sixth joint to the user-selected end effector. When this length is set, the forward and inverse kinematics in the software will use the end of the end effector as the reference coordinate system.

In the "Robot Setting" page (as shown below):

![Robot Settings Interface](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/robotSettingPage.png)

- **2**: The two rows of numbers can be used to set the two preset positions in the bottom right corner of **1**.
- Using the "Read" button, you can directly read the current joint angles of the robot arm, making it convenient for you to record them.
- After setting, click the "Save" button to save; if you need to undo any modifications, you can click the "Reset" button at any time to return to the previously saved data.

---

### STR400 Robot Arm Kinematics Model & Motion Planning

<a name="str400-robot-arm-kinematics-model--motion-planning"></a>

### 1. Robot Arm Modeling

![Robot Arm Description](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/robotDescription.png)

#### 1.1 Joint Angle Definition

As shown above, the robot arm has a total of 6 joint angles from J1 to J6, with the direction of the yellow arrow representing the positive direction. For example, in the posture displayed, the joint angles of the robot arm are 0°, 0°, 90°, 0°, 90°, 0°.

#### 1.2 Joint Angle Range

The range of joint angles is as follows:

- **J1:** -170° to 170°
- **J2:** -120° to 120°
- **J3:** -120° to 120°
- **J4:** -145° to 145°
- **J5:** -110° to 110°
- **J6:** -170° to 170°

#### 1.3 Robot Arm End Cartesian Space Position Definition

As shown in the diagram, the end coordinates of the robot arm pass through the axis of J6 and point outward. At the J6=0° position, the x-coordinate is parallel to the world y-axis of the robot arm, and the y-coordinate is parallel to the world x-axis of the robot arm, both in the positive direction.

As shown in the second row of numbers in the top right corner of the figure, the position of the end of the robot arm can be described by the transformation from the world coordinates to the current coordinates. We use x, y, z, Roll, Pitch, Yaw in the Euler angle intrinsic rotation method to indicate this (more information on this can be found [here](https://en.wikipedia.org/wiki/Davenport_chained_rotations#:~:text=Intrinsic%20rotations%20are%20elemental%20rotations,rotates%2C%20while%20xyz%20is%20fixed.)).

The position shown in the figure is: first translate x=0mm, y=158mm, z=203mm. Then rotate 180° around its x-axis, 0° around its y-axis, and -90° around its z-axis. Note that during rotation, the coordinate system's positive direction faces you, clockwise is a negative rotation, and counterclockwise is a positive rotation.

### 2. Motion Planning Methods

#### 2.1 MOVEL

`MOVEL` is a linear motion command that directs the robot arm to move directly in a straight line from its current position to the target position, with both the starting and ending speeds being zero.

![MOVEL Illustration](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/MOVEL.png)

This command includes the target's Cartesian coordinates and time. The Cartesian coordinates indicate the three translations and three Euler angles relative to the robot arm's base {B}, rotating in the order of Roll, Pitch, Yaw. Time represents the duration needed to move from the current position to the target position, in seconds.

#### 2.2 MOVES

Similar to `MOVEL`, but `MOVES` is primarily used to describe continuous multi-point motion. When there's only one `MOVES` command in the instruction, it functions the same as `MOVEL`. When there are multiple consecutive `MOVES` commands, the system integrates these commands, ensuring that the end of the robot arm can pass through the specified positions at the predetermined times, while also ensuring the continuity of the entire motion.

![MOVES Illustration](https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/MOVES.png)

Each `MOVES` command also includes the target's Cartesian coordinates and time. Time indicates the duration needed to move from the previous target position to the next one, in seconds.

#### 2.3 WScript Example

```plaintext
A: MOVEL X1, Y1, Z1, Roll1, Pitch1, Yaw1, Time1
A: MOVEL X2, Y2, Z2, Roll2, Pitch2, Yaw2, Time2
WAIT Time3
A: MOVES X4, Y4, Z4, Roll4, Pitch4, Yaw4, Time4
A: MOVES X5, Y5, Z5, Roll5, Pitch5, Yaw5, Time5
A: MOVES X6, Y6, Z6, Roll6, Pitch6, Yaw6, Time6
```

The explanation of this WScript segment is as follows:

- **1**： The robot arm moves in a straight line from its current position to position 1 over Time1, with its speed dropping to zero.
- **2**： Immediately after, the robot arm moves in a straight line to position 2 over Time2, again with its speed dropping to zero.
- **3**： The robot arm remains stationary at position 2 for Time3.
- **4**: Afterward, the robot arm begins continuous multi-point motion. First, it moves to position 4 over Time4, then to position 5 over Time5, and finally to position 6 over Time6.

Task complete

---

### Python API examples

<a name="python-api examples"></a>

TBD
