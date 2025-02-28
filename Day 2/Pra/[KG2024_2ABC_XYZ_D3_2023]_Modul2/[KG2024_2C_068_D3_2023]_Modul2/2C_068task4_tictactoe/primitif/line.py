import numpy as np
import math

def round(x):
    return int(x+0.5)

def line_dda(xa, ya, xb, yb):    
    dx = abs(xb - xa)
    dy = abs(yb - ya)
    length = max(dx, dy)
    
    # Handle the case where the length is zero
    if length == 0:
        return np.array([[int(xa), int(ya)]])
    
    dx = (xb - xa) / length
    dy = (yb - ya) / length
    
    x = xa
    y = ya
    
    res = [[int(xa), int(ya)]]
    
    for i in range(int(length) + 1):    
        res.append([round(x), round(y)])
        x += dx
        y += dy
    
    return np.array(res)




def line_bresenham(xa,ya,xb,yb):
    if(abs(yb-ya) < abs(xb-xa)):
        if(xa > xb):
            return np.array(line_low(xb,yb,xa,ya))
        else:
            return np.array(line_low(xa,ya,xb,yb))
    else:
        if(ya > yb):
            return np.array(line_high(xb,yb,xa,ya))
        else:
            return np.array(line_high(xa,ya,xb,yb))
def line_low(xa, ya, xb, yb):
    res = [[int(xa), int(ya)]]
    dx = int(xb - xa)
    dy = int(yb - ya)
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    p = (2 * dy) - dx
    twody = 2 * dy
    twodydx = 2 * (dy - dx)
    y = int(ya)

    for x in range(int(xa), int(xb)):
        res.append([x, y])
        if p > 0:
            y += yi
            p += twodydx
        else:
            p += twody

    return res

def line_high(xa, ya, xb, yb):
    res = [[int(xa), int(ya)]]
    dx = int(xb - xa)
    dy = int(yb - ya)
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    p = (2 * dx) - dy
    twodx = 2 * dx
    twodxdy = 2 * (dx - dy)
    x = int(xa)

    for y in range(int(ya), int(yb)):
        res.append([x, y])
        if p > 0:
            x += xi
            p += twodxdy
        else:
            p += twodx

    return res
