import pygame as pg
import numpy as np

class GraphRenderer:
    width: int
    height: int

    def __init__(self, width: int = 500, height: int = 500):
        self.width = width
        self.height = height
    
    def draw_arrow(self, screen, color, start, end, width=1, arrow_size=8):
        start = np.array(start, dtype=float)
        end = np.array(end, dtype=float)

        # Draw main line
        pg.draw.aaline(screen, color, start, end, width)

        # Direction vector
        direction = end - start
        length = np.linalg.norm(direction)
        if length == 0:
            return

        direction /= length

        # Perpendicular vector
        perp = np.array([-direction[1], direction[0]])

        # Arrowhead points
        arrow_tip = end
        left = arrow_tip - arrow_size * direction + (arrow_size / 2) * perp
        right = arrow_tip - arrow_size * direction - (arrow_size / 2) * perp

        pg.draw.polygon(screen, color, [arrow_tip, left, right])


    def draw(self, graph, directed=False):
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
            if directed:
                for u, v, w in graph.edges:
                    self.draw_arrow(
                        screen,
                        weight_to_red(w),
                        points[u],
                        points[v],
                        width=1,
                        arrow_size=10
                    )
            else:
                for edge in graph.edges:
                    pg.draw.aaline(
                        screen,
                        weight_to_red(edge[2]),
                        points[edge[0]],
                        points[edge[1]],
                        1
                    )

            for point in points:
                pg.draw.circle(screen, 'red', point, 4)
            
            pg.display.flip()
        pg.quit()
