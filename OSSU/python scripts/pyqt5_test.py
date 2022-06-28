from PyQt5.QtWidgets import *
import qdarkstyle

app = QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet())


window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
label = QLabel('Hello World!')
label.show()
window.show()
app.exec()