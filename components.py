from PyQt5.QtGui import QPainter, QBrush, QPolygon
from PyQt5.QtCore import QPoint, QRect, Qt, QLine


# TODO EZER Y SAUL: implementar la funcionalidad de editar con click derecho,
# cambiar los metodos de dibujado


class Switch:
    def __init__(self, coordinates: QPoint, inputs=list()) -> None:
        self.size = 30
        self.coordinates = coordinates
        self.state = False

    def draw(self, painter: QPainter) -> None:
        if self.state:
            painter.setBrush(QBrush(Qt.green))
        else:
            painter.setBrush(QBrush(Qt.black))
        c = self.coordinates
        r = QRect(c.x() - self.size // 2, c.y() - self.size // 2, self.size, self.size)
        painter.drawRect(r)

    def hitbox(self, point) -> None:
        c = self.coordinates
        delta = self.size // 2
        if (
            point.x() > c.x() - delta
            and point.x() < c.x() + delta
            and point.y() > c.y() - delta
            and point.y() < c.y() + delta
        ):
            return True
        return False

    def change_state(self) -> None:
        self.state = not self.state

    def calculate_state(self) -> None:
        pass


class Bulb:
    def __init__(self, coordinates: QPoint, inputs=list()) -> None:
        self.size = 30
        self.coordinates = coordinates
        self.state = False
        self.inputs = inputs

    def draw(self, painter: QPainter) -> None:
        self.calculate_state()
        if self.state:
            painter.setBrush(QBrush(Qt.yellow))
        else:
            painter.setBrush(QBrush(Qt.black))
        c = self.coordinates
        p = QPolygon()
        p << QPoint(c.x(), c.y() + self.size // 2)
        p << QPoint(c.x() - self.size // 2, c.y() - self.size // 2)
        p << QPoint(c.x() + self.size // 2, c.y() - self.size // 2)
        painter.drawPolygon(p)

    def hitbox(self, point) -> None:
        c = self.coordinates
        delta = self.size // 2
        if (
            point.x() > c.x() - delta
            and point.x() < c.x() + delta
            and point.y() > c.y() - delta
            and point.y() < c.y() + delta
        ):
            return True
        return False

    def change_state(self) -> None:
        pass

    def calculate_state(self) -> None:
        states = [x.state for x in self.inputs]
        self.state = True in states


# TODO MAR: implementar el codigo de las clases and, or, not basandose en las
# clases bulb y switch
class LG_AND:
    pass


class LG_OR:
    pass


class LG_NOT:
    pass


class Cable:
    def __init__(self, line: QLine) -> None:
        self.line = line
        self.state = False

    def draw(self, painter: QPainter) -> None:
        painter.drawLine(self.line)
