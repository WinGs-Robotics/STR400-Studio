from STR400_SDK.str400 import STR400
import time

robot = STR400(host='localhost', port=8080)

# Activate the robot
robot.enable()
time.sleep(0.5)
print("Robot has been successfully enabled.")

# Initiate MoveJ to move robot joints to the specified angles
print(
    "Initiating MoveJ to target angles [0, 0, 90, 0, 90, 0] over a duration of 6 seconds...")
angles = [0, 0, 90, 0, 90, 0, 6]
robot.movej(angles)
time.sleep(6.5)

# Begin real-time control
print("Entering Realtime control mode...")
robot.start_real_time_position_control()
time.sleep(0.5)

# Command to move the robot's X position forward for 2 seconds
print("Instructing the robot to move forward along the X-axis for 2 seconds...")
values = {"x": True, "y": None, "z": None,
          "roll": None, "pitch": None, "yaw": None}
robot.real_time_position_control(values)
time.sleep(2)

# Command to halt the robot's movement for 2 seconds
print("Halting robot movements for 2 seconds...")
values = {"x": None, "y": None, "z": None,
          "roll": None, "pitch": None, "yaw": None}
robot.real_time_position_control(values)
time.sleep(2)

# Command to move the robot's X position backward for 2 seconds
print("Instructing the robot to move backward along the X-axis for 2 seconds...")
values = {"x": False, "y": None, "z": None,
          "roll": None, "pitch": None, "yaw": None}
robot.real_time_position_control(values)
time.sleep(2)

# Once again, halt the robot's movement for 2 seconds
print("Halting robot movements again for 2 seconds...")
values = {"x": None, "y": None, "z": None,
          "roll": None, "pitch": None, "yaw": None}
robot.real_time_position_control(values)
time.sleep(2)

# Initiate MoveJ to reset robot joints to their default positions
print(
    "Initiating MoveJ to reset robot joints to default positions [0, 0, 0, 0, 0, 0] over 6 seconds...")
angles = [0, 0, 0, 0, 0, 0, 6]
robot.movej(angles)
time.sleep(6.5)

print("MoveJ operation to default positions completed.")

# Terminate all operations and deactivate the robot
robot.stop()
robot.disable()
print("Realtime control demonstration has concluded. Robot is now disabled.")
