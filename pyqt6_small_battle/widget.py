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
        self.p1_move = "null"

        #button = QPushButton("Hello World!",self)
        #button.move(295,345)
        # player 1's buttons
        attack_p1 = QPushButton("P1: ATTACK!",self)
        attack_p1.move(125,200)
        #self.p1_move = attack_p1.clicked.connect("attack")
        attack_p1.clicked.connect(self.p1_attacked)
        defend_p1 = QPushButton("P1: Defend",self)
        defend_p1.move(125,250)
        defend_p1.clicked.connect(self.p1_defended)
        heal_p1 = QPushButton("P1: Heal",self)
        heal_p1.move(125,300)
        heal_p1.clicked.connect(self.p1_healed)
        # player 2's buttons
        attack_p2 = QPushButton("P2: ATTACK!",self)
        attack_p2.move(475,200)
        attack_p2.clicked.connect(self.p2_attacked)
        defend_p2 = QPushButton("P2: Defend",self)
        defend_p2.move(475,250)
        defend_p2.clicked.connect(self.p2_defended)
        heal_p2 = QPushButton("P2: Heal",self)
        heal_p2.move(475,300)
        heal_p2.clicked.connect(self.p2_healed)
        # the update button
        update = QPushButton("UPDATE",self)
        update.move(295,400)
        update.clicked.connect(self.push_update)
        # the mode selection buttons
        normal = QPushButton("Normal",self)
        normal.move(195,400)
        normal.clicked.connect(self.push_normal)
        custom = QPushButton("Custom",self)
        custom.move(395,400)
        custom.clicked.connect(self.push_custom)
        #if heal_p1 == True:
        #    print("player 1 healed")

 
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
    def p1_attacked(self):
        self.p1_move = "attacked"
        print("player 1 attacked")
    def p1_defended(self):
        print("player 1 defended")
    def p1_healed(self):
        print("player 1 healed")
    def p2_attacked(self):
        print("player 2 attacked")
    def p2_defended(self):
        print("player 2 defended")
    def p2_healed(self):
        print("player 2 healed")
    def push_update(self):
        print(str(self.p1_move))
    def push_normal(self):
        print("You chose normal.")
    def push_custom(self):
        print("You chose custom.")
 
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

#if __name__ == "__main__":
#    main()
main()