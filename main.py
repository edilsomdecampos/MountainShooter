import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))  # Corrigi o nome da variável para 'window'
print("Setup End")

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Evento correto para fechar a janela
            pygame.quit()  # Fecha o Pygame
            quit()  # Finaliza o programa
    pygame.display.update()  # Atualiza a tela a cada loop
