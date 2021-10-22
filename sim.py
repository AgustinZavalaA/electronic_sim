import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QFont, QPen, QBrush, QPolygon
from PyQt5.QtCore import QPoint, QRect, Qt, QLine
from components import Switch, Bulb, LG_AND, LG_OR, LG_NOT, Cable


class Simulation(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle("SIMULATION")
        self.setGeometry(100, 100, 640, 480)

        self.components = []
        self.connections = []

        # prueba
        self.components.append(Bulb(QPoint(320, 240)))

        self.show()

    def mousePressEvent(self, e) -> None:
        self.start = None
        for i, c in enumerate(self.components):
            if c.hitbox(e.pos()):
                self.start = i, e.pos()
                break
        else:
            lg_and = Switch(e.pos())
            self.components.append(lg_and)
        self.update()

    def mouseReleaseEvent(self, e) -> None:
        if self.start is not None:
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
            c.draw(painter)


def main() -> None:
    app = QApplication(sys.argv)
    window = Simulation()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
