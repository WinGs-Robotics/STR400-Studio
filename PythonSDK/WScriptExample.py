from STR400_SDK.str400 import STR400
import time

# Initialize the robot with the given host and port
robot = STR400(host='localhost', port=8080)

# Activate the robot and notify
robot.enable()
print("Robot has been successfully enabled.")

Script = """
A:MOVEJ 0,60,120,0,-90,0,6
R:MOVEL 0,0,150,0,0,0,2
R:MOVEL 0,0,-100,0,0,0,1.5
R:MOVEL 0,200,0,0,0,0,2
R:MOVEL 0,0,-200,0,0,0,2
R:MOVEL 0,0,150,0,0,-90,2
R:MOVEL 400,0,0,0,0,90,4
R:MOVEL 180,0,0,0,0,90,2
R:MOVEL 400,0,0,0,0,0,8

A:MOVEJ 0,0,90,0,90,0,4
R:MOVEJ 45,0,0,45,0,0,2
WAIT 0.5
//moveS group
R:MOVES 0,0,0,0,-15,0,1
R:MOVES 0,0,0,0,15,0,1.5
R:MOVES 0,0,0,0,0,0,1
WAIT 0.5
R:MOVEL 0,0,0,-45,0,0,2
R:MOVEL 0,0,150,0,0,0,2
WAIT 0.5
R:MOVEL 150,0,0,0,0,0,3
R:MOVEL -150,0,0,0,0,0,2
R:MOVEL 0,150,0,0,0,0,2
R:MOVEL 0,-150,0,0,0,0,2
WAIT 1
A:MOVEJ 0,0,90,0,90,0,5
"""

# Start executing the WScript and notify
robot.wscript(Script, repeatCount=1)
print("Executing WScript. Expected to run once...")
time.sleep(0.5)

# Monitor the task status and provide updates until the script execution concludes
try:
    while True:
        task_status = robot.get_task_status()
        print(
            f"Task Name: {task_status.get('type')}, Task Progress: {task_status.get('progress')}")

        # Check if the WScript execution has ended
        if task_status.get('type') is None:
            print("WScript execution concluded.")
            break

        time.sleep(0.2)  # Brief pause between status checks

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Stop the robot and provide a completion message
robot.stop()
print("Example successfully completed. Robot is now stopped.")
