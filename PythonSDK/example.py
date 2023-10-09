from STR400_SDK.str400 import STR400
import time

robot = STR400(host='localhost', port=8080)

# Example usage
response = robot.enable()
print(response)

time.sleep(1)

# MoveJ command
angles = [0, 0, 90, 0, 90, 0, 6]
response = robot.movej(angles)
print(response)
