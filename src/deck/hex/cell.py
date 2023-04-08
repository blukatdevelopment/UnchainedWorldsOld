class Cell:
    def __init__(self, name, color, coords, terrain):
        self.name = name
        # Color
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

        # Cell coordinates on map, irrespective of scale
        self.x = coords[0]
        self.y = coords[1]
        self.terrain = terrain