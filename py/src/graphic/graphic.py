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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False

    displayFile(screen,file)
    return True

class printAble:
    textLinePart:util.linePart
    position=[]
    def __init__(self,LinePart,position_) -> None:
        self.position = position_
        self.textLinePart = LinePart
        pass

def displayFile(screen,file:util.file)->None:

    lineSpacing = 28
    topoffset = 20
    sideoffset = 20

    screen.fill((255,255,255))
    pygame.font.init()
    displayFont_hel = pygame.font.Font("./util/font/helvetica/Helvetica.ttf",20)
    displayFont_hel_ital = pygame.font.Font("./util/font/helvetica/Helvetica-Oblique.ttf",20)
    displayFont_hel_bold = pygame.font.Font("./util/font/helvetica/Helvetica-Bold.ttf",20)
    displayFont_hel_Header = pygame.font.Font("./util/font/helvetica/Helvetica-Bold.ttf",26)

    for i in range(len(file.lines)):
        currentLine = []
        lineLen = 0
        for j in range(len(file.lines[i].lineParts)):
            x = sideoffset + lineLen * (12);
            y = i*lineSpacing + topoffset;
            p_ = printAble(file.lines[i].lineParts[j],(x,y))
            lineLen += len(file.lines[i].lineParts[j].linePartContent)
            currentLine.append(p_)
        for a in currentLine:
            if(a.textLinePart.linePartType == util.contentType.bold):
                text_helvectica = displayFont_hel_bold.render(a.textLinePart.linePartContent, True, (0,0,0))
            elif(a.textLinePart.linePartType == util.contentType.tab):
                a.textLinePart.linePartContent = "    "
                text_helvectica = displayFont_hel.render(a.textLinePart.linePartContent, True, (0,0,0))
            elif(a.textLinePart.linePartType == util.contentType.header):
                text_helvectica = displayFont_hel_Header.render(a.textLinePart.linePartContent, True, (0,0,0))
            elif(a.textLinePart.linePartType == util.contentType.italic):
                text_helvectica = displayFont_hel_ital.render(a.textLinePart.linePartContent, True, (0,0,0))
            elif(a.textLinePart.linePartType == util.contentType.bulletpoint):
                a.textLinePart.linePartContent = "•"
                text_helvectica = displayFont_hel.render(a.textLinePart.linePartContent, True, (0,0,0))
            elif(a.textLinePart.linePartType == util.contentType.pi):
                a.textLinePart.linePartContent = "π"
                text_helvectica = displayFont_hel.render(a.textLinePart.linePartContent, True, (0,0,0))
            else:
                text_helvectica = displayFont_hel.render(a.textLinePart.linePartContent, True, (0,0,0))
            screen.blit(text_helvectica, (a.position[0],a.position[1]))
    pygame.display.flip()
    return