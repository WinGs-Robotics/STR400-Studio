from STR400_SDK.str400 import STR400
import time

# Initialize the robot with specified host and port
robot = STR400(host='localhost', port=8080)

# Activating the robot
robot.enable()
print("Robot successfully activated.")

# Commanding the robot to move its joints to specified angles using MoveJ
print(
    "Initiating MoveJ to target angles [0, 0, 0, 0, 0, 0] with a duration of 6 seconds...")
angles = [0, 0, 0, 0, 0, 0, 6]
robot.movej(angles)

# Brief pause to ensure the MoveJ command is processed
time.sleep(0.5)

# Monitoring task status and waiting for the completion of the MoveJ operation
print("Monitoring task status until MoveJ operation is completed...")
while True:
    task_status = robot.get_task_status()
    if task_status.get('type') is None:  # Check if the task has concluded
        print("MoveJ operation completed.")
        break
    time.sleep(0.2)

# Pause to ensure full completion of the operation
time.sleep(5)

# Commanding the robot to move to a specified Cartesian pose using MoveC
CartesianPose = [-41, 83, 603, 19, -26, -126, 10]
robot.movec(CartesianPose)
time.sleep(0.5)

print("Monitoring task status until the MoveC operation is completed...")
while True:
    task_status = robot.get_task_status()
    if task_status.get('type') is None:  # Check if the task has concluded
        print("MoveC operation completed.")
        break
    time.sleep(0.2)

# Pause to ensure full completion of the operation
time.sleep(5)

# Repeating MoveJ command to return to the initial joint angles
print(
    "Initiating MoveJ back to initial angles [0, 0, 0, 0, 0, 0] with a duration of 6 seconds...")
angles = [0, 0, 0, 0, 0, 0, 6]
robot.movej(angles)

# Brief pause to allow processing of the MoveJ command
time.sleep(0.5)

# Monitoring task status for the completion of the MoveJ operation
print("Monitoring task status until MoveJ operation is completed...")
while True:
    task_status = robot.get_task_status()
    if task_status.get('type') is None:  # Check if the task has concluded
        print("MoveJ operation completed.")
        break
    time.sleep(0.2)

# Disabling the robot after all operations are completed
robot.disable()
print("Robot is now disabled.")
