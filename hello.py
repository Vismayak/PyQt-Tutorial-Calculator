import sys
# Import releveant PyQt6 widgets and QApplication
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create the application's GUI
window = QWidget()
window.setWindowTitle("Hello App")
window.setGeometry(100,100,300,80)
helloMsg = QLabel('<h1>Hello World</h1>',parent=window)
helloMsg.move(60,15)

# Show GUI
window.show()

# App's event loop
sys.exit(app.exec())

