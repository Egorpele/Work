x = int(input("x="))
y = int(input("y="))
if x>0 and y>0:
    print('1 к.ч')
elif x<0 and y>0:
    print('2 к.ч')
elif x<0 and y<0:
    print('3 к.ч')
elif x>0 and y<0:
    print('4 к.ч')