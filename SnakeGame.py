import pygame
import time
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 600

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Configurações do jogo
tamanho_bloco = 20
velocidade = 15

# Inicialização da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobra")

# Controle de tempo
relogio = pygame.time.Clock()

# Fontes
fonte = pygame.font.SysFont(None, 35)
fonte_pontuacao = pygame.font.SysFont(None, 25)

# Função para exibir pontuação
def sua_pontuacao(pontos):
    texto = fonte_pontuacao.render(f"Pontos: {pontos}", True, verde)
    tela.blit(texto, [10, 10])

# Função para desenhar a cobra
def cobra(tamanho_cobra, lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

# Função para exibir mensagem
def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])

# Função principal do jogo
def jogo():
    fim_jogo = False
    game_over = False

    x1 = largura / 2
    y1 = altura / 2
    x1_mudanca = 0
    y1_mudanca = 0

    lista_cobra = []
    tamanho_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    while not fim_jogo:
        while game_over:
            tela.fill(preto)
            mensagem("Você perdeu! Aperte Q para sair ou C para continuar.", vermelho)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x1_mudanca == 0:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT and x1_mudanca == 0:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP and y1_mudanca == 0:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN and y1_mudanca == 0:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        # Verifica se a cobra bateu nas bordas
        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            game_over = True

        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(preto)

        # Desenhar a comida
        pygame.draw.rect(tela, azul, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        # Atualizar o corpo da cobra
        cabeca_cobra = [x1, y1]
        lista_cobra.append(cabeca_cobra)

        if len(lista_cobra) > tamanho_cobra:
            del lista_cobra[0]

        # Verificar colisão com o próprio corpo
        for bloco in lista_cobra[:-1]:
            if bloco == cabeca_cobra:
                game_over = True

        cobra(tamanho_bloco, lista_cobra)
        sua_pontuacao(tamanho_cobra - 1)
        pygame.display.update()

        # Verificar se a cobra comeu a comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            tamanho_cobra += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

jogo()
