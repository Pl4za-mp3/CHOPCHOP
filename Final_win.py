from text import *

class Final_win(QWidget):
   def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
   def set_appear(self):
        self.setWindowTitle('Joselito')
        self.resize(700, 500)
        self.move(700, 300) 
   def initUI(self):
        self.despedida= QLabel('su orden ha sido procesada, ya se esta preparando!')
        self.line = QVBoxLayout()
        self.line.addWidget(self.despedida, alignment= Qt.AlignCenter)
        self.setLayout(self.line)

        