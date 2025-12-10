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
        self.setWindowTitle('Pedido')
        self.resize(700, 500)
        self.move(700, 300)
    def initUI(self):
        self.instrucciones= QLabel(second_win_text)
        self.menu = QLabel(menu)
        self.pedido = QLineEdit('que querria de nuestro menu?')
        self.botones = QPushButton('procesar orden')
        self.line = QVBoxLayout()
        self.line.addWidget(self.instrucciones, alignment= Qt.AlignCenter)
        self.line.addWidget( self.menu , alignment= Qt.AlignCenter)
        self.line.addWidget(self.pedido, alignment= Qt.AlignCenter )
        self.line.addWidget(self.botones , alignment= Qt.AlignCenter)
        self.setLayout(self.line)
    def connects(self):
        self.botones.clicked.connect(self.abrir_ventana)
    def abrir_ventana(self):
        self.hide()
        self.tw = Final_win()


sw = Second_win()
