from text import *
from Final_win import *

class Second_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle()
        self.resize(win_size)
        self.move(win_pos)
    def initUI(self):
        self.instrucciones= QLabel(second_win_text)
        self.menu = QLabel(menu)
        self.botones = QPushButton('pagar')
        h_line = QHBoxLayout()
        l_line = QVBoxLayout()
        r_line = QVBoxLayout()
        h_line.addWidget( self.menu , alignment= Qt.AlignCenter)
        l_line.addWidget(self.botones , alignment= Qt.AlignCenter)
        self.l_line.addWidget(self.button)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.boton.clicked.connect(self.show)
    def show(self):
        self.hide()
        self.tw = Final_win()


sw = Second_win()
