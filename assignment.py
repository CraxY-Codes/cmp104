import math
msg = input('what shape would you like to find the area?')


#msg triangle
if msg == 'triangle':
    base = int(input('what is the base?'))
    height = int(input('what is the height?'))
    area = 1/2 * (base * height)
    print('the area of {}= {}'.format(msg, area))

#msg rectangle
elif msg == 'rectangle':
    length = int(input('what is the length?'))
    breadth = int(input('what is the breadth?'))
    area = length * breadth
    print('the area of {}= {}'.format(msg, area))

#msg square
elif msg == 'square':
    length = int(input('what is the length?'))
    area = length ** 2
    print('the area of {}= {}'.format(msg, area))

#msg circle
elif msg == 'circle':
    radius = int(input('what is the radius?'))
    pie = math.pi
    area = pie * radius ** 2
    area = round(area, 2)
    print('the area of {}= {}'.format(msg, area))

#msg kite
elif msg == 'kite':
    diagonal_1 = int(input('what is the diagonal_1?'))
    diagonal_2 = int(input('what is the diagonal_2?'))
    area = diagonal_1 * diagonal_2 / 2
    print('the area of {}= {}'.format(msg, area))

#msg parallelogram
elif msg == 'parallelogram':
    base = int(input('what is the base?'))
    height = int(input('what is the height?'))
    area = base * height
    print('the area of {}= {}'.format(msg, area))

#msg rhombus
elif msg == 'rhombus':
    diagonal_1 = int(input('what is the diagonal_1?'))
    diagonal_2 = int(input('what is the diagonal_2?'))
    area = diagonal_1 * diagonal_2 / 2
    print('the area of {}= {}'.format(msg, area))


