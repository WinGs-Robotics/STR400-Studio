import websocket
import json
import time
import threading
from queue import Queue
from queue import Empty


class STR400:
    def __init__(self, host='localhost', port=8080):
        self.uri = f"ws://{host}:{port}/api/ws"
        self.ws = websocket.WebSocketApp(self.uri, on_message=self.on_message)
        self.message_queue = Queue()
        self.connected = False
        self.task_status = {}
        self.robot_status = {}

        thread = threading.Thread(target=self.run_forever)
        thread.daemon = True
        thread.start()

        time.sleep(2)

    def on_message(self, ws, message):
        data = json.loads(message)
        event_type = data.get('event')
        if event_type == 'TaskUpdate':
            self.task_status = data.get('payload', {})
        elif event_type == 'StatusUpdate':
            self.robot_status = data.get('payload', {}).get('jointState', {})
        else:
            self.message_queue.put(data)

    def send_request(self, action, payload=None):
        data = {
            "action": action,
            "payload": payload
        }
        self.ws.send(json.dumps(data))

    def run_forever(self):
        self.ws.run_forever()

    def enable(self):
        self.send_request("Enable")
        time.sleep(1)

    def disable(self):
        self.send_request("Stop")
        time.sleep(0.5)
        self.send_request("Disable")

    def stop(self):
        self.send_request("Stop")

    def back_to_zero(self):
        payload = {"type": "BackToZeroTask"}
        self.send_request("SetTask", payload)

    def start_real_time_position_control(self):
        payload = {"type": "RealTimePositionControlTask", "args": {"x": None, "y": None, "z": None,
                                                                   "roll": None, "pitch": None, "yaw": None}}
        self.send_request("SetTask", payload)

    def real_time_position_control(self, values):
        action = "RealTimePositionControl"
        self.send_request(action, values)

    def wscript(self, script, repeatCount=1):
        args = {"script": script, "repeatCount": repeatCount}
        payload = {"type": "WScriptTask", "args": args}
        self.send_request("SetTask", payload)

    def movej(self, angles):
        payload = {"type": "MoveJTask", "args": angles}
        self.send_request("SetTask", payload)

    def movec(self, positions):
        payload = {"type": "MoveCTask", "args": positions}
        self.send_request("SetTask", payload)

    def movel(self, positions):
        payload = {"type": "MoveLTask", "args": positions}
        self.send_request("SetTask", payload)

    def moves(self, positions):
        payload = {"type": "MoveSTask", "args": positions}
        self.send_request("SetTask", payload)

    def get_task_status(self):
        return self.task_status

    def get_robot_status(self):
        return self.robot_status
