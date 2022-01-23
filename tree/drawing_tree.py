

import turtle


def tree(branch_len, green_color, thickness, t):
    length_reducer = 1.7
    changer_degree = 1.4
    minimum_length = 5
    t.color((0,min(green_color,1),0))
    t.width(thickness)
    if branch_len > minimum_length:
        t.forward(branch_len)
        t.right(25)
        tree(branch_len/length_reducer, green_color*changer_degree, thickness/changer_degree, t)
        t.left(50)
        tree(branch_len/length_reducer,green_color*changer_degree, thickness/changer_degree, t)
        t.right(25)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(120)
    t.down()
    tree(100, 0.2, 10, t)
    my_win.exitonclick()

main()

