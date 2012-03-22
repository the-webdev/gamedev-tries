import utils
class TileSet:
      def __init__(self, image, colorkey, tileWidth, tileHeight):
          self.__image = utils.loadImage()
          self.__tileWidth = tileWidth
          self.__tileHeight = tileHeight
          
          self.__tileTypes = dict()
      def getImage(self):
          return self.__image
      def setImage(file, colorkey):
          self.__image = utils.loadImage(file, colorkey)
      def getTileWidth(self):
          return self.__tileWidth
      def getTileHeight(self):
          return self.__tileHeight
      def getTileSize(self):
          return (self.__tileWidth, self.__tileWidth)
      