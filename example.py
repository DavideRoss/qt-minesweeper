from requests import Session
from threading import Thread
from time import sleep
from PySide2.QtCore import *
from PySide2.QtWidgets import *

name = 'Ross'
chat_url = 'https://build-system.fman.io/chat'
server = Session()

app = QApplication([])

text_area = QTextEdit()
text_area.setFocusPolicy(Qt.NoFocus)

message = QLineEdit()

layout = QVBoxLayout()
layout.addWidget(text_area)
layout.addWidget(message)

window = QWidget()
window.setLayout(layout)
window.show()

new_messages = []

def fetch_new_messages():
    while True:
        response = server.get(chat_url).text
        if response:
            new_messages.append(response)
        sleep(.5)

def display_new_messages():
    while new_messages:
        text_area.append(new_messages.pop(0))

def send_message():
    server.post(chat_url, {'name': name, 'message': message.text()})
    message.clear()

# Signals
message.returnPressed.connect(send_message)

timer = QTimer()
timer.timeout.connect(display_new_messages)
timer.start(1000)

thread = Thread(target=fetch_new_messages, daemon=True)
thread.start()

app.exec_()