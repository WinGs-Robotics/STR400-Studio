from STR400_SDK.str400 import STR400
import time

robot = STR400(base_url="ws://localhost:8080/api/ws")

# Example usage
response = robot.enable()
print(response)

time.sleep(500)

# MoveJ command
angles = [0, 0, 90, 0, 90, 0]
response = robot.movej(angles)
print(response)
