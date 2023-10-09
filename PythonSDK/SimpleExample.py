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
