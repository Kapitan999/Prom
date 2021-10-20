import pygame
##import keyboard
import sys

size = width, height = 800, 800
color = 232, 227, 214
screen = pygame.display.set_mode(size)


class StaticSprite:
    def __init__(self, R, G, B, posX, posY, image):
       self.R = R
       self.G = G
       self.B = B
       self.posX = posX
       self.posY = posY
       self.image = image
    def draw(self):
       rect = self.image.get_rect()
     #color1 = self.R, self.G, self.B
       rect.x = self.posX
       rect.y = self.posY

       screen.blit(self.image, rect)



def main():
    pygame.init()
    gameover = False
    ImageBlock = pygame.image.load("block.jpg")
    ImagePl = pygame.image.load("sokoban.jpg")
    ImageFl = pygame.image.load("floor.png")
    test = ImageBlock.get_rect()
    print(test)

    # Построение карты
    #####################################################
    #####################################################
    #####################################################
    #####################################################
    x = 120
    y = 34
    map = []
    wall = StaticSprite(0, 0, 0, x, y, ImageFl)
    for i in range(12):
        y = y + 43
        wall = StaticSprite(0, 0, 0, x, y, ImageFl)
        map.append(wall)
    for i in range(12):
        x = x + 43
        wall = StaticSprite(0, 0, 0, x, y, ImageFl)
        map.append(wall)
    for i in range(12):
        y = y - 43
        wall = StaticSprite(0, 0, 0, x, y, ImageFl)
        map.append(wall)
    for i in range(12):
        x = x - 43
        wall = StaticSprite(0, 0, 0, x, y, ImageFl)
        map.append(wall)

    pygame.draw.rect(screen, (125, 149, 152), (163, 163, 473, 473), 0)
    #####################################################
    #####################################################
    #####################################################
    #####################################################
    playX = 200
    playY = 150
    player = StaticSprite(0, 0, 0, playX, playY, ImagePl)
    player.draw()

    blX = 250
    blY = 200
    block = StaticSprite(0, 0, 0, blX, blY, ImageBlock)
    block.draw()
    # Отрисовка
    while not gameover:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                gameover = True
        screen.fill(color)

        # Отрисовка карты
        pygame.draw.rect(screen, (125, 149, 152), (163, 77, 473, 473), 0)
        for i in range(len(map)):
            map[i].draw()
        for i in pygame.event.get():
            if(i.type == pygame.KEYDOWN):
                if(i.key == pygame.K_d):
                    playX += 43
        ################
        ##if (keyboard.is_pressed('d')):



        ##elif (keyboard.is_pressed('a')):
                elif (i.key == pygame.K_a):
                    playX -= 43

        ##elif (keyboard.is_pressed('w')):
                elif (i.key == pygame.K_w):
                    playY -= 43

        ##elif (keyboard.is_pressed('s')):
                elif (i.key == pygame.K_s):
                    playY += 43

        player = StaticSprite(0, 0, 0, playX, playY, ImagePl)
        player.draw()

        block = StaticSprite(0, 0, 0, blX, blY, ImageBlock)
        block.draw()
        if player.rect.coliderect(block.rect):
            print("YES")
        pygame.display.flip()
        pygame.time.wait(1)
    sys.exit()

if __name__ == '__main__':
    main()
