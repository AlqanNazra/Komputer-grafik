import numpy as np

def round(x):
    return int(x + 0.5)

def line_dda(xa, ya, xb, yb):    
    dx = abs(xb - xa)
    dy = abs(yb - ya)
    length = max(dx, dy)
    
    dx = (xb - xa) / length
    dy = (yb - ya) / length
    
    x = xa
    y = ya
    
    res = [[xa, ya]]
    
    for i in range(length + 1):    
        res.append([round(x), round(y)])
        x = x + dx
        y = y + dy
    
    return np.array(res)

def line_bresenham(xa, ya, xb, yb):
    if abs(yb - ya) < abs(xb - xa):
        if xa > xb:
            return np.array(line_low(xb, yb, xa, ya))
        else:
            return np.array(line_low(xa, ya, xb, yb))
    else:
        if ya > yb:
            return np.array(line_high(xb, yb, xa, ya))
        else:
            return np.array(line_high(xa, ya, xb, yb))

def line_low(xa, ya, xb, yb, dash_length=0):
    res = [[xa, ya]]
    dx = xb - xa
    dy = yb - ya
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    p = 2 * dy - dx
    twody = 2 * dy
    twodydx = 2 * (dy - dx)
    y = ya
    
    draw = True
    count = 0

    for x in range(xa, xb):
        if draw:
            res.append([x, y])
        count += 1
        if count == dash_length:
            draw = not draw
            count = 0
        if p > 0:
            y += yi
            p += twodydx
        else:
            p += twody
    
    return res

def line_high(xa, ya, xb, yb, dash_length=0):
    res = [[xa, ya]]
    
    dx = xb - xa
    dy = yb - ya
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    p = 2 * dx - dy
    twodx = 2 * dx
    twodxdy = 2 * (dx - dy)
    x = xa
    
    draw = True
    count = 0

    for y in range(ya, yb):
        if draw:
            res.append([x, y])
        count += 1
        if count == dash_length:
            draw = not draw
            count = 0
        if p > 0:
            x += xi
            p += twodxdy
        else:
            p += twodx
    
    return res
