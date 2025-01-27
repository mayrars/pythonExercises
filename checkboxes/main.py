import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.checkbox = QCheckBox("Check me", self)
        self.initUI()
    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size: 20px;"
                                    "font-weight: bold;"
                                    "font-family: Arial;")

        self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("Checked")
        else:
            print("Unchecked")

#Define a function called main
def main():
    #Create a QApplication object with the command line arguments
    app = QApplication(sys.argv)
    #Create a MainWindow object
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()