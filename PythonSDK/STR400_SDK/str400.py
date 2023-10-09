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

        thread = threading.Thread(target=self.run_forever)
        thread.daemon = True
        thread.start()

        time.sleep(2)  # 休眠一段时间确保WebSocket连接建立

    def on_message(self, ws, message):
        self.message_queue.put(json.loads(message))

    def send_request(self, action, payload=None):
        data = {
            "action": action,
            "payload": payload
        }
        self.ws.send(json.dumps(data))

        # 返回从服务器收到的下一条消息
        while True:
            try:
                return self.message_queue.get(timeout=5)
            except Empty:
                return None

    def run_forever(self):
        self.ws.run_forever()

    def enable(self):
        self.send_request("Enable")

    def disable(self):
        self.send_request("Disable")

    def stop(self):
        self.send_request("Stop")

    def back_to_zero(self):
        payload = {"type": "BackToZeroTask"}
        self.send_request("SetTask", payload)

    def external_position_control(self, task, args=None):
        payload = {"type": task, "args": args}
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

    def movel(self, positions):
        payload = {"type": "MoveLTask", "args": positions}
        self.send_request("SetTask", payload)

    def moves(self, positions):
        payload = {"type": "MoveSTask", "args": positions}
        self.send_request("SetTask", payload)

