import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
gamewindow = pygame.display.set_mode((300, 300))
gamewindow.fill(white)
pygame.display.set_caption('Tic Tac Toe')
pygame.draw.line(gamewindow, black, [100, 0], [100, 300], 1)
pygame.draw.line(gamewindow, black, [200, 0], [200, 300], 1)
pygame.draw.line(gamewindow, black, [0, 100], [300, 100], 1)
pygame.draw.line(gamewindow, black, [0, 200], [300, 200], 1)
pygame.display.update()
fon = pygame.font.SysFont(None, 40)
text = fon.render('a', True, (0, 0, 0), (255, 255, 255))
gamewindow.blit(text, [50, 50])
text = fon.render('b', True, (0, 0, 0), (255, 255, 255))
gamewindow.blit(text, [150, 50])
text = fon.render('c', True, (0, 0, 0), (255, 255, 255))
gamewindow.blit(text, [250, 50])
text = fon.render('d', True, (0, 0, 0), (255, 255, 255))
gamewindow.blit(text, [50, 150])
text = fon.render('e', True, (0, 0, 0), (255, 255, 255))
gamewindow.blit(text, [150, 150])
text = fon.render('f', True, (0, 0, 0), (255, 255, 255))
gamewindow.blit(text, [250, 150])
text = fon.render('g', True, (0, 0, 0), (255, 255, 255))
gamewindow.blit(text, [50, 250])
text = fon.render('h', True, (0, 0, 0), (255, 255, 255))
gamewindow.blit(text, [150, 250])
text = fon.render('i', True, (0, 0, 0), (255, 255, 255))
gamewindow.blit(text, [250, 250])
pygame.display.update()
player1 = []
player2 = []
win1 = ['a', 'e', 'i']
win2 = ['c', 'e', 'g']
win3 = ['a', 'd', 'g']
win4 = ['a', 'b', 'c']
win5 = ['c', 'f', 'i']
win6 = ['g', 'h', 'i']
win7 = ['b', 'e', 'h']
win8 = ['d', 'e', 'f']

