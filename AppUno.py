import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette


class StyledForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)  # Set window size
        self.setWindowTitle('Styled Form')  # Set window title

        # Set general style
        self.setFont(QFont('Source Sans Pro', 16))
        self.setStyleSheet("QWidget { background-color: #eff3f4; }")

        # Create layout
        layout = QVBoxLayout()

        # Email input
        self.email = QLineEdit()
        self.email.setPlaceholderText('Enter your email')
        self.email.setFont(QFont('Source Sans Pro', 20, QFont.Bold))
        self.email.setStyleSheet("""
            QLineEdit {
                padding: 14px;
                border: 2px solid #217093;
                border-radius: 4px;
                color: #353538;
                background-color: #f3fafd;
            }
            QLineEdit:focus {
                border: 2px solid #4eb8dd;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            }
        """)

        # Password input
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText('Enter your password')
        self.password.setFont(QFont('Source Sans Pro', 20, QFont.Bold))
        self.password.setStyleSheet(self.email.styleSheet())  # Use the same style as the email input

        # Submit button
        self.button = QPushButton('Submit')
        self.button.setFont(QFont('Source Sans Pro', 20, QFont.Bold))
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #4eb8dd;
                color: white;
                border-radius: 4px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #217093;
            }
        """)

        # Add widgets to layout
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(self.button)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StyledForm()
    ex.show()
    sys.exit(app.exec_())
