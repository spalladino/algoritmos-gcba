import pygame

class Mapa:

    Height = 400
    Width = 400
    Margin = 20

    Colors = {
        'R': pygame.Color(0xFF,0x44,0x44),
        'G': pygame.Color(0x44,0xFF,0x44),
        'B': pygame.Color(0x44,0x44,0xFF),
        'X': pygame.Color(0x88,0x88,0x88)
    }

    def __init__(self, matrix):
        self.matrix = matrix
        self.validar()
        self.dibujar()
        self.main_loop()
       
    # Escucha input del usuario para cerrarse
    def main_loop(self):
        finished = False
        while not finished:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    finished = True
        pygame.quit()
        
    # Chequea que el mapa sea valido
    def validar(self):
        if len(self.matrix) == 0:
            raise Exception("El mapa debe tener al menos una fila")
        
        columnas = len(self.matrix[0])
        if columnas == 0:
            raise Exception("El mapa debe tener al menos una columna")
        
        for index, fila in enumerate(self.matrix):
            if len(fila) != columnas:
                raise Exception("La fila %s tiene %s elementos, se esperaban %s" % (index, len(fila), columnas))
        
        for i, fila in enumerate(self.matrix):
            for j, elem in enumerate(fila):
                if not elem in ['R','G','B','X']:
                    raise Exception('Valor no esperado: %s' % elem)
    
    # Dibuja el mapa inicialmente
    def dibujar(self):
        # Setup de la pantalla
        pygame.init()
        self.screen = pygame.display.set_mode([self.Height + self.Margin*2, self.Width + self.Margin*2])
        pygame.display.set_caption("Lectura archivo mapa")
        self.screen.fill(pygame.Color("white"))        
        clock = pygame.time.Clock()
        
        # Armamos medidas
        matrix = self.matrix            
        height = self.Height / len(matrix)
        width =  self.Width / len(matrix[0])
        
        # Dibujamos el mapa
        pygame.display.update()
        for i, fila in enumerate(matrix):
            for j, elem in enumerate(fila):
                pygame.draw.rect(self.screen, self.Colors[elem], [self.Margin + j * width, self.Margin + i * height, width, height])
                clock.tick(10)
                pygame.display.update()            

# Muestra un ejemplo por pantalla si se lo invoca directamente                
if __name__ == '__main__':            
    Mapa([['R', 'G', 'B'], ["G", 'B', 'R']])
