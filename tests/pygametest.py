import pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("TEXT-test")
clock = pygame.time.Clock()
done = False
font = pygame.font.Font(None,30)
text = font.render("Hello World!", True, [255,0,255])
while not done:
      for event in py0game.event.get():
          if event.type == pygame.QUIT:
             done = True
          if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
             done = True
      screen.fill([255,255,255])
      screen.blit(text, (320 - text.get_width()//2, 240 - text.get_height()//2))
      pygame.display.flip()
      clock.tick(60)
