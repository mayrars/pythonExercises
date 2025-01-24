import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(100,300,500,500)
        label = QLabel("Hello World", self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(100,100,300,300)
        label.setStyleSheet("background-color: red;"
                            "color: white;"
                            "font-weight: bold;"
                            "font-style: italic;")
        label.setAlignment(Qt.AlignTop | Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()