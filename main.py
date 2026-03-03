from turtle import *

# The background color
bgcolor("white")

# Target Area
target_x = 50
target_y = 40
target_range = 30   # How close they need to be

# Function to Check Hit
def hit_target(x, y):
    return abs(x - target_x) < target_range and abs(y - target_y) < target_range

# write your pseudocode below

# The Welcome
print("Welcome to the treasure hunt?")

x = int(input("Enter your x coordinate "))

y = int(input("Enter your y coordinate "))

if hit_target(x, y):
    print("You hit")
    penup()
    goto(x, y)
    color("Yellow")
    pendown()
    begin_fill()
    circle(20)  
    end_fill()
    penup()
    forward(15)
    hideturtle()
else:
    print("You didn't hit it")
    penup()
    goto(x, y)
    color("Red")
    pendown()
    begin_fill()
    circle(20)  
    end_fill()
    penup()
    forward(15)
    hideturtle()


# To keep the window open
done()