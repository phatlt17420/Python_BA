import turtle as t

from numpy.ma.core import sqrt

############################################
# t.bgcolor("black")
# t.color('red')
# def curve():
#     for i in range (200):
#         t.right(1)
#         t.forward(1)
# t.speed(3)
# t.left(140)
# curve()
# t.left(120)
# curve()
# t.forward(111.65)
# t.right(140)
# t.forward(111.65)
# t.mainloop()
###########################################
t.bgcolor('black')
colors = ['red', 'green', 'blue', 'yellow']
for i in range(200):
    t.color(colors[i % len(colors)])
    t.fd(i)
    t.left(90)

t.mainloop()