class hang:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def out(self):
        print(self.a, self.b)


class left(hang): # Для обьвления дочернего класса, надо в скобках написать название родительского класса. Созданный класс будет наследовать свойства родительского, даже конструктор
    m = None

class right(hang):
    def __init__(self, a, b):
        hang.__init__(self, a, b) # Благодаря этой функции можно продолжить наследовать соответствующую функцию с родительского класса
        print(self.a, self.b)

class mid(hang):
    def __init__(self, a, b):
        super().__init__(a, b) # Наследует все свойства родительского класса


won=hang("Abcd", "Efgh")
won.out()

life=left("Q", True) # Разные обьекты одного класса независят друг от друга, если поменять атрибуты в классе в одном обьекте, это не изменит в другом
life.out()
won.out()

head=mid("will", 123)
head.out()