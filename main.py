from turtle import *
bgcolor("white")
# Target Area
target_x = 50
target_y = 40
target_range = 30   # How close they need to be

# Function to Check Hit
def hit_target(x, y):
    return abs(50 - target_x) < target_range and abs(40 - target_y) < target_range

# write your pseudocode below
print("Welcome to the treasure hunt")
penup()
goto(50, 40)
pendown()
color("yellow")
circle(20)
penup()
color("black")
goto(0, 0)

done()