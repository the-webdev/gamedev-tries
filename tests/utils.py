def loadImage(filename, colorkey = None):
    image = pygame.image.load(filename)

    if image.get_alpha() == None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))

        image.set_colorkey(colorkey, RLEACCEL)

    return image