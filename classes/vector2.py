class Vector2():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return 'Vector2({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return str(self)

    def get_neighbor(self, radius=1, include_self=False, include_neg=False):
        out = []
        for x in range(self.x - radius, self.x + radius + 1):
            for y in range(self.y - radius, self.y + radius + 1):
                if x < 0 or y < 0:
                    continue

                if x == self.x and y == self.y and not include_self:
                    continue

                out.append(Vector2(x, y))

        return out