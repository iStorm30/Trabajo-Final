import pygame
import sys
import coords
import algorithms as a
from math import sqrt
import sys
pygame.init() 

clock = pygame.time.Clock()

WIDTH = coords.total_w * 30
HEIGHT = coords.total_h * 30 
FILENAME = "result.path"
DOT_COLOR = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH + 200, HEIGHT + 200))

pygame.mouse.set_visible(True)

pygame.display.set_caption('TSP Solution')



screen.fill((255, 184, 108))

from_scratch = False
start = 0
if "--start" in sys.argv:
    from_scratch = True
    start = int(sys.argv[2])
    print(f"Computing MST starting from {coords.data.iloc[start]['Distritos']}")


def remap_coord(x, y):
    return ( int(100 + x*WIDTH), int(100 + HEIGHT - (y*HEIGHT)))
def draw_point(x, y):
    pygame.draw.circle(screen, (0,0,255), remap_coord(x,y), 3, 1)

for x, y in zip(coords.x, coords.y):
    draw_point(x,y)

def euclidean_dist(row_a, row_b):
    return sqrt((row_a['X'] - row_b['X'])**2 + (row_a['Y'] - row_b['Y'])**2)

vs = []
if a.p == None or from_scratch:
    print("No MST loaded. Computing it now using Prim's algorithm... (~2 min)\n")


    for index, (label, current) in enumerate(coords.data.iterrows()):
        rowed = [(vi, euclidean_dist(current, v)) for vi, (_, v) in enumerate(coords.data.iterrows())]
        rowed = sorted(rowed, key=lambda x: x[-1])[:15]
        vs += [rowed]
  

    a.p = a.prim(vs, start)
    f = open(FILENAME, 'w')
    f.write(' '.join(map(str, a.p)))
    f.close()
    print("Saved MST on 'result.path'")
else:
    print("MST loaded from 'result.path'")



# draw path 
print("Path to follow...")

print(len(vs))
print(len(a.p))
cost = 0
for i, n in enumerate(a.p):
    if n != -1:
        dist = euclidean_dist(coords.data.iloc[i], coords.data.iloc[n])
        cost += dist

        pygame.draw.line(screen, (255,0,0), remap_coord(coords.x[i], coords.y[i]), 
                                            remap_coord(coords.x[n], coords.y[n]), 3)
        
        print(coords.data['Distritos'][i], '->', coords.data['Distritos'][n])

print()
print(f"Total distance: {round(cost, 3)} long")
print(f"         in km: ~{round(cost*110.574, 3)} km")

while True:
    clock.tick(60)

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



    pygame.display.update()
