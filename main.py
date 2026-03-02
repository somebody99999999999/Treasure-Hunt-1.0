from turtle import *

# The background color
bgcolor("white")

# Target Area
target_x = 50
target_y = 40
target_range = 30   # How close they need to be

# Function to Check Hit
def hit_target(x, y):
    return abs(50 - target_x) < target_range and abs(40 - target_y) < target_range

# write your pseudocode below

# The Welcome
print("Welcome to the treasure hunt?")

target_x == int(input("Enter your x coordinate "))

target_y == int(input("Enter your y coordinate "))

# Where the Treasure is
penup()
goto(50, 40)
pendown()
color("yellow")
circle(20)
penup()

# Back to the start
# color("black")
# goto(0, 0)


# To keep the window open
done()