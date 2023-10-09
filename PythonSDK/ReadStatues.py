from STR400_SDK.str400 import STR400
import time

robot = STR400(host='localhost', port=8080)

# Example usage
robot.enable()

# MoveJ command
angles = [0, 0, 90, 0, 90, 0, 6]
robot.movej(angles)
time.sleep(0.5)
try:  # Exception handling block
    while True:
        task_status = robot.get_task_status()
        print("Task Name:", task_status.get('type'))
        print("Task Progress:", task_status.get('progress'))

        robot_status = robot.get_robot_status()
        print("Joint Angles:", robot_status.get('jointAngle'))
        print("Cartesian Position:", robot_status.get('cartesianPosition'))

        if task_status.get('type') is None:  # Check if task name is null
            break

        time.sleep(0.2)  # Delay for 200ms
except Exception as e:
    print("An error occurred:", e)

robot.stop()
print("Realtime control example completed. Robot Stopped")
