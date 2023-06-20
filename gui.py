import pygame

from jogo_da_velha import criarBoard, fazMovimento,  getInputValido, \
                            printBoard, verificaGanhador,  verificaMovimento

from minimax import movimentoIA

pygame.font.init()
font = pygame.font.SysFont("comicsans", 40)
text = font.render("Restart", True, (0, 0, 0))
textPoweredBy = font.render("Powered By Hamoa Tech", True, (0, 0, 0))
button_width = text.get_width() + 20
button_height = text.get_height() + 10
button_x = (600 - button_width) // 2
button_y = 650

def draw_board(win, board):
    height = 600
    width = 600
    tamanho = 600/3

    for i in range(1, 3):
        pygame.draw.line(win, (0, 0 ,0), (0, i *  tamanho), (width, i * tamanho), 3)
        pygame.draw.line(win, (0, 0 ,0), (i * tamanho, 0), (i * tamanho, height), 3)

    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont("comicsans", 100)

            x = j * tamanho
            y = i * tamanho

            text = font.render(board[i][j], 1, (128, 0, 0))
            win.blit(text, ((x + 75), (y + 75)))

def draw_button(win):
    pygame.draw.rect(win, (192, 192, 192), (button_x, button_y, button_width, button_height))
    pygame.draw.rect(win, (0, 0, 0), (button_x, button_y, button_width, button_height), 3)
    win.blit(text, (button_x + 10, button_y + 5))
    win.blit(textPoweredBy, (button_x - 140, button_y + 70))

def redraw_window(win, board):
    win.fill((255, 255, 255))
    draw_board(win, board)
    draw_button(win)

def restart_game():
    main()

def main():
    win = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Jogo Da Velha")

    board = criarBoard()

    redraw_window(win, board)
    pygame.display.update()

    jogador = 0
    ganhador = verificaGanhador(board)
    
    while(not ganhador):
        printBoard(board)
        if(jogador == 0):
            jogou = False
            while(not jogou):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        button_x = (600 - button_width) // 2
                        button_y = 650
                        print('chamou aqui')
                        if button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height:
                            return restart_game()
                    if(event.type == pygame.QUIT):
                        return
                    elif(event.type == pygame.MOUSEBUTTONUP):
                        pos = pygame.mouse.get_pos()
                        i = int(pos[1]/200)
                        j = int(pos[0]/200)
                        jogou = True
        else:
            i,j = movimentoIA(board, jogador)
        
        if(verificaMovimento(board, i, j)):
            fazMovimento(board, i, j, jogador)
            jogador = (jogador + 1)%2
        
        ganhador = verificaGanhador(board)
        redraw_window(win, board)
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                button_x = (600 - button_width) // 2
                button_y = 650
                print('chamou aqui')
                if button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height:
                    restart_game()
            else:
                continue
            break

main()