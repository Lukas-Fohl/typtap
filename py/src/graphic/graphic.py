from util import util as util
import pygame

def init():
    (width, height) = (600, 600)
    screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
    pygame.display.set_caption('...')
    screen.fill((0,0,0))
    pygame.display.flip()
    #create window
    return screen

def update(screen,file:util.file)->bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    displayFile(screen,file)
    return True

def displayFile(screen,file:util.file)->None:

    lineSpacing = 28
    topoffset = 20
    sideoffset = 20

    screen.fill((255,255,255))
    pygame.font.init()
    displayFont_hel = pygame.font.Font("./util/font/helvetica/Helvetica.ttf",20)

    for i in range(len(file.lines)):
        currentLine = ""
        for x in file.lines[i].lineParts:
            currentLine += x.linePartContent
        text_helvectica = displayFont_hel.render(currentLine, False, (0,0,0))
        screen.blit(text_helvectica, (sideoffset, i*lineSpacing + topoffset))
        pass


    #displayFont_times = pygame.font.Font("./util/font/timesNewRoman/times new roman.ttf",32)

    #text_times = displayFont_times.render('nice text in times new roman', False, (255, 255, 255))

    #x_times = ((pygame.display.get_window_size()[0])/2)-(text_times.get_size()[0]/2)
    #y_times = ((pygame.display.get_window_size()[1])/2)+(text_times.get_size()[1]/2)

    #screen.blit(text_times, (x_times, y_times))
    pygame.display.flip()
    return