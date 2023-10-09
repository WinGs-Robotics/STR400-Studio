---
### Table of Contents

1. [Version Information & Update Log](#version-information--update-log)
2. [Download & Installation](#download--installation)
3. [UI Feature Overview](#ui-feature-overview)
4. [STR400 Robotic Arm Kinematics Model & Motion Planning Methods](#str400-robotic-arm-kinematics-model--motion-planning-methods)
5. [websocket APIs and Python SDK](#python-api-examples)
---

### Version Information & Update Log

<a name="version-information--update-log"></a>

This update is the first update, with a version serial number of v0.253.

---

### Download & Installation

<a name="download--installation"></a>

#### 1. Downloading the Software

Go to the [WinGs Robotics STR400 Studio Github Page](https://github.com/WinGs-Robotics/STR400-Studio/tree/main/APP) and download the entire folder. It contains executable files and corresponding configuration files.

**System Compatibility Tests**:

- Windows 10 (x86)
- Ubuntu 22.04 (x86)

**Recommended Hardware Configuration**:

- **CPU**: 11th gen Intel(R) Core(TM) i5-1135G7 @ 2.8Ghz 1.69Hz
- **RAM**: 8GB
- **GPU**: Intel UHD Graphic

#### 2. Connecting the Device

Ensure the power supply is connected and the USB data cable is properly inserted. Check if the computer has successfully recognized the USB data port.

#### 3. Launching the Program

Based on your OS (Windows, Mac (Intel), or Linux), locate the respective executable and launch it. Upon successful launch, you'll see the following window:

<p>&nbsp;</p>

<div align="center">    
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/terminal.png" width="500">
</div>

<p>&nbsp;</p>

Next, open a browser and visit [http://localhost:8080] to enter the APP interface.

> **Note**: If you wish to access the service from another device within the same LAN, ensure the STR400 Studio backend service runs on the PC. Additionally, you'll need to know the IP address of the PC running `str-studio` executable, and make sure the 8080 port is not firewalled.

---

### UI Feature Overview

<a name="ui-feature-overview"></a>

#### 1. Serial Port Connection

After successfully launching the program and accessing the front-end interface through the browser, you'll see the following UI:

<p>&nbsp;</p>

<div align="center">
    <img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/connectionPage.png" width="1000">
</div>

<p>&nbsp;</p>

- **1**: Displays the communication rate, currently only supporting a baud rate of 2.25M. The refresh button on the right can help you re-detect all USB connection statuses.
- **2**: Click to attempt connection to the corresponding serial port.
- **3**: Toggle option for the interface language.

#### 2. Dashboard

Once connected, you'll enter the main interface of the STR Studio:

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/mainPage.png" width="1000">
</div>

<p>&nbsp;</p>

- **1**: Function selection area, where you can view the robot's dashboard, Teaching function, W Script, and Configuration settings.
- **2**: A 3D model representation of the robotic arm. You can use the mouse to rotate, pan, and zoom in/out on the model.
- **3**: QR code for mobile control. Scanning this QR code with a mobile phone will open the robot control interface on the phone.
- **4**: Common quick actions, including emergency stop, passive mode, zeroing, and two preset positions.
- **5**: This section displays the current status of the robotic arm, as well as the status and progress of the ongoing task.

#### 3. Mobile Controller

By scanning the QR code on the dashboard with a phone, you can get a similar control interface on the mobile. This feature allows you to control the robotic arm from anywhere within the same LAN.

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/mobilePage.png" width="300">
</div>

<p>&nbsp;</p>

#### 4. Teaching Feature

The teaching feature allows users to create a series of key points by manually rotating the robotic arm joints and recording their joint angles or Cartesian coordinate positions. These key points are integrated into a "Track" and can be played back.

**Track List Window** is shown below:

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/teachingPage.png" width="1000">
</div>

<p>&nbsp;</p>

- **1**: From left to right, the function keys respectively represent: edit track, delete track, play track once, and repeat play track.
- **2**: By clicking the "add track" button, you can add and edit a track.

Upon clicking "Edit" or "Add Track", you'll be directed to the detailed track editing interface:

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/teachingEditPage.png" width="1000">
</div>

<p>&nbsp;</p>

- **1**: Edit the track name.
- **2**: Save the current track and return to the previous menu.
- **3**: Add a new action here. You can choose to record the current position or add a "wait" action. After selecting to record the current position, you can decide which method to use to move to this key point, choosing between **MoveJ**, **MoveL**, or **MoveS**. The functions of these three commands are equivalent to the **A:MoveJ**, **A:MoveL**, and **A:MoveS** in the next subsection about WScript.
- **4**: Set the time required to move to the recorded point, with a default value of 2 seconds.
- **5**: You can delete a key point or adjust its order in the list, including moving it up or down.

#### 5. Running WScript

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/WScriptPage.png" width="1000">
</div>

<p>&nbsp;</p>

- **1**: From left to right on the toolbar, the functions are: run once, repeat execution by a specified number of times, save Script. Note that unsaved changes will be lost when switching pages. If the specified motion is impossible for the robotic arm to execute, for instance, if it's out of the workspace, the software will not execute the specified track. In such cases, clicking the start button will have no response, and the terminal will display an error message. If the track verification succeeds, clicking the start button will immediately begin execution. Ensure there are no obstacles around the robotic arm during operation.
- **2**: Just enter the specified command in the text box, and you can easily program the robotic arm. WScript has built-in trajectory planning, ensuring that the endpoint of the robotic arm is continuous in position, velocity, and acceleration during the movement, ensuring smooth operation and preventing vibrations caused by sudden stops.

WScript currently provides the following main commands:

- **A:MOVEJ** - Move from the current position to the given absolute rotation joint angle within the specified time.
- **A:MOVEL** - Move from the current endpoint position to the given absolute Cartesian coordinate position within the specified time.
- **A:MOVES** - Move from the current endpoint position through a series of given absolute Cartesian coordinate positions within the specified time.
- **R:MOVEJ** - Move from the current position to the given relative rotation joint angle within the specified time.
- **R:MOVEL** - Move from the current endpoint position to the given relative Cartesian coordinate position within the specified time.
- **R:MOVES** - Move from the current endpoint position through a series of given relative Cartesian coordinate positions within the specified time.
- **WAIT** - Wait for the specified time.

**Note**: The prefix "A" stands for absolute positioning, while "R" indicates relative positioning. In Cartesian coordinates, the absolute position is relative to the robotic arm's base coordinate, while the relative position is relative to the end position coordinate at the beginning of the action.

Each line can have one command. By combining these commands, you can achieve more complex actions. But be cautious: if the specified action cannot be executed by the robotic arm, such as being out of the workspace, the software will not execute the specified trajectory. In this case, clicking the start button will have no response, and the terminal will display an error message. If the trajectory verification succeeds, clicking the start button will immediately begin execution. Make sure there are no obstacles around the robotic arm during operation.

#### 6. Parameter Settings

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/serverSettingPage.png" width="1000">
</div>

<p>&nbsp;</p>

The above image showcases the common server settings. Particularly noteworthy is the "End Effector Length", which denotes the distance from the output shaft of the sixth joint to the user-selected end effector. After setting this length, the software's forward and inverse kinematics will take the end of the end effector as the reference coordinate system.

On the "Robot Setting" page (as shown below):

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/robotSettingPage.png" width="1000">
</div>

<p>&nbsp;</p>

- **2**'s two rows of numbers can be used to set the two preset positions in the lower right corner of **1**.
- By using the "Read" button, you can directly read the current joint angles of the robotic arm for easy recording.
- Once set, click the "Save" button to save; if you want to undo changes, you can click the "Reset" button at any time to return to the previously saved data.

---

### STR400 Robotic Arm Kinematics Model & Motion Planning Methods

<a name="str400-robotic-arm-kinematics-model--motion-planning-methods"></a>

### 1. Robotic Arm Modeling

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/robotDescription.png" width="1000">
</div>

<p>&nbsp;</p>

#### 1.1 Joint Angle Definition

As shown in the image above, the robotic arm has 6 joint angles from J1 to J6. The yellow arrow direction indicates the positive direction. For instance, in the posture displayed in the image, the joint angles of the robotic arm are 0°, 0°, 90°, 0°, 90°, 0°.

#### 1.2 Joint Angle Range

The ranges of the joint angles are:

- **J1:** -170° to 170°
- **J2:** -120° to 120°
- **J3:** -120° to 120°
- **J4:** -145° to 145°
- **J5:** -110° to 110°
- **J6:** -170° to 170°

#### 1.3 Robotic Arm End Cartesian Space Position Definition

As depicted in the image, the terminal coordinates of the robotic arm's axis pass through the J6 axis heart and point outward. In the position of J6=0°, the x-coordinate is parallel to the robotic arm's world coordinate y-axis, and the y-coordinate is parallel to the robotic arm's world coordinate x-axis, both in the positive direction.

The second row of numbers in the upper right corner of the image indicates that the position of the robotic arm's end can be described by transforming from the world coordinates to the current coordinates. We use the x, y, z, Roll, Pitch, Yaw method, rotating by Euler angles intrinsically (for more information on this, [click here](https://en.wikipedia.org/wiki/Davenport_chained_rotations#:~:text=Intrinsic%20rotations%20are%20elemental%20rotations,rotates%2C%20while%20xyz%20is%20fixed.)).

The position shown in the image is: first, translate x=0mm, y=158mm, z=203mm. Then, in sequence, rotate around its own x-axis by 180°, y-axis by 0°, and z-axis by -90°. Note that during the rotation, the coordinate system's positive direction faces oneself; clockwise is negative rotation, and counterclockwise is positive rotation.

### 2. Motion Planning Methods

#### 2.1 MOVEL

`MOVEL` is a linear motion command. It causes the robotic arm to move directly along a straight line from its current position to the target position, with a speed of zero at the start and end.

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/MOVEL.png" width="300">
</div>

<p>&nbsp;</p>

This command contains the target position's Cartesian coordinates and time. Cartesian coordinates represent three translations and three Euler angles relative to the robotic arm's base {B}, rotating in the order Roll, Pitch, Yaw. Time indicates the duration required to move from the current position to the target position, in seconds.

#### 2.2 MOVES

Similar to `MOVEL`, but `MOVES` is primarily used to describe continuous multi-point movements. When the command contains only one `MOVES` command, it's the same as `MOVEL`. When there are multiple consecutive `MOVES` commands, the robot will move from the starting point to the next point along the direct line, maintaining continuous velocity and acceleration at the end position of each point.

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/MOVES.png" width="400">
</div>

<p>&nbsp;</p>

The three main considerations for trajectory planning:

1. Ensure the robotic arm moves smoothly, maintaining continuous position, velocity, and acceleration.
2. The real trajectory should be close to the target trajectory.
3. Try to minimize the execution time.

---

### WebSocket APIs and Python SDK

<a name="python-api-examples"></a>

#### 1. WebSocket APIs

##### 1.1 Websocket Service

Service Port: Defaults to 8080, can be changed in `Parameter Settings` > `Host Computer Settings`  
Websocket URI is `/api/ws`, local access address: `ws://localhost:{port}/api/ws`

##### 1.2 Data Format

The data format is a json string.

##### 1.3 Update Frequency

The frequency at which the host computer retrieves robotic arm information is approximately 50HZ, and the frequency to send commands to the robotic arm is also 50HZ.

Commands sent too quickly will be discarded, and the host computer synchronizes according to the last received frontend instruction.

###### 1.4 Information Initiated by the Host Computer

The host computer will actively push updates on the state of the robotic arm with a 50HZ update frequency.

```typescript
{
  event: "StatusUpdate",
  payload:
  {
    jointState: {
      jointEnabled: JointVector; // Servo status (0:Off/1:On)
      encoderAbsolutePositions: JointVector; // Encoder absolute reading 0 ~ 32767
      jointAngle: JointVector, // Joint angle -180 ~ 180
      cartesianPosition: Position, // Cartesian coordinates
      jointTemperature: JointVector; // Joint temperature
      jointErrorCode: JointVector; // Error code (0:Normal,1:Under-voltage,2:High temperature,3:Overload)
    };
    jointSetting: {
      jointMaxCurrent: JointVector; // Set motor upper limit current[unit:MA](stall without warning)
      jointAccelerationDuration: JointVector; // Motor acceleration time (unit: milliseconds)
      jointDecelerationDuration: JointVector; // Motor deceleration time (unit: milliseconds)
      jointTargetSpeed: JointVector; // Motor operating speed[unit:(revolutions/minute)]
      jointPositionKp: JointVector; // Kp1 proportional coefficient (proportionality, larger value means higher stiffness)
      jointPositionKi: JointVector; // Ki1 integral coefficient (positioning, eliminates steady-state error)
      jointPositionKd: JointVector; // Kd1 differential coefficient (damping, prevents oscillation)
    };
    connected: boolean; // Whether the serial port is connected
  }
}
```

The host computer will actively push the operational status of the robotic arm task to the client. The two important data types are as shown below:

```typescript
interface JointVector = [number, number, number, number, number, number] // JointVector is an array with six floats, unit is degrees
interface Position = {x:number, y:number, z:number, roll:number, pitch:number, yaw:number} //Position is a json data, unit is meters and degrees

```

```typescript
{
  event: "TaskUpdate",
  payload:
  {
    type: string | null, // name of the task, null means the task has completed
    progress: number, // 0 ~ 1. progress of the task, a float number from 0 to 1
  }
}

{
  event: "StatusUpdate",
  payload:
  {
    jointState: {
      jointEnabled: JointVector; // Whether the motor is being driven
      jointAngle: JointVector; // Current angle
      cartesianPosition: Position; // Current end position
      jointSpeed: JointVector; // Current motor speed
      jointErrorCode: JointVector; // Error codes for each motor
      jointCurrent: JointVector; // Current current size for each motor
    };
  }
}

```

##### 1.5 Available Commands for Lower Machine

- Start

```json
{
  "action": "Enable",
  "payload": null
}
```

- Stop

```json
{
  "action": "Disable",
  "payload": null
}
```

> **Note**: Before calling "Disable", it's typically necessary to first "Stop", wait for 500ms, and then Disable. Otherwise, enabling it again might cause issues.

- Brake (stops the running task at the same time)

```json
{
  "action": "Stop",
  "payload": null
}
```

- Reset joint to zero

```json
{
  "action": "SetTask",
  "payload": {
    "type": "BackToZeroTask"
  }
}
```

- Real-time control

```json

// First, send SetTask to activate the external position tracking task
{
  "action":"SetTask",
  "payload": {
    "type":"RealTimePositionControlTask",
    "args": {"x":null, "y":null, "z": null, "roll":null, "pitch": null, "yaw": null}
  }
}

// Afterward, commands can be sent for real-time control
{
  "action":"RealTimePositionControl",
  "payload": {"x":null, "y":null, "z": null, "roll":null, "pitch": null, "yaw": null} // null means stop this dimension, true means increase this relative position, false means decrease this relative position
}

```

- WScript

```json
{
  "action": "SetTask",
  "payload": {
    "type": "WScriptTask",
    "args": {
      "script": "...", // WScript: string of the entire script
      "repeatCount": 1 // Number of repetitions, optional
    }
  }
}
```

- MoveJ

```json
{
  "action": "SetTask",
  "payload": {
    "type": "MoveJTask",
    "args": [0, 0, 0, 0, 0, 0, 0] // Joint angle positions, unit is degrees, the last one is time, unit is seconds
  }
}
```

- MoveL

```json
{
  "action": "SetTask",
  "payload": {
    "type": "MoveLTask",
    "args": [0, 0, 0, 0, 0, 0, 0] // Cartesian positions, unit is mm and degrees, the last one is time, unit is seconds
  }
}
```

- MoveS

```json
{
  "action": "SetTask",
  "payload": {
    "type": "MoveSTask",
    "args": [
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]
    ] // Several Cartesian positions, data is consistent with MoveLTask
  }
}
```

#### 2. Python SDK (experimental)

##### 2.1 Download and Use

Open [link](https://github.com/WinGs-Robotics/STR400-Studio/tree/main/PythonSDK) to download the directory. Within this directory, import STR400 to access the Python SDK. Ensure the STR400 APP is running and that the robot has completed serial port connection.

This SDK has been tested with Python 3.9.13.
Before running, you need to install the required Python packages.

```bash
pip install websocket-client
```

Here's a simple example:

```python
from STR400_SDK.str400 import STR400
import time

# Initialize the robot with the given host and port
robot = STR400(host='localhost', port=8080)

# Activate the robot
robot.enable()
print("Robot has been successfully enabled.")

# Command the robot to move its joints to the specified angles using MoveJ
print(
    "Initiating MoveJ to target angles [0, 0, 0, 0, 0, 0] over a duration of 6 seconds...")
angles = [0, 0, 0, 0, 0, 0, 6]
robot.movej(angles)

# Brief pause to allow the MoveJ command to be processed
time.sleep(0.5)

# Monitor the task status and wait until the MoveJ operation is completed
print("Monitoring task status until the MoveJ operation is completed...")
while True:
    task_status = robot.get_task_status()
    if task_status.get('type') is None:  # Check if task has concluded
        print("MoveJ operation completed.")
        break
    time.sleep(0.2)

# Deactivate the robot after operations are done
robot.disable()
print("Robot is now disabled.")
```

##### 2.2 Available Commands

Currently, the supported commands are as follows. Refer to the examples in the SDK folder for more details.

##### Read Commands

-**_Task Status_**: Returns the real-time status of the ongoing task. When task_status.name is null, it indicates an idle status and is ready to accept commands.

```python
task_status = robot.get_task_status()
print("Task Status:", task_status)
```

Sample output:

```python
Task Status: {'type': 'MoveJTask', 'progress': 0.9867109634551495}
```

-**_Robot Status_**: Returns the real-time status of the robot.

```python
robot_status = robot.get_robot_status()
print("Robot Status:", robot_status)
```

Sample output:

```python
Robot Status: {
'jointEnabled': [1, 1, 1, 1, 1, 1],
'jointAngle': [0, 0, 89.99176000244148, 0, 89.99176000244148, 0],
'cartesianPosition': {'x': 2.653931355114116e-17,
                      'y': 0.1577425676345506,
                      'z': 0.20302268576136304,
                      'roll': -179.983520004883,
                      'pitch': 7.017718262059415e-15,
                      'yaw': -90},
'encoderAbsolutePositions': [0, 0, 0, 0, 0, 0],
'jointTemperature': [0, 0, 0, 0, 0, 0],
'jointSpeed': [0, 0, 0, 0, 0, 0],
'jointErrorCode': [0, 0, 0, 0, 0, 0],
'jointRunning': [0, 0, 0, 0, 0, 0],
'jointCurrent': [0, 0, 0, 0, 0, 0]
}
```

##### Write Commands

-**_Initialization_**: Establish connection with the robotic arm.

```python
robot = STR400(host='localhost', port=8080)
```

-**_Enable Robot_**: Start the robotic arm.

```python
robot.enable()
```

-**_Disable Robot_**: Disable the robotic arm.

```python
robot.disable()
```

-**_Stop Robot_**: Immediately stop the robotic arm.

```python
robot.stop()
```

-**_Return to Zero Position_**: Move all robot joints to their zero position and calibrate.

```python
robot.back_to_zero()
```

-**_Activate Real-Time Position Control_**: Sends real-time position control commands to the robot. null means stop, true indicates the positive direction, and false denotes the reverse direction.

```python
robot.start_real_time_position_control()
```

-**_Real-time Position Control_**: Send real-time position control command to the robot. null means stop, true means positive direction, false means reverse direction.

```python
values = {"x":null, "y":null, "z": null, "roll":null, "pitch": null, "yaw": null} #boolean or null
robot.real_time_position_control(values)
```

-**_Execute WScript_**:Execute the given WScript on the robot.

```python
script_content = "... your script ..."
robot.wscript(script_content, repeatCount=1)
```

-**_MoveJ_**: Move robot joints to specified angles. Six angles, the last one is time in seconds.

```python
angles = [0, 0, 0, 0, 0, 0，0]
robot.movej(angles)
```
