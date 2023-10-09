import requests
import json


class STR400:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, action, payload):
        data = {
            "action": action,
            "payload": payload
        }
        response = requests.post(self.base_url, json=data)
        return response.json()

    def enable(self):
        return self.send_request("Enable", None)

    def disable(self):
        return self.send_request("Disable", None)

    def stop(self):
        return self.send_request("Stop", None)

    def back_to_zero(self):
        payload = {"type": "BackToZeroTask"}
        return self.send_request("SetTask", payload)

    def external_position_control(self, task, args=None):
        payload = {"type": task, "args": args}
        return self.send_request("SetTask", payload)

    def real_time_position_control(self, values):
        action = "RealTimePositionControl"
        return self.send_request(action, values)

    def wscript(self, script, repeatCount=1):
        args = {"script": script, "repeatCount": repeatCount}
        payload = {"type": "WScriptTask", "args": args}
        return self.send_request("SetTask", payload)

    def movej(self, angles):
        payload = {"type": "MoveJTask", "args": angles}
        return self.send_request("SetTask", payload)

    def movel(self, positions):
        payload = {"type": "MoveLTask", "args": positions}
        return self.send_request("SetTask", payload)

    def moves(self, positions):
        payload = {"type": "MoveSTask", "args": positions}
        return self.send_request("SetTask", payload)
