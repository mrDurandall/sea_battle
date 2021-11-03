from random import randint

from common.const import SHIPS, SEA, LIFE_SHIP, KILLED_SHIP, BLOCKED
from common.const import SIZE, STATUS, COORDINATES, OK, WOUNDED, KILLED
from common.const import HIT, MISS, INCORRECT, HEIGHT, WIDTH


class Field:

    def __init__(self):
        self.field = self.new_field()
        self.ships = []
        for ship in SHIPS:
            self.ships.append({
                SIZE: ship,
                STATUS: OK,
                COORDINATES: []
            })

    @staticmethod
    def new_field():
        return [[SEA for _ in range(HEIGHT)] for _ in range(WIDTH)]

    def set_random(self):
        for ship in self.ships:
            correct_position = False
            while not correct_position:
                rotation = randint(0, 1)
                correct_position = True
                if rotation == 0:
                    spx = randint(0, WIDTH - 1 - ship[SIZE])
                    spy = randint(0, HEIGHT - 1)
                    points = [[x, spy] for x in range(spx, spx + ship[SIZE])]
                    for point in points:
                        if self.field[point[0]][point[1]] != SEA:
                            correct_position = False
                            break
                else:
                    spx = randint(0, WIDTH - 1)
                    spy = randint(0, HEIGHT - 1 - ship[SIZE])
                    points = [[spx, y] for y in range(spy, spy + ship[SIZE])]
                    for point in points:
                        if self.field[point[0]][point[1]] != SEA:
                            correct_position = False
                            break
            ship[COORDINATES] = points

            # Расставляем корабль и блокируем соседние клетки
            for point in points:
                self.field[point[0]][point[1]] = LIFE_SHIP
                self.blocking_cells(point)

        # Чистим заблокированные клетки
        for x in range(len(self.field)):
            for y in range(len(self.field[0])):
                if self.field[x][y] == BLOCKED:
                    self.field[x][y] = SEA

    def shoot(self, x, y):
        if self.field[x][y] == LIFE_SHIP:
            self.field[x][y] = KILLED_SHIP
            for ship in self.ships:
                if [x, y] in ship[COORDINATES]:
                    ship[SIZE] -= 1
                    if ship[SIZE] != 0:
                        ship[STATUS] = WOUNDED
                    else:
                        ship[STATUS] = KILLED
                        for point in ship[COORDINATES]:
                            self.blocking_cells(point)
                    print(self.is_end())
                    return HIT, ship[STATUS]
        elif self.field[x][y] in (KILLED_SHIP, BLOCKED):
            return INCORRECT
        else:
            self.field[x][y] = BLOCKED
            return MISS

    def set_ships(self, ships):
        self.field = self.new_field()
        self.ships = ships
        for ship in ships:
            for cell in ship[COORDINATES]:
                self.field[cell[0]][cell[1]] = LIFE_SHIP

    def blocking_cells(self, point):
        for x in range(point[0] - 1, point[0] + 2):
            for y in range(point[1] - 1, point[1] + 2):
                if 0 <= x <= WIDTH - 1 and 0 <= y <= HEIGHT - 1 and self.field[x][y] == SEA:
                    self.field[x][y] = BLOCKED

    def is_end(self):
        print(sum((ship[SIZE] for ship in self.ships)))
        return not sum((ship[SIZE] for ship in self.ships))

    def __str__(self):
        strfield = '   1 2 3 4 5 6 7 8 9 10\n 1 '
        for x in range(len(self.field[0])):
            for y in range(len(self.field)):
                strfield += f'{self.field[y][x]} '
            strfield += f'\n{x + 2:2} '
        # for x in self.field:
        #     strfield += f'{" ".join(x)}\n'
        # for ship in self.ships:
        #     print(ship)
        return strfield


if __name__ == '__main__':
    field = Field()
    field.set_random()
    print(field)
    while True:
        shoot = list(map(lambda x: int(x), input('введите координаты\n').strip().split()))
        print(field.shoot(shoot[0] - 1, shoot[1] - 1))
        print(field)