def winner():
    check1p1=all(item in player1 for item in win1)
    if check1p1 is True:
        text = fon.render('Player 2 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check2p1=all(item in player1 for item in win2)
    if check2p1 is True:
        text = fon.render('Player 2 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check3p1=all(item in player1 for item in win3)
    if check3p1 is True:
        text = fon.render('Player 2 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check4p1=all(item in player1 for item in win4)
    if check4p1 is True:
        text = fon.render('Player 2 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check5p1=all(item in player1 for item in win5)
    if check5p1 is True:
        text = fon.render('Player 2 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check6p1=all(item in player1 for item in win6)
    if check6p1 is True:
        text = fon.render('Player 2 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check7p1=all(item in player1 for item in win7)
    if check7p1 is True:
        text = fon.render('Player 2 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check8p1 = all(item in player1 for item in win8)
    if check8p1 is True:
        text = fon.render('Player 2 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check1p2 = all(item in player2 for item in win1)
    if check1p2 is True:
        text = fon.render('Player 1 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check2p2 = all(item in player2 for item in win2)
    if check2p2 is True:
        text = fon.render('Player 1 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check3p2 = all(item in player2 for item in win3)
    if check3p2 is True:
        text = fon.render('Player 1 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check4p2 = all(item in player2 for item in win4)
    if check4p2 is True:
        text = fon.render('Player 1 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check5p2 = all(item in player2 for item in win5)
    if check5p2 is True:
        text = fon.render('Player 1 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check6p2 = all(item in player2 for item in win6)
    if check6p2 is True:
        text = fon.render('Player 1 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check7p2 = all(item in player2 for item in win7)
    if check7p2 is True:
        text = fon.render('Player 1 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])
    check8p2 = all(item in player2 for item in win8)
    if check8p2 is True:
        text = fon.render('Player 1 WON', True, (255, 0, 0), (255, 255, 255))
        gamewindow.blit(text, [50, 150])

def loop():
    gameclose = False

    for count in range(1, 11):
        while not gameclose:
            winner()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or count == 10:
                    gameclose = True
                if count % 2 == 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            pygame.draw.rect(gamewindow, black, [30, 30, 30, 30])
                            pygame.display.update()
                            player1.append('a')
                            count = count + 1
                            break
                        elif event.key == pygame.K_b:
                            pygame.draw.rect(gamewindow, black, [130, 30, 30, 30])
                            pygame.display.update()
                            player1.append('b')
                            count = count + 1
                            break
                        elif event.key == pygame.K_c:
                            pygame.draw.rect(gamewindow, black, [230, 30, 30, 30])
                            pygame.display.update()
                            player1.append('c')
                            count = count + 1
                            break
                        elif event.key == pygame.K_d:
                            pygame.draw.rect(gamewindow, black, [30, 130, 30, 30])
                            pygame.display.update()
                            player1.append('d')
                            count = count + 1
                            break
                        elif event.key == pygame.K_e:
                            pygame.draw.rect(gamewindow, black, [130, 130, 30, 30])
                            pygame.display.update()
                            player1.append('e')
                            count = count + 1
                            break
                        elif event.key == pygame.K_f:
                            pygame.draw.rect(gamewindow, black, [230, 130, 30, 30])
                            pygame.display.update()
                            player1.append('f')
                            count = count + 1
                            break
                        elif event.key == pygame.K_g:
                            pygame.draw.rect(gamewindow, black, [30, 230, 30, 30])
                            pygame.display.update()
                            player1.append('g')
                            count = count + 1
                            break
                        elif event.key == pygame.K_h:
                            pygame.draw.rect(gamewindow, black, [130, 230, 30, 30])
                            pygame.display.update()
                            player1.append('h')
                            count = count + 1
                            break
                        elif event.key == pygame.K_i:
                            pygame.draw.rect(gamewindow, black, [230, 230, 30, 30])
                            pygame.display.update()
                            player1.append('i')
                            count = count + 1
                            break
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            pygame.draw.rect(gamewindow, blue, [30, 30, 30, 30])
                            pygame.display.update()
                            player2.append('a')
                            count = count + 1
                            break
                        elif event.key == pygame.K_b:
                            pygame.draw.rect(gamewindow, blue, [130, 30, 30, 30])
                            pygame.display.update()
                            player2.append('b')
                            count = count + 1
                            break
                        elif event.key == pygame.K_c:
                            pygame.draw.rect(gamewindow, blue, [230, 30, 30, 30])
                            pygame.display.update()
                            player2.append('c')
                            count = count + 1
                            break
                        elif event.key == pygame.K_d:
                            pygame.draw.rect(gamewindow, blue, [30, 130, 30, 30])
                            pygame.display.update()
                            player2.append('d')
                            count = count + 1
                            break
                        elif event.key == pygame.K_e:
                            pygame.draw.rect(gamewindow, blue, [130, 130, 30, 30])
                            pygame.display.update()
                            player2.append('e')
                            count = count + 1
                            break
                        elif event.key == pygame.K_f:
                            pygame.draw.rect(gamewindow, blue, [230, 130, 30, 30])
                            pygame.display.update()
                            player2.append('f')
                            count = count + 1
                            break
                        elif event.key == pygame.K_g:
                            pygame.draw.rect(gamewindow, blue, [30, 230, 30, 30])
                            pygame.display.update()
                            player2.append('g')
                            count = count + 1
                            break
                        elif event.key == pygame.K_h:
                            pygame.draw.rect(gamewindow, blue, [130, 230, 30, 30])
                            pygame.display.update()
                            player2.append('h')
                            count = count + 1
                            break
                        elif event.key == pygame.K_i:
                            pygame.draw.rect(gamewindow, blue, [230, 230, 30, 30])
                            pygame.display.update()
                            player2.append('i')
                            count = count + 1
                            break
    pygame.display.update()
    pygame.quit()
    quit()
loop()