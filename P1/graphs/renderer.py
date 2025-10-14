import pygame as pg
import numpy as np

class GraphRenderer:
    width: int
    height: int

    def __init__(self, width: int = 500, height: int = 500):
        self.width = width
        self.height = height

    def draw(self, graph):
        pg.init()
        screen = pg.display.set_mode((self.width, self.height))
        running = True
        ar = graph.get_ar()
        scaling = np.array([int(self.width/2), int(self.height)/2]) 
        scaling = scaling * ([1, 1/ar] if ar > 1 else [ar, 1])
        scaling = scaling - [15, 15]
        translate = np.array([int(self.width/2), int(self.height)/2])
        points = graph.calculate_cords()
        points = list(map(lambda p: p * scaling + translate, points))

        def weight_to_red(weight):
            weight = max(0, weight)

            r = int(205*(1-weight))
            g = r
            b = r
            
            return (r, g, b)
        
        def weight_to_width(weight):
            return 1 + weight

        while running:
            screen.fill('white')
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    #sys.exit()
            for edge in graph.edges:
                pg.draw.aaline(screen, weight_to_red(edge[2]), points[edge[0]], points[edge[1]], 1)

            for point in points:
                pg.draw.aacircle(screen, 'red', point, 4)
            
            pg.display.flip()
        pg.quit()
