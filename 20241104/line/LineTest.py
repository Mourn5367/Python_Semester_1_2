from Line import Line

li = Line(start= (1.0,2.0), end = (-1.0,3.0), color = 'red')
li.show()
print(f'length = {li.length():.5f}')

li2 = Line(end=(-1.0,3.0))
li2.show()