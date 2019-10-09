from src.mi.miband2 import MiBand2
from bluepy.btle import BTLEDisconnectError
import time
import threading

# Constants
left_brace_mac = 'FB:EB:16:F9:95:85'
right_brace_mac = 'E5:73:4B:C7:7F:25'
max_reconnect_attempts = 10
reconnect_pause = 3

# GLOBALS
braces_connected = False
left_dev = None
right_dev = None


def init():
    global left_dev
    global right_dev
    global braces_connected

    # Left brace init
    left_dev_connection_attempts = 0
    left_successfully_connected = False
    while not left_successfully_connected and left_dev_connection_attempts < max_reconnect_attempts:
        try:
            print('Connecting to left brace ' + left_brace_mac)
            left_dev = MiBand2(left_brace_mac)
            left_dev.setSecurityLevel(level="medium")
            left_dev.authenticate()
            left_dev.init_after_auth()
            print("Left brace has been connected")
            left_successfully_connected = True
        except BTLEDisconnectError as e:
            print("BLE error. Trying to reconnect to left brace: " + str(e))
            left_successfully_connected = False
            left_dev_connection_attempts += 1
            time.sleep(reconnect_pause)
        except Exception as e:
            print("Trying to reconnect to left brace")
            left_successfully_connected = False
            left_dev_connection_attempts += 1
            time.sleep(reconnect_pause)

    # Right brace init
    right_dev_connection_attempts = 0
    right_successfully_connected = False
    while not right_successfully_connected and right_dev_connection_attempts < max_reconnect_attempts:
        try:
            print('Connecting to right brace ' + right_brace_mac)
            right_dev = MiBand2(right_brace_mac)
            right_dev.setSecurityLevel(level="medium")
            right_dev.authenticate()
            right_dev.init_after_auth()
            print("Right brace has been connected")
            right_successfully_connected = True
        except BTLEDisconnectError as e:
            print("BLE error. Trying to reconnect to right brace: " + str(e))
            right_successfully_connected = False
            right_dev_connection_attempts += 1
            time.sleep(reconnect_pause)
        except Exception as e:
            print("Trying to reconnect to left brace")
            right_successfully_connected = False
            right_dev_connection_attempts += 1
            time.sleep(reconnect_pause)

    braces_connected = left_successfully_connected and right_successfully_connected
    return braces_connected


def left_brace_up():
    left_dev.char_alert.write(b'\x02')
    time.sleep(0.3)
    left_dev.char_alert.write(b'\x00')


def right_brace_up():
    right_dev.char_alert.write(b'\x02')
    time.sleep(0.3)
    right_dev.char_alert.write(b'\x00')


def generate_vibration(bracelet_id):
    left_brace_thread = threading.Thread(target=left_brace_up)
    right_brace_thread = threading.Thread(target=right_brace_up)
    if bracelet_id == 0:
        left_brace_thread.start()
    elif bracelet_id == 1:
        right_brace_thread.start()
    elif bracelet_id == 2:
        left_brace_thread.start()
        right_brace_thread.start()


