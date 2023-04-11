from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys
# Need to organize screen properly. After that make game end and clean up code and write rules.
class Window(QWidget):
    
    def __init__(self):
        self.resources = "pyqt6_small_battle/resources/"
        super().__init__()
        self.resize(690, 500)
        self.setWindowTitle("IDK")
        self.setWindowIcon(QIcon(self.resources+"icon.png"))
        self.GUI()
        self.text = "stats"
        self.p1_move = "null"
        self.p2_move = "null"
        self.push_normal()

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
        normal = QPushButton("Re/Start",self)
        normal.move(195,400)
        normal.clicked.connect(self.push_normal)
        custom = QPushButton("Custom",self)
        custom.move(395,400)
        custom.clicked.connect(self.push_custom)
        #if heal_p1 == True:
        #    print("player 1 healed")
        #display = QLineEdit("Stats", self)
        #display.move(295,100)
        #display.setText(self.text)
        #display = QLabel(self.text, self)
        #display.move(295,100)
        #display.setText(self.text)
        

 
    def GUI(self):
        
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        self.notes = QLabel("Notes: The custom mode is currently not available. This game is meant for 2 players. To start the game press (UPDATE). Rules: This game is meant for 2 players. To start the game press (UPDATE). One player will look away from the screen while the other chooses a move for which player they are. Then the 2 players will switch positions and the other player will choose while the 1st is looking away. After both players have chosen their move they need to click (UPDATE). This will calculate the moves and stats of the players. This is the gameplay loop and the goal of this game is to predict your players move like rock paper scissors. Each player has 3 moves Atack!, Defend and Heal. Attacking will damage the opponent unless they defend. Defending will reflect the damage done to you onto the other player. Healing will heal you unless the other player attacks. The game ends once a players HP falls below 1.")
        self.notes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.notes)
        self.notes.setWordWrap(True)
        
        self.player_1_stats = QLabel("Player 1 stats")
        #self.player_1_stats.move(125,100)
        self.player_1_stats.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.player_1_stats)
        self.player_2_stats = QLabel("Player 2 stats")
        #self.player_2_stats.move(475,100)
        self.player_2_stats.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        #self.player_2_stats.move(100,475)
        layout.addWidget(self.player_2_stats)
        """self.button = QPushButton("Attack", )
        self.button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button)
        if button:
            print("atk")"""
    def calculate(self,player_1,player_2):
        if self.p1_move == 'atk' and self.p2_move == 'atk':
            player_1['HP'] = int(player_1['HP']) - int(player_2['ATK'])
            player_2['HP'] = int(player_2['HP']) - int(player_1['ATK'])
        if self.p1_move == 'atk' and self.p2_move == 'def':
            player_1['HP'] = int(player_1['HP']) - int(player_2['ATK'])
            #pass
        if self.p1_move == 'atk' and self.p2_move == 'heal':
            player_2['HP'] = int(player_2['HP']) - int(player_1['ATK'])
        if self.p1_move == 'def' and self.p2_move == 'atk':
            player_2['HP'] = int(player_2['HP']) - int(player_1['ATK'])
            #pass
        if self.p1_move == 'def' and self.p2_move == 'def':
            pass
        if self.p1_move == 'def' and self.p2_move == 'heal':
            player_2['HP'] = player_2['HP'] + player_2['HEAL']
        if self.p1_move == 'heal' and self.p2_move == 'atk':
            player_1['HP'] = player_1['HP'] - player_2['ATK']
        if self.p1_move == 'heal' and self.p2_move == 'def':
            player_1['HP'] = player_1['HP'] + player_1['HEAL']
        if self.p1_move == 'heal' and self.p2_move == 'heal':
            player_2['HP'] = player_2['HP'] + player_2['HEAL']
            player_1['HP'] = player_1['HP'] + player_1['HEAL']
        # check HP
        if player_1['HP'] > player_1['MAXHP']:
            player_1['HP'] = player_1['MAXHP']
        if player_2['HP'] > player_2['MAXHP']:
            player_2['HP'] = player_2['MAXHP']
    def p1_attacked(self):
        self.p1_move = "atk"
        print("player 1 attacked")
    def p1_defended(self):
        self.p1_move = "def"
        print("player 1 defended")
    def p1_healed(self):
        self.p1_move = "heal"
        print("player 1 healed")
    def p2_attacked(self):
        self.p2_move = "atk"
        print("player 2 attacked")
    def p2_defended(self):
        self.p2_move = "def"
        print("player 2 defended")
    def p2_healed(self):
        self.p2_move = "heal"
        print("player 2 healed")
    def push_update(self):
        print("player 1" + str(self.p1_move))
        print("player 2" + str(self.p2_move))
        #self.display.DisplayText("hello")
        
        self.calculate(self.player_1, self.player_2)
        print("player 1 " + str(self.player_1))
        print("player 2 " + str(self.player_2))
        #self.label.setText(str("player 1 " + str(self.player_1) + "player 2 " + str(self.player_2)))
        self.player_1_stats.setText(str("Player 1: HP: "+str(self.player_1['HP'])))#+", ATK: "+str(self.player_1['ATK'])))
        self.player_2_stats.setText(str("Player 2: HP: "+str(self.player_2['HP'])))#+", ATK: "+str(self.player_2['ATK'])))
        #self.display.setText(self.text)
        self.notes.setText("Notes: The custom mode is currently not available. I will be adding (Random) buttons and custom stats later. Currently the button (Custom) does nothing. For rules again press (Re/Start). Remember: This works on the honor system don't change the other players move. Be nice:)")
        self.p1_move = "null"
        self.p2_move = "null"
        # End game messages and checks
        if (int(self.player_1['HP']) > 0) and (int(self.player_2['HP']) <= 0):
            self.notes.setText("Player 1 wins!.")
        if (int(self.player_1['HP']) <= 0) and (int(self.player_2['HP']) <= 0):
            self.notes.setText("It's a tie!")
        if (int(self.player_1['HP']) <= 0) and (int(self.player_2['HP']) > 0):
            self.notes.setText("Player 2 wins!")
    def push_normal(self):
        print("You chose normal.")
        self.player_1 = {'MAXHP': 3,'HP': 3,'ATK': 1,'HEAL': 1}
        self.player_2 = {'MAXHP': 3,'HP': 3,'ATK': 1,'HEAL': 1}
        self.notes.setText("Notes: The custom mode is currently not available. This game is meant for 2 players. To start the game and get rid of the rules press (UPDATE). Rules:-> One player will look away from the screen while the other chooses a move for which player they are. Then the 2 players will switch positions and the other player will choose while the 1st is looking away. After both players have chosen their move they need to click (UPDATE). This will calculate the moves and stats of the players. This is the gameplay loop and the goal of this game is to predict your players move like rock paper scissors. Each player has 3 moves Atack!, Defend and Heal. Attacking will damage the opponent unless they defend. Defending will reflect the damage done to you onto the other player. Healing will heal you unless the other player attacks. The game ends once a players HP falls below 1.")
    def push_custom(self):
        print("You chose custom.")
        self.player_1['MAXHP'] = get_custom('Player 1 MAXHP')
        self.player_1['ATK'] = get_custom('Player 1 ATK')
        self.player_1['HEAL'] = get_custom('Player 1 HEAL')
        self.player_2['MAXHP'] = get_custom('Player 2 MAXHP')
        self.player_2['ATK'] = get_custom('Player 2 ATK')
        self.player_2['HEAL'] = get_custom('Player 2 HEAL')
        self.player_1['HP'] = self.player_1['MAXHP']
        self.player_2['HP'] = self.player_2['MAXHP']
        """self.player_1 = {'MAXHP': get_custom('Player 1 MAXHP'),'ATK': get_custom('Player 1 ATK'),'HEAL': get_custom('Player 1 HEAL')}
        self.player_2 = {'MAXHP': get_custom('Player 2 MAXHP'),'ATK': get_custom('Player 2 ATK'),'HEAL': get_custom('Player 2 HEAL')}
        self.player_1['HP'] = self.player_1['MAXHP']
        self.player_2['HP'] = self.player_2['MAXHP']"""
        self.print_stats()
    def print_stats(self):
        print(self.player_1)
        print(self.player_2)
def get_custom(result):
    #num = ""
    #while(type(num) != int):
    while(True):
        try:
            num = int(input(str(result)+": "))
        except(ValueError):
            num = " "
        if(type(num) == int):
            return num

    
 
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

#if __name__ == "__main__":
#    main()
main()