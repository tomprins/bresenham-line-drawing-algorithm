###########################
##   Author: Tom Prins   ##
###########################

# import the required library
from grid import Grid


def bresenham(x1, y1, x2, y2):
    # If the line is vertical, just add the points between the y-values
    # This needs to be a separate case, or a division by zero occurs
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)):
            g.addPoint(x1, y)

    # If the line is horizontal, just add the points between the x-values
    # This needs to be a separate case, or a division by zero occurs
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)):
            g.addPoint(x, y1)

    else:
        # First calculate the slope of the formula
        a = (y2 - y1)/(x2 - x1)

        # Assign 'x' to every whole x-value between the two points
        for x in range(min(x1, x2), max(x1, x2)+1):
            b = calculateY(a, x1, y1, x)
        # Depending on the direction of the line, you need a diffrent way, the y-value is asssigned
        if y1 > y2:
            # Assign 'y' to every whole y-value between the two points
            for y in range(max(y1, y2), min(y1, y2)-1, -1):
                calculateX(a, b, y)
        else:
            # Assign 'y' to every whole y-value between the two points
            for y in range(min(y1, y2), max(y1, y2)+1):
                calculateX(a, b, y)


def calculateX(a, b, y):
    # Calculate every x-value of the points, by iterating through every y-value, and putting it in the formula
    g.addPoint(round((y - b)/a), y)


def calculateY(a, x1, y1, x):
    # Calculate every y-value of the points, by iterating through every x-value, and putting it in the formula
    b = y1 - (a*x1)
    g.addPoint(x, round(a*x+b))
    # return 'b', so the function 'calculateX' doesn't have to calculate it again
    return b

g = Grid(100, 100)

bresenham(5, 30, 5, 70)
bresenham(20, 10, 80, 10)
bresenham(30, 30, 60, 60)
bresenham(8, 12, 90, 30)
bresenham(95, 40, 85, 95)
bresenham(5, 90, 60, 80)
bresenham(60, 30, 70, 80)
g.draw()
