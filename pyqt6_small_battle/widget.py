from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys
 
class Window(QWidget):
    
    def __init__(self):
        self.resources = "pyqt6_small_battle/resources/"
        super().__init__()
        self.resize(690, 690)
        self.setWindowTitle("IDK")
        self.setWindowIcon(QIcon(self.resources+"icon.png"))
        self.GUI()

        button = QPushButton("Hello World!",self)
        #button.move(345,345)
 
    def GUI(self):
        
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        label = QLabel("Weird boi")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        """self.button = QPushButton("Attack", )
        self.button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button)
        if button:
            print("atk")"""
 
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

#if __name__ == "__main__":
#    main()
main()