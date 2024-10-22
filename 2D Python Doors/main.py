import pygame

pygame.init()

# Numéricas
screen_sizeX, screen_sizeY = (800, 600)
posX = screen_sizeX // 2 - 10 
graY = screen_sizeY // 2 - 10 
speed = 200  # Aumenta la velocidad para usar dt
# Fin de numéricas

# Booleanas
running = True
ifApressed = False
ifdpressed = False
# Fin de booleanas

# Colores
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
# Fin colores

# Pygame
Screen = pygame.display.set_mode((screen_sizeX, screen_sizeY))
clock = pygame.time.Clock()  # Crear el objeto Clock
# Fin pygame

# Bucle
while running:
    dt = clock.tick(60) / 1000.0  # Calcular dt en segundos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()  
    ifApressed = keys[pygame.K_a]
    ifdpressed = keys[pygame.K_d]
    
    if ifApressed:
        posX -= speed * dt  # Mover hacia la izquierda
    if ifdpressed:
        posX += speed * dt  # Mover hacia la derecha

    Screen.fill(white)  
    pygame.draw.rect(Screen, blue, (posX, graY, 20, 20))  
    pygame.display.flip() 
# Fin bucle

# Al final del bucle
pygame.quit()
# Fin de al final del bucle
