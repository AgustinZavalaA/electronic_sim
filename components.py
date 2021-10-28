from PyQt5.QtGui import QPainter, QBrush, QPolygon
from PyQt5.QtCore import QPoint, QRect, Qt, QLine


class Switch:
    def __init__(self, coordinates: QPoint, inputs=list()) -> None:
        self.size = 40
        self.coordinates = coordinates
        self.state = False

    def draw(self, painter: QPainter) -> None:
        if self.state:
            painter.setBrush(QBrush(Qt.green))
        else:
            painter.setBrush(QBrush(Qt.red))
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
        self.size = 40
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


class LG_AND:
    def __init__(self, coordinates: QPoint, inputs=list()) -> None:
        self.size = 30
        self.coordinates = coordinates
        self.state = False
        self.inputs = inputs

    def draw(self, painter: QPainter) -> None:
        self.calculate_state()

        self.x, self.y = self.coordinates.x(), self.coordinates.y()
        self.h, self.w = 45, 45
        painter.drawArc(self.x - 32, self.y - 20, self.h, self.w, 270 * 16, 180 * 16)
        painter.drawLine(self.x - 10, self.y - 20, self.x - 10, self.y + 25)
        # PATAS TRASERAS
        painter.drawLine(self.x - 10, self.y - 10, self.x - 28, self.y - 10)
        painter.drawLine(self.x - 10, self.y + 10, self.x - 28, self.y + 10)
        # PATA DELANTERA
        painter.drawLine(self.x + 13, self.y, self.x + 30, self.y)

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
        if len(states) == 0:
            self.state = False
        else:
            self.state = not (False in states)


class LG_OR:
    def __init__(self, coordinates: QPoint, inputs=list()) -> None:
        self.size = 30
        self.coordinates = coordinates
        self.state = False
        self.inputs = inputs

    def draw(self, painter: QPainter) -> None:
        self.calculate_state()
        self.x, self.y = self.coordinates.x(), self.coordinates.y()
        self.h, self.w = 45, 45
        painter.drawArc(self.x - 32, self.y - 20, self.h, self.w, 270 * 16, 180 * 16)
        painter.drawArc(self.x - 52, self.y - 20, self.h, self.w, 270 * 16, 180 * 16)
        # LINEAS SEPARADORAS DE ARCOS
        painter.drawLine(self.x - 7, self.y - 20, self.x - 25, self.y - 20)
        painter.drawLine(self.x - 7, self.y + 25, self.x - 25, self.y + 25)
        # PATAS TRASERAS
        painter.drawLine(self.x - 10, self.y - 9, self.x - 35, self.y - 9)
        painter.drawLine(self.x - 10, self.y + 12, self.x - 35, self.y + 12)
        # PATA DELANTERA
        painter.drawLine(self.x + 13, self.y, self.x + 38, self.y)

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


class LG_NOT:
    def __init__(self, coordinates: QPoint, inputs=list()) -> None:
        self.size = 30
        self.coordinates = coordinates
        self.state = False
        self.inputs = inputs

    def draw(self, painter: QPainter) -> None:
        self.calculate_state()
        self.x, self.y = self.coordinates.x(), self.coordinates.y()
        painter.drawLine(self.x - 10, self.y - 20, self.x - 10, self.y + 25)
        painter.drawLine(self.x - 10, self.y - 20, self.x + 30, self.y)
        painter.drawLine(self.x - 10, self.y + 25, self.x + 30, self.y)
        # PATAS TRASERAS
        painter.drawLine(self.x - 10, self.y, self.x - 27, self.y)
        # PATA DELANTERA
        painter.drawLine(self.x + 47, self.y, self.x + 30, self.y)

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
        self.state = not (True in states)


class Cable:
    def __init__(self, line: QLine) -> None:
        self.line = line
        self.state = False

    def draw(self, painter: QPainter) -> None:
        painter.drawLine(self.line)

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
