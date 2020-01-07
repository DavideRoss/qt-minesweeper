from settings import *

class Vector2():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return 'Vector2({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return str(self)

    def get_neighbors(self, max_size, radius=1, include_self=False, check_inbound=True):
        out = []
        for x in range(self.x - radius, self.x + radius + 1):
            for y in range(self.y - radius, self.y + radius + 1):
                if not include_self and x == self.x and y == self.y:
                    continue

                if check_inbound and (x < 0 or y < 0 or x >= max_size.x or y >= max_size.y):
                    continue

                out.append(Vector2(x, y))

        return out

    def in_safe_zone(self, chk_x, chk_y, radius=1):
        for x in range(self.x - radius, self.y + radius + 1):
            for y in range(self.y - radius, self.y + radius +1):
                if x == chk_x and y == chk_y:
                    return True

        return False