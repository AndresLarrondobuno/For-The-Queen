import pygame

class SpriteParaAventurero(pygame.sprite.Sprite):
    def __init__(self, imagen, coordenadas_de_dibujo=(0,0)):
        super().__init__()
        self.image = imagen
        self.rect = imagen.get_rect()
        self.coordenadas_de_dibujo = coordenadas_de_dibujo
        self.rect.x = coordenadas_de_dibujo[0]
        self.rect.y = coordenadas_de_dibujo[1]
    

    def update(self):
        pass



class SpriteParaCasilla(pygame.sprite.Sprite):
    def __init__(self, casilla):
        super().__init__()
        self.origen_de_dibujo = casilla.origen_de_dibujo
        self.image = casilla.imagen
        self.rect = casilla.rect
        self.rect.x = casilla.origen_de_dibujo[0]
        self.rect.y = casilla.origen_de_dibujo[1]



class SpriteParaResaltador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = None
        self.image= None
    
    
    def update(self, superficie, casilla):
        pygame.draw.rect(superficie, "Green", casilla.rect, 1)
        
    

    
class SpriteParaBoton(pygame.sprite.Sprite):
    def __init__(self, imagen, coordenadas_de_dibujo=(0, 0)):
        super().__init__(imagen, coordenadas_de_dibujo)
        

        




'''
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Create a rect sprite and add it to a sprite group
spritesDeResaltado = pygame.sprite.Group()

imagen_herrero = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dc-mon\holy\paladin.png")), (120,120))
imagen_erudito = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dc-mon\wizard.png")), (120,120))


sprite_herrero = SpriteCustom(imagen_herrero, (0,0))
sprite_erudito = SpriteCustom(imagen_erudito, (50,50))

superficie_para_resaltador = pygame.Surface((100, 50))
sprite_para_resaltador = SpriteParaResaltador(superficie_para_resaltador)

sprites = [sprite_herrero, sprite_erudito]
grupo_aventureros = pygame.sprite.Group(sprites)
grupo_resaltador = pygame.sprite.Group()

running = True
while running:
    posicion_mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the rect
    grupo_aventureros.draw(screen)

    # Remove the rect from the sprite group and display surface
    if event.type == pygame.MOUSEBUTTONDOWN and sprite_herrero.rect.collidepoint(posicion_mouse):
        sprites.remove(sprite_herrero)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
'''