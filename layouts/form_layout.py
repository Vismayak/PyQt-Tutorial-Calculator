import sys
from PyQt6.QtWidgets import QApplication,QFormLayout,QLineEdit,QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Horizontal Layout')
layout = QFormLayout()
layout.addRow("Name:",QLineEdit())
layout.addRow("Age:",QLineEdit())
layout.addRow("Job:",QLineEdit())
window.setLayout(layout)
window.show()
sys.exit(app.exec())