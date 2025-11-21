#En este archivo está el texto y las variales del programa
titulo_1 = 'ChopChop'
win_pos = 850, 450
win_size = 500, 385

main_win.setWindowTitle()
main_win.show()
h_line = QHBoxLayout()
h_line.addWidget(winner, alignment = Qt.AlignCenter)
main_win.setLayout(h_line)

