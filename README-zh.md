### 目录

1. [下载与安装](#下载与安装)
2. [UI 界面功能介绍](#ui界面功能介绍)
3. [STR400 机械臂 kinematics 模型&运动规划方法](#str400-机械臂kinematics模型运动规划方法)
4. [Websocket API 和 Python SDK](#python-api示例)

---

### 下载与安装

<a name="下载与安装"></a>

#### 1. 下载软件

前往 [WinGs Robotics STR400 Studio Github 页面](https://github.com/WinGs-Robotics/STR400-Studio/tree/main) 页面右边下载最新的 release。其中包含了不同系统下的可执行文件。

**系统兼容性测试**:

- Windows 10 (x86)
- Ubuntu 22.04 (x86)

**建议的硬件配置**:

- **CPU**: 11th gen Intel(R) Core(TM) i5-1135G7 @ 2.8Ghz 1.69Hz
- **RAM**: 8GB
- **显卡**: Intel UHD Graphic

#### 2. 连接设备

请确保电源已连接并且 USB 数据线已插好。检查电脑是否已成功识别 USB 数据端口。

#### 3. 启动程序

根据您的操作系统（Windows、Mac（Intel）或 Linux），找到对应的可执行文件并启动。成功启动后，您将看到如下窗口：

<p>&nbsp;</p>

<div align="center">    
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/terminal.png" width="500">
</div>

<p>&nbsp;</p>
随后，使用浏览器打开 [http://localhost:8080] 以进入 APP 界面。

> **注意**: 若您想在同一局域网的其他设备上访问此服务，确保 STR400 Studio 后台服务在 PC 上运行。同时，您需要知道运行`str-studio`可执行文件的电脑的 IP 地址，并确保 8080 端口的防火墙保护已关闭。

---

### UI 界面功能介绍

<a name="ui界面功能介绍"></a>

#### 1. 串口连接

成功启动程序后，使用浏览器访问程序的前端界面，您会看到如下的界面：

<p>&nbsp;</p>

<div align="center">
    <img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/connectionPage.png"  width="1000">
</div>

<p>&nbsp;</p>

- **1**：显示通讯速率，目前仅支持 2.25M 波特率。右侧的刷新按钮可以帮助您重新检测所有的 USB 连接状态。
- **2**：点击可以尝试连接到对应的串口。
- **3**：切换界面的语言选项。

#### 2. 仪表盘

一旦连接成功，您将进入到 STR Studio 的主界面：

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/mainPage.png"  width="1000">
</div>

<p>&nbsp;</p>

- **1**：功能选择区域，可以查看机械臂的仪表盘、Teaching 功能、W Script 和 Configuration 设置。
- **2**：机械臂的三维模型展示，您可以使用鼠标来旋转、位移和缩放模型。
- **3**：手机控制的二维码。通过手机扫描此二维码，可以在手机端打开机械臂的控制界面。
- **4**：常用的快捷操作，包括急停、被动模式、归零、以及两个预设位置。
- **5**：这部分展示了机械臂的当前状态，以及正在执行的任务的状态和进度。

#### 3. 手机控制器

通过手机扫描仪表盘上的二维码，您可以在手机上得到与主界面相似的控制界面。该功能使得您可以在同一局域网内的任意位置控制机械臂。

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/mobilePage.png" width="300">
</div>

<p>&nbsp;</p>

#### 4. 示教功能

示教功能使用户能够通过手动旋转机械臂关节并记录其关节角或笛卡尔坐标位置来创建一系列关键点，这些关键点被整合为一个“Track”并可以进行回放。

**Track 列表窗口**如下所示：

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/teachingPage.png"  width="1000">
</div>

<p>&nbsp;</p>

- **1**： 从左到右，功能键分别代表：编辑 track、删除 track、单次播放 track、重复播放 track。
- **2**： 通过点击“add track”按钮，您可以新增并编辑一条轨迹。

点击“编辑”或“新增轨迹”后，您将进入到轨迹的详细编辑界面：

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/teachingEditPage.png"  width="1000">
</div>

<p>&nbsp;</p>

- **1**： 编辑轨迹的名称。
- **2**： 保存当前轨迹并返回至上一菜单。
- **3**： 在这里添加新的动作。可以选择记录当前位置，或者添加“等待”动作。当选择记录当前位置后，您可以决定使用 **MoveJ**、**MoveL** 或 **MoveS** 中的哪一种方法来移动到该关键点。这三个指令的作用等同于下一小节中 WScript 的**A:MoveJ**、**A:MoveL** 和 **A:MoveS**。
- **4**： 设定移动到所记录点所需的时间，缺省值为 2 秒。
- **5**： 您可以删除关键点，或调整其在列表中的顺序，包括上移或下移。

#### 5. 运行 WScript

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/WScriptPage.png"  width="1000">
</div>

<p>&nbsp;</p>

- **1**： 工具栏上从左到右的功能分别为：执行一遍、按指定次数重复执行、保存 Script。请注意，未保存的更改在切换页面后会被丢失。
- **2**： 您只需在文本框中输入指定的指令，即可轻松地为机械臂编程。WScript 内置了轨迹规划功能，确保机械臂的末端在运行轨迹中位置、速度、加速度都是连续的，从而确保运行的流畅性，并防止因急停引起的震动。

WScript 当前提供以下主要指令：

- **A:MOVEJ** - 从当前位置在指定时间内移动到给定的绝对旋转关节角度。
- **A:MOVEC** - 在指定时间内，沿非直线路径将机械臂从当前位置移动到预设的绝对笛卡尔坐标位置。
- **A:MOVEL** - 在指定时间内，沿直线路径将机械臂从当前位置移动到预设的绝对笛卡尔坐标位置。
- **A:MOVES** - 从当前末端位置在指定时间内经过一系列给定的绝对笛卡尔坐标位置。
- **R:MOVEJ** - 从当前位置在指定时间内移动到给定的相对旋转关节角度。
- **R:MOVEC** - 在指定时间内，沿非直线路径将机械臂从当前位置移动到相对的笛卡尔坐标位置。
- **R:MOVEL** - 在指定时间内，沿直线路径将机械臂从当前位置移动到相对的笛卡尔坐标位置。
- **R:MOVES** - 从当前末端位置在指定时间内经过一系列给定的相对笛卡尔坐标位置。
- **WAIT** - 等待指定的时间。

**备注**：前缀"A"表示绝对位置，而"R"表示相对位置。在笛卡尔坐标中，绝对位置是相对于机械臂的底座坐标，而相对位置则是相对于动作开始时的末端位置坐标。

每行可以输入一个命令，将这些命令组合在一起，您可以实现更复杂的动作。但请注意，如果指定的动作无法由机械臂执行，例如超出工作空间，则软件将不会执行指定轨迹，此时，点击开始按钮将没有任何响应，并且终端会显示错误消息。如果验证轨迹可以执行，点击开始按钮将立即开始执行，请确保机械臂周围没有障碍物。

#### 6. 参数设置

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/serverSettingPage.png"  width="1000">
</div>

<p>&nbsp;</p>

上述图像展示了常用的上位机设置。特别要注意的是，“末端执行器长度”表示从第六个关节的输出轴到用户选择的末端执行器的长度。当您设置了这个长度后，软件中的正逆运动学会将末端执行器的末端作为参考坐标系。

在“Robot Setting”页面（如下图所示）：

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/robotSettingPage.png"  width="1000">
</div>

<p>&nbsp;</p>

- **2** 的两行数字可以用来设置 **1** 中右下角的两个预设位置。
- 使用“Read”按钮，您可以直接读取当前机械臂的关节角度，方便您进行记录。
- 设置完成后，点击“Save”按钮进行保存；如果需要撤销修改，您可以随时点击“Reset”按钮回到之前保存的数据。

---

### STR400 机械臂 kinematics 模型&运动规划方法

<a name="str400-机械臂kinematics模型运动规划方法"></a>

### 1. 机械臂建模

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/robotDescription.png"  width="1000">
</div>

<p>&nbsp;</p>

#### 1.1 关节角定义

如上图所示，机械臂从 J1 到 J6 共有 6 个关节角，黄色箭头方向代表正方向。例如，在图中显示的姿势下，机械臂的关节角度是 0°, 0°, 90°, 0°, 90°, 0°。

#### 1.2 关节角范围

关节角度的范围如下：

- **J1:** -145° to 145°
- **J2:** -120° to 120°
- **J3:** -120° to 120°
- **J4:** -155° to 155°
- **J5:** -110° to 110°
- **J6:** -170° to 170°

#### 1.3 机械臂末端笛卡尔空间位置定义

如图所示，机械臂末端坐标的轴线经过 J6 的轴心并指向外部。在 J6=0° 的位置，x 坐标与机械臂的世界坐标 y 轴平行，而 y 坐标与机械臂的世界坐标 x 轴平行，这两个方向均为正方向。

如图中右上角第二排数字所示，机械臂末端的位置可以通过从世界坐标到当前坐标的转换来描述。我们使用 x, y, z, Roll, Pitch, Yaw 的方式，通过欧拉角内旋(intrinsic rotation)来标识(关于此的更多信息可以[点击这里](https://en.wikipedia.org/wiki/Davenport_chained_rotations#:~:text=Intrinsic%20rotations%20are%20elemental%20rotations,rotates%2C%20while%20xyz%20is%20fixed.)查看)。

如图中所示的位置是：先平移 x=0mm, y=158mm, z=203mm。然后再依次绕自身的 x 轴旋转 180°，y 轴旋转 0°，z 轴旋转-90°。注意，在旋转时，坐标系正方向朝向自己，顺时针为负旋转，逆时针为正旋转。

### 2. 运动规划方法

#### 2.1 MOVEL

`MOVEL` 是一种线性运动命令，它使机械臂从当前位置直接沿直线移动到目标位置，开始和结束时的速度都为零。

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/MOVEL.png" width="300">
</div>

<p>&nbsp;</p>

此命令包含目标位置的笛卡尔坐标及时间。笛卡尔坐标表示相对于机械臂基座{B}的三个平移量和三个欧拉角，按 Roll、Pitch、Yaw 的顺序进行旋转。时间表示从当前位置移动到目标位置所需的时长，单位为秒。

#### 2.3 MOVEC

`MOVEC` 是一种曲线运动命令，允许机械臂从当前位置沿着非直线路径移动到目标位置。

该命令指定了目标位置的笛卡尔坐标和所需的时间。与 `MOVEL` 类似，笛卡尔坐标表示相对于机械臂基座{B}的三个平移量和三个欧拉角，按 Roll、Pitch、Yaw 的顺序进行旋转。时间参数确定了机械臂从当前位置到达目标位置的时长，单位为秒。不同于 `MOVEL` 的是，`MOVEC` 允许在移动过程中调整路径，从而使得在工作空间边缘位置，也就是 IK 的解不连续的区域，或者奇异点附近工作成为了可能。

#### 2.3 MOVES

与 `MOVEL` 相似，但 `MOVES` 主要用于描述连续的多点运动。当指令中只有一条 `MOVES` 命令时，它与 `MOVEL` 相同。当有连续多条 `MOVES` 命令时，系统将整合这些命令，保证机械臂末端可以按预定时间点经过指定的位置，并确保整个运动过程的连续性。

<p>&nbsp;</p>

<div align="center">
<img src="https://github.com/WinGs-Robotics/STR400-Studio/raw/main/references/MOVES2.png" width="300">
</div>

<p>&nbsp;</p>

每条 `MOVES` 命令也包含目标位置的笛卡尔坐标及时间。时间指从前一个目标位置移动到下一个所需的时长，单位为秒。

#### 2.4 WScript 实例

```plaintext
A: MOVEL X1, Y1, Z1, Roll1, Pitch1, Yaw1, Time1
A: MOVEL X2, Y2, Z2, Roll2, Pitch2, Yaw2, Time2
WAIT Time3
A: MOVES X4, Y4, Z4, Roll4, Pitch4, Yaw4, Time4
A: MOVES X5, Y5, Z5, Roll5, Pitch5, Yaw5, Time5
A: MOVES X6, Y6, Z6, Roll6, Pitch6, Yaw6, Time6
```

此段 WScript 的解释如下：

- **1**： 机械臂从当前位置，经过`Time1`的时间，直线移动到位置 1，速度为零。
- **2**： 接着，机械臂经过`Time2`的时间，直线移动到位置 2，速度为零。
- **3**： 机械臂在位置 2 保持静止`Time3`的时间。
- **4**： 之后，机械臂开始连续的多点运动，首先在`Time4`内移动到位置 4，然后在`Time5`内移动到位置 5，最后在`Time6`内移动到位置 6，并使速度减为零。这三个移动中，机械臂的轨迹和结束时的速度可能会有所不同。

任务结束。

---

### WebSocket APIs 和 Python SDK

<a name="python-api示例"></a>

#### 1. WebSocket APIs

##### 1.1 Websocket 服务

服务端口: 默认为 8080，可以在 `参数设置` > `上位机设置`处更改  
Websocket URI 为 `/api/ws` , 本机访问地址：`ws://localhost:{port}/api/ws`

##### 1.2 数据格式

数据格式为 json 字符串

##### 1.3 更新频率

上位机的获取机械臂信息频率约为 50HZ，发送命令至机械臂频率也为 50HZ

过快发送的命令会被丢弃，上位机同步以最后收到的前端指令为准

###### 1.4 上位机主动信息

上位机会主动推送机械臂的状态更新，50HZ 更新频率

```typescript
{
  event: StatusUpdate,
  payload:
  {
    jointState: {
      jointEnabled: JointVector; // 伺服状态 (0:关闭/1:打开)
      encoderAbsolutePositions: JointVector; // 编码器绝对读数 0 ～ 32767
      jointAngle: JointVector, // 关节角 -180 ~ 180
      cartesianPosition: Position, // 迪卡尔坐标
      jointTemperature: JointVector; // 关节温度
      jointErrorCode: JointVector; // 故障代码(0:正常,1:欠压,2:高温,3:过载)
    };
    jointSetting: {
      jointMaxCurrent: JointVector; // 设置电机上限电流[单位:MA](堵转停止不警报)
      jointAccelerationDuration: JointVector; // 电机加速度时间(单位:毫秒)
      jointDecelerationDuration: JointVector; // 电机减速度时间(单位:毫秒)
      jointTargetSpeed: JointVector; // 电机运行速度[单位:(转/分钟)]
      jointPositionKp: JointVector; // Kp1 比例系数(比例,数值越大刚性越强)
      jointPositionKi: JointVector; // Ki1 积分系数(定位,消除稳态误差)
      jointPositionKd: JointVector; // Kd1 微分系数(阻尼,防止震荡)
    };
    connected: boolean; // 串口是否连接
  }
}


```

上位机会主动推送机械臂任务运行状态至客户端
其中两个重要数据类型如下所示

```typescript
interface JointVector = [number, number, number, number, number, number] // JointVector是一个有六个float的数组，单位是度
interface Position = {x:number, y:number, z:number, roll:number, pitch:number, yaw:number} //Position是一个json数据，单位时m和度
```

```typescript
{
  event: TaskUpdate,
  payload:
  {
    type: string | null, // task的名称, null 则为task运行完成
    progress: number, // 0 ~ 1. task的运行进度，0 ~ 1 的浮点数
  }
}


{
  event: StatusUpdate,
  payload:
  {
    jointState: {
        jointEnabled: JointVector; //电机是否被驱动
        jointAngle: JointVector; //当前角度
        cartesianPosition: Position;//当前末端位置
        jointSpeed: JointVector; //当前电机转速
        jointErrorCode: JointVector;//各个电机的错误代码
        jointCurrent: JointVector;//各个电机的当前电流大小
     };
  }
}
```

##### 1.5 下位机可用命令

- 启动

```json
{
  "action": "Enable",
  "payload": null
}
```

- 停止

```json
{
  "action": "Disable",
  "payload": null
}
```

> **注意**: 调用"Disable"之前通常需要先"Stop"，等待 500ms，再 Disable，否则在此 enable 可能会导致问题。

- 制动 (同时停止正在运行的任务)

```json
{
  "action": "Stop",
  "payload": null
}
```

- 关节归零

```json
{
  "action": "SetTask",
  "payload": {
    "type": "BackToZeroTask"
  }
}
```

- 实时控制

```json

// 首先发送SetTask激活外部位置追踪任务
{
  "action":"SetTask",
  "payload": {
    "type":"RealTimePositionControlTask",
    "args": {"x":null, "y":null, "z": null, "roll":null, "pitch": null, "yaw": null}
  }
}

// 之后可以发送命令来实时控制

{
  "action":"RealTimePositionControl",
  "payload": {"x":null, "y":null, "z": null, "roll":null, "pitch": null, "yaw": null} // null为这个维度停止，true为这个维度相对位置增加，false为这个维度相对位置减小
}

```

- WScript

```json
{
  "action": "SetTask",
  "payload": {
    "type": "WScriptTask",
    "args": {
      "script": "...", // WScript： 整个脚本的字符串
      "repeatCount": 1 // 重复次数，可选
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
    "args": [0, 0, 0, 0, 0, 0, 0] //关节角位置，单位是度，最后一位是时间单位是秒
  }
}
```

- MoveC

```json
{
  "action": "SetTask",
  "payload": {
    "type": "MoveCTask",
    "args": [0, 0, 0, 0, 0, 0, 0] //笛卡尔位置, 单位是mm和度，最后一位是时间单位是秒
  }
}
```

- MoveL

```json
{
  "action": "SetTask",
  "payload": {
    "type": "MoveLTask",
    "args": [0, 0, 0, 0, 0, 0, 0] //笛卡尔位置, 单位是mm和度，最后一位是时间单位是秒
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
    ] //数个笛卡尔位置，数据和MoveLTask一致
  }
}
```

#### 2. Python SDK (实验中，谨慎使用)

##### 2.1 下载并使用

打开[link](https://github.com/WinGs-Robotics/STR400-Studio/tree/main/PythonSDK),下载这个文件夹，在这个文件夹里 import STR400，可以得到 Python 的 SDK，需要 STR400 的 APP 运行着，并且和机械臂已经完成串口连接。

该 SDK 在 Python 3.9.13 完成测试。
在运行之前，需要安装必要的 python 包

```bash
pip install websocket-client
```

以下是一个简单的示例：

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

##### 2.2 可用命令

目前支持的命令如下，参照 SDK 文件夹里的 Example 了解更多

##### 读取命令

-**_任务状态_**: 返回正在运行的实时任务状态，task_status.name == null 的时候是闲置状态，可以接受命令

```python
task_status = robot.get_task_status()
print("Task Status:", task_status)
```

示例输出:

```python
Task Status: {'type': 'MoveJTask', 'progress': 0.9867109634551495}
```

-**_机器人状态_**: 返回实时机器人状态

```python
robot_status = robot.get_robot_status()
print("Robot Status:", robot_status)
```

示例输出:

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

##### 写入命令

-**_初始化_**: 与机械臂建立连接。

```python
robot = STR400(host='localhost', port=8080)
```

-**_启动机器人_**: 启动机械臂。

```python
robot.enable()
```

-**_禁用机器人_**: 禁用机械臂。

```python
robot.disable()
```

-**_停止机器人_**: 立即停止机械臂。

```python
robot.stop()
```

-**_回归零位置_**: 将所有机器人关节移动到其零位置，并校准。

```python
robot.back_to_zero()
```

-**_激活实时位置控制_**: 向机器人发送实时位置控制命令, null 为停止，true 为正方向，false 为反方向

```python
robot.start_real_time_position_control()
```

-**_实时位置控制_**: 向机器人发送实时位置控制命令, null 为停止，true 为正方向，false 为反方向

```python
values = {"x":null, "y":null, "z": null, "roll":null, "pitch": null, "yaw": null} #boolean or null
robot.real_time_position_control(values)
```

-**_执行 WScript_**: 在机器人上执行给定的 WScript。

```python
script_content = "... 你的脚本 ..."
robot.wscript(script_content, repeatCount=1)
```

-**_MoveJ_**: 将机器人关节移动到指定的角度，六个角度，最后一位是时间，单位是秒

```python
angles = [0, 0, 0, 0, 0, 0，0] #需要指定一个实际的关节角位置和时间区间
robot.movej(angles)
```

-**_MoveC_**: 将机器人关节移动到指定的笛卡尔位置，过程为非直线，六个数字分别是 x, y, z, roll, pitch, yaw，单位同样是 mm 和角度，最后一位是时间，单位是秒

```python
CartisianPose = [0, 0, 0, 0, 0, 0，0] #需要指定一个实际的笛卡尔位置和时间区间
robot.movel(CartisianPose)
```

-**_MoveL_**: 将机器人关节移动到指定的笛卡尔位置, 过程为直线，六个数字分别是 x, y, z, roll, pitch, yaw，单位同样是 mm 和角度，最后一位是时间，单位是秒

```python
CartisianPose = [0, 0, 0, 0, 0, 0，0] #需要指定一个实际的笛卡尔位置和时间区间
robot.movel(CartisianPose)
```
