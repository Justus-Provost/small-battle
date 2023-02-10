from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys
 
class Window(QWidget):
    
    def __init__(self):
        self.resources = "pyqt6_small_battle/resources/"
        super().__init__()
        self.resize(690, 500)
        self.setWindowTitle("IDK")
        self.setWindowIcon(QIcon(self.resources+"icon.png"))
        self.GUI()

        #button = QPushButton("Hello World!",self)
        #button.move(295,345)
        # player 1's buttons
        attack_p1 = QPushButton("P1: ATTACK!",self)
        attack_p1.move(125,200)
        defend_p1 = QPushButton("P1: Defend",self)
        defend_p1.move(125,250)
        heal_p1 = QPushButton("P1: Heal",self)
        heal_p1.move(125,300)
        # player 2's buttons
        attack_p2 = QPushButton("P2: ATTACK!",self)
        attack_p2.move(475,200)
        defend_p2 = QPushButton("P2: Defend",self)
        defend_p2.move(475,250)
        heal_p2 = QPushButton("P2: Heal",self)
        heal_p2.move(475,300)
        # the update button
        update = QPushButton("UPDATE",self)
        update.move(295,400)
        # the mode selection buttons
        normal = QPushButton("Normal",self)
        normal.move(195,400)
        custom = QPushButton("Custom",self)
        custom.move(395,400)

 
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