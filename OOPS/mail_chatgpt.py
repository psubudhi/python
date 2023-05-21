import sys
import threading

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication

from backend import Chatbot


class ChatBotWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 300)

        # Add chat area
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 300)

        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"Me : {user_input} ")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f" {response}")


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
