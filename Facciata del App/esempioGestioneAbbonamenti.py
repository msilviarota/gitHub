import sys
from PyQt6.QtWidgets import(
    QApplication,QWidget,
    QVBoxLayout , QLabel,QPushButton
)
app= QApplication(sys.argv)
finestra = QWidget()
finestra.setWindowTitle("Gestione Abbonamenti")

etichetta =QLabel("Benvenuti nell'App del Gestione Abbonamenti")
pulsante= QPushButton("clicca qui")
pulsante2= QPushButton("esci")

layout =QVBoxLayout()

layout.addWidget(etichetta)
layout.addWidget(pulsante)
layout.addWidget(pulsante2)
finestra.setLayout(layout)
finestra.show()
app.exec()