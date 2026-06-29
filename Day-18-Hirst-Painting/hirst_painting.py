import turtle as t 
import random
# import colorgram

color_list =[(233, 232, 233), (231, 237, 233), (236, 234, 231), (222, 226, 232), (208, 82, 160), (54, 131, 89), (146, 40, 91), (140, 48, 26), (222, 108, 206), (132, 203, 177), (158, 83, 45), (47, 103, 55), (167, 38, 160), (128, 143, 189), (84, 44, 20), (36, 70, 42), (187, 105, 93), (187, 170, 139), (84, 181, 123), (59, 31, 39), (78, 165, 153), (88, 91, 157), (195, 72, 79), (45, 78, 74), (161, 220, 202), (80, 44, 73), (57, 121, 131), (218, 188, 176), (220, 166, 183), (166, 165, 207), (179, 211, 188), (149, 35, 37), (46, 71, 73), (45, 62, 65)]

# colors = colorgram.extract('image.jpg',60)

# for color in colors:
#     r= color.rgb.r
#     g= color.rgb.g
#     b= color.rgb.b
#     new_color = (r ,b ,g)
#     color_list.append(new_color)

# print(color_list)

timmy = t.Turtle()
t.colormode(255)
# timmy.shape("turtle")
timmy.speed("fastest")
 
timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.fd(300)
timmy.setheading(0)
for i in range (10):
    for j in range (10):
        color=random.choice(color_list)
        timmy.dot(20,color)
        timmy.fd(50)
    timmy.setheading(90)
    timmy.fd(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


display = t.Screen()
display.exitonclick()
 
