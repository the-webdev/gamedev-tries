import pygame
def get_tmap():
    map = [
    [0,1,2,2,1,1,2,1,1,1,0,0,2,1,2,0],
    [0,1,2,2,1,1,2,0,0,1,0,0,2,2,2,0],
    [0,1,2,2,1,1,2,0,0,1,0,0,2,1,2,0],
    [0,1,2,2,1,1,2,1,1,1,0,0,2,1,2,0],
    [0,1,2,2,1,1,2,0,0,1,0,0,2,1,2,0]
    ]
    return map
def render_tmap(tmap):
    tilesize = 20
    map_x = len(tmap[0])
    map_y = len(tmap)
    map_surface = pygame.surface.Surface([map_x*tilesize, map_y*tilesize])
    for x in range(map_x):
        for y in range(map_y):
            tile = pygame.surface.Surface((tilesize,tilesize))
            if   tmap[y][x] == 0:
                          tile.fill((0,0,0))
            elif tmap[y][x] == 1:
                          tile.fill((255,0,0))
            elif tmap[y][x] == 2:
                            tile.fill((0,0,255))
            map_surface.blit(tile,(x*tilesize,y*tilesize))
    return map_surface
if __name__ == "__main__":
   clock = pygame.time.Clock()
   surf = render_tmap(get_tmap())
   running = True
   while(running):
               clock.tick(30)
               screen = pygame.display.set_mode((320,100))
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                      running = False
                   elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                        running = False
               screen.fill((0,0,0))
               screen.blit(surf,(0,0))
               pygame.display.flip()