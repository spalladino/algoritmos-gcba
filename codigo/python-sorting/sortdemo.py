import pygame
import random

import sortalgorithm
import threading

class SortDemo:

    Margin = 20
    TitleHeight = 40
    
    Colors = {
        'normal': (pygame.Color(0xAA,0xAA,0xAA), pygame.Color(0x88,0x88,0x88)),
        'write':  (pygame.Color(0xFF,0x88,0x88), pygame.Color(0xAA,0x44,0x44)),
        'cmp':    (pygame.Color(0x88,0x88,0xFF), pygame.Color(0x44,0x44,0xFF)),
        'active': (pygame.Color(0x99,0x99,0x99), pygame.Color(0x88,0x88,0x88)),
        'success':(pygame.Color(0xAA,0xCC,0xAA), pygame.Color(0x88,0xBB,0x88)),
        'fail':   (pygame.Color(0xFF,0x44,0x44), pygame.Color(0xFF,0x88,0x88)),
    }
    
    
    # Dibuja un arreglo con determinados estados
    def draw_array(self, runner, index=0):
        # Calculamos left offset y dimensiones
        array = runner.array
        left = self.Margin + index * (self.Margin + self.array_width)
        top = self.TitleHeight + self.Margin
        max_value = max(array)
        height = self.array_height / len(array)
        width = self.array_width / max_value

        # Dibujamos el titulo
        font = pygame.font.Font(None, 36)
        text = font.render(runner.name, 1, (0x00, 0x00, 0x00))
        textpos = text.get_rect()
        textpos.centerx = left + self.array_width / 2
        textpos.top = 10
        self.screen.blit(text, textpos)
        
        # Dibujamos el estado
        font = pygame.font.Font(None, 16)
        status = "Comparaciones = %5d | Asignaciones = %5d" % (runner.comparisons, runner.assignments)
        text = font.render(status, 1, (0x00, 0x00, 0x00))
        textpos = text.get_rect()
        textpos.centerx = left + self.array_width / 2
        textpos.top = 40
        self.screen.blit(text, textpos)
        
        # Armamos las coordenadas de los rectangulos para la pantalla, sin dibujarlos aun
        screen_array = [ pygame.Rect(left, top + index*height, value * width, height) for index, value in enumerate(array) ]
        
        # Dibujamos el margen
        pygame.draw.rect(self.screen, pygame.Color(0xCC,0xCC,0xCC), [left, top, self.array_width, self.array_height], 1)
        
        # Dibujamos el arreglo en si
        for rect, status in zip(screen_array, runner.statuses):
            self.draw_item(rect, status)
        
	# Dibujamos un item con determinado color
    def draw_item(self, rect, color_set='normal'):
        fill, border = self.Colors[color_set]
        pygame.draw.rect(self.screen, fill, rect)
        pygame.draw.rect(self.screen, border, rect, 1)


    def __init__(self, runs, **kwargs):
        self.fps = kwargs.get('fps') or 20
        self.array_width = kwargs.get('ancho') or 280
        self.array_height = kwargs.get('alto') or 500

        self.event = threading.Event()
        self.runners = [sortalgorithm.SortAlgorithm(algorithm, list(array), self.event, name) for (algorithm, name, array) in runs]
        
        pygame.init()
        
        # Setup de la pantalla
        self.screen = pygame.display.set_mode([self.Margin + (self.array_width + self.Margin) * len(self.runners), self.TitleHeight + self.array_height + self.Margin * 2])
        pygame.display.set_caption("Sorting Algorithms Demo")
        clock = pygame.time.Clock()
        self.screen.fill(pygame.Color("white"))        
        
        # Dibujamos los arreglos            
        for index, runner in enumerate(self.runners):
            self.draw_array(runner, index)
        
        # Arrancamos los algoritmos
        for runner in self.runners:
            runner.start()
        
        # Main loop: ejecutamos mientras el usuario no elija salir
        finished = False
        while not finished:
            
            # Levantamos el input del usuario
            for event in pygame.event.get(): 
                # Si eligio salir, cortamos cuando termine esta iteracion del loop
                if event.type == pygame.QUIT:
                    finished = True

            # Le damos tiempo a los algoritmos para que ejecuten
            for runner in self.runners:
                runner.wait_for_execute_iteration()

            # Limpiamos la pantalla
            self.screen.fill(pygame.Color("white"))        

            # Dibujamos los arreglos            
            for index, runner in enumerate(self.runners):
                self.draw_array(runner, index)
            
            # Redibujamos
            clock.tick(self.fps)
            pygame.display.update()

            # Los despertamos
            self.event.set()
        
        pygame.quit()
        
