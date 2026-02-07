import turtle as t
# def square (l):
#     for i in range(4):
#         t.fd(l)
#         t.left(90)
# square(500)
# t.mainloop()
# vẽ hình chữ nhật có chiều rộng w, chiều cao h
# def rectangle (w,h):
#     for i in range(2):
#             t.fd(w)
#             t.left(90)
#             t.fd(h)
#             t.left(90)
# rectangle(200,100)
###########################
# t.speed(5)
# t.tracer(1,10)
# for i in range(10,101,10):
#
#     if i/10 %2 ==0:
#         t.circle(i)
#     else:
#         t.circle(-i)
# t.mainloop()
###########################

# colors = ['green','blue','cyan','red','black','purple','yellow','gray']
# t.pensize(3)
# for i in range(12):
#     t.color(colors[i])
#     t.circle((i+1)*15)
#     t.color(colors[i+1])
#     t.circle((i + 1) * -10)
# t.mainloop()
###########################
# t.color('red')
# for i in range(0,360,15):
#     t.seth(i)
#     t.circle(100)
###########################
# colors = ['green','blue','cyan','red','black','purple','yellow','gray']
# for i in range (45):
#     t.color(colors[i %6])
#     t.pendown()
#     t.fd(2+i*5)
#     t.left(45)
#     t.width(i)
#     t.penup()
###########################
# def square (m):
#     t.color('green')
#     t.begin_fill()
#     for i in range(4):
#         t.fd(150)
#         t.left(90)
#     t.end_fill()
# def printxy (x,y):
#     if x>=0 and x<= 150 and y>=0 and y<=150:
#         print('in')
#     else:
#         print('out')
# square(150)
# t.onscreenclick()
# t.mainloop()
#
# t.mainloop()

#############################################
# t.forward(50)
# t.left(90)
# t.forward(100)
# t.right(45)
# t.mainloop()
#######################################
# t.fd(100)
# t.lt(120)
# t.fd(100)
# t.lt(120)
# t.fd(100)
# t.mainloop()
#######################################
# t.fd(100)
# t.lt(180)
# t.fd(200)
# t.lt(180)
# t.fd(100)
# t.lt(90)
# t.fd(50 + 50)
# t.lt(90 * 2)
# t.fd(40 + 80 * 2)
# t.mainloop()
#######################################

# for i in range(3):
#     t.fd(100)
#     t.left(120)
# for i in range(6):
#     t.fd(100)
#     t.left(60)
# for i in range(8):
#     t.fd(100)
#     t.left(45)
t.right(36)
for i in range(4):
    t.fd(100)
    t.left(144)
for i in range(3):
    t.left(120)
    t.fd(100)
    t.left(120)

t.mainloop()

















