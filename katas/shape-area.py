def shapeArea(n):
    area = 1
    sides = 4
    print(f'Solving for {n}')
    for i in range(1, n + 1):
        print(f'1st - i: {i}, area: {area}, sides: {sides}')
        area = area + sides * (i - 1)
        print(f'2nd - i: {i}, area: {area}, sides: {sides}')
    print(f'Area is {area}')


shapeArea(1)
shapeArea(2)
shapeArea(3)
'''
shapeArea(4)
shapeArea(5)
shapeArea(6)
shapeArea(7)
'''

'''
    if n == 1: 
        c = c + (s * (n -1))
        return c # 1
    
    
    if n == 2: 
        c = c + (s * (n - 1))
        return c # 5
    
    
    if n == 3: 
        c = c + (s * (n - 1))
        return c # 13
    
'''
