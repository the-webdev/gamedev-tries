# encoding: UTF-8
class TileObject:
      def __init__(self, name, startX, startY, widh, height):
          self.__name = name
          self.__rect = pygame.rect.Rect(startX, startY, width, height)
      def getName():
          return self.__name
      def getRect():
          return self.__rect