# Работа с итераторами внутри класса
# Похоже на принцип работы генератора
class hand:
  e=30
  def __init__(self,a,b):
    self.a=a
    self.b=b
    
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.a<self.e:
      p=self.a
      self.a+=self.b
      return p
    else:
      raise StopIteration # Остановка итерации


y=hand(2,9)
for u in y: # То же самое что и u=iter(y) и и next(u)
    print(u)