class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('Запуск рисунка.')
class Pen(Stationery):
    def draw(self):
        print('Рисунок ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Рисунок карандашом')
class Handle(Stationery):
    def draw(self):
        print('Рисунок маркером')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()