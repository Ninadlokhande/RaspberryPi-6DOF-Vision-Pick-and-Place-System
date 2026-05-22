def calculate_position(cx, cy):

    if cx < 200:
        position = "LEFT"

    elif cx > 400:
        position = "RIGHT"

    else:
        position = "CENTER"

    return position
