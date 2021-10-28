import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar, QPushButton
from PyQt5.QtGui import QPainter, QFont, QPen, QBrush, QPolygon
from PyQt5.QtCore import QPoint, QRect, Qt, QLine, QMetaObject, QPointF
from PyQt5.QtCore import QCoreApplication
from components import Switch, Bulb, LG_AND, LG_OR, LG_NOT, Cable


class Simulation(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.component_view = Ui_MainWindow()
        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle("SIMULATION")
        self.setGeometry(450, 50, 640, 480)

        self.components = []
        self.connections = []
        self.start = None
        self.moved_component = None

        # prueba
        self.components.append(Bulb(QPoint(320, 240)))

        self.show()

    def mousePressEvent(self, e) -> None:
        self.moved_component = None
        self.start = None
        if e.button() == Qt.LeftButton:
            for i, c in enumerate(self.components):
                if c.hitbox(e.pos()):
                    self.start = i, e.pos()
                    break
            else:
                if self.component_view.component_type == 1:
                    self.components.append(LG_AND(e.pos(), []))
                elif self.component_view.component_type == 2:
                    self.components.append(LG_OR(e.pos(), []))
                elif self.component_view.component_type == 3:
                    self.components.append(LG_NOT(e.pos(), []))
                elif self.component_view.component_type == 4:
                    self.components.append(Bulb(e.pos(), []))
                elif self.component_view.component_type == 5:
                    self.components.append(Switch(e.pos()))
        elif e.button() == Qt.RightButton:
            for i, c in enumerate(self.components):
                if c.hitbox(e.pos()):
                    self.moved_component = i, e.pos()
                    self.mouseMoveEvent(e)
                    break

        self.update()

    def mouseMoveEvent(self, event) -> None:
        if self.moved_component is not None:
            self.components[self.moved_component[0]].coordinates = event.pos()

    def mouseReleaseEvent(self, e) -> None:
        if self.start:
            for i, c in enumerate(self.components):
                if c.hitbox(e.pos()):
                    if i != self.start[0]:
                        l = Cable(QLine(self.start[1], e.pos()))
                        self.connections.append(l)
                        c.inputs.append(self.components[self.start[0]])
                    else:
                        c.change_state()
                    break

        self.update()

    def paintEvent(self, e) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.black))
        painter.setPen(QPen(Qt.black, 2))
        painter.setFont(QFont("bold", 16))

        for cable in self.connections:
            cable.draw(painter)

        for c in self.components:
            c.calculate_state()
        for c in self.components:
            c.draw(painter)


class Ui_MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(50, 50, 300, 400)
        self.setupUi(self)
        self.component_type = 0
        self.show()

    def setupUi(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.andButton = QPushButton(self.centralwidget)
        self.andButton.setGeometry(QRect(50, 30, 200, 50))
        self.andButton.setObjectName("andButton")
        self.orButton = QPushButton(self.centralwidget)
        self.orButton.setGeometry(QRect(50, 100, 200, 50))
        self.orButton.setObjectName("orButton")
        self.notButton = QPushButton(self.centralwidget)
        self.notButton.setGeometry(QRect(50, 170, 200, 50))
        self.notButton.setObjectName("notButton")
        self.ledButton = QPushButton(self.centralwidget)
        self.ledButton.setGeometry(QRect(50, 240, 200, 50))
        self.ledButton.setObjectName("ledButton")
        self.swButton = QPushButton(self.centralwidget)
        self.swButton.setGeometry(QRect(50, 310, 200, 50))
        self.swButton.setObjectName("swButton")

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Panel de Objetos"))
        self.andButton.setText(_translate("MainWindow", "AND"))
        self.orButton.setText(_translate("MainWindow", "OR"))
        self.notButton.setText(_translate("MainWindow", "NOT"))
        self.ledButton.setText(_translate("MainWindow", "LED"))
        self.swButton.setText(_translate("MainWindow", "SW"))
        self.andButton.clicked.connect(self.AndClicked)
        self.orButton.clicked.connect(self.OrClicked)
        self.notButton.clicked.connect(self.NotClicked)
        self.ledButton.clicked.connect(self.LedClicked)
        self.swButton.clicked.connect(self.SwClicked)

    def AndClicked(self):
        self.component_type = 1

    def OrClicked(self):
        self.component_type = 2

    def NotClicked(self):
        self.component_type = 3

    def LedClicked(self):
        self.component_type = 4

    def SwClicked(self):
        self.component_type = 5


def main() -> None:
    app = QApplication(sys.argv)
    window = Simulation()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
