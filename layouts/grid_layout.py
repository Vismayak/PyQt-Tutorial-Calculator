import sys
from PyQt6.QtWidgets import QApplication,QGridLayout,QPushButton,QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Grid Layout')
layout = QGridLayout()
layout.addWidget(QPushButton('Top Right'),0,0)
layout.addWidget(QPushButton('Center'),1,1)
layout.addWidget(QPushButton('Bottom Left from Center'),2,1,1,2)
window.setLayout(layout)
window.show()
sys.exit(app.exec())