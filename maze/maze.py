class maze:
    def __init__(self):
        self.road_open = []
        for x in range(5):
            for y in range(5):
                self.road_open[x][y] = True
        for x in range(2):
            for y in range(2):
                self.road_open[x+1][y+1] = True
    