# Функции
# First commit
def root(number):
  result = number ** 0.5
  return result

def exponents(a, b):
  result = a ** b
  return result

x =25
print(f'корень из {x} = {root(x)}')
x, y = 5, 3
print(f'{x} в степени {y} = {exponents(x, y)}')
