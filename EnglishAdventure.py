import pygame
from sys import exit


def sair():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def nome():
    global nome_texto
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                nome1 = ''.join(nome_texto)
                return nome1  # Retorna o nome digitado
            elif event.key == pygame.K_BACKSPACE:
                if len(nome_texto) > 0:
                    nome_texto.pop()
            else:
                nome_texto.append(event.unicode)


def render_nome_texto():
    nome_jogador = fonte2.render('Nick name: ' + ''.join(nome_texto), False, 'Black')
    nome_jogador_retangulo = nome_jogador.get_rect(center=(400, 150))
    tela.blit(nome_jogador, nome_jogador_retangulo)


def render_texto(t):
    y = 100
    for linha in t:
        texto = fonte2.render(linha, False, 'Black')
        texto_retangulo = texto.get_rect(center=(625, y))
        tela.blit(texto, texto_retangulo)
        y += 50


pygame.init()
tela = pygame.display.set_mode((1250, 625))
pygame.display.set_caption(' EnglishAdventure ')
clock = pygame.time.Clock()
fonte1 = pygame.font.SysFont('Ariel', 50, False)
fonte2 = pygame.font.SysFont('Ariel', 30)
nome_texto = []
nome_usuario = None

intro_texto = [f'{nome_usuario}, é um(a) jovem determinado(a) e com um grande espírito ',
               'aventureiro que nasceu em uma cidade pequena no interior do São Paulo, ',
               'ele(a) tinha o sonho de viajar pelo mundo e conhecer novas culturas.',
               f'Em um certo dia, {nome_usuario} acaba se '
               f'inscrevendo em um concurso que daria como prêmio',
               'uma longa viagem pelos países. ',
               'Para a surpresa de todos e de si próprio(a), ',
               f'{nome_usuario} acaba ganhando e então embarca na maior aventura de sua vida.',
               f'Mas espera aí...  {nome_usuario} não sabe inglês, ',
               f'então essa viagem também será uma grande aprendizagem.']

cena_1 = pygame.image.load('cenario1.jpg').convert_alpha()
cena_2 = pygame.image.load('castelodentro.jpg').convert_alpha()

nome_jogo = fonte1.render('English Adventure', False, 'Black')
nome_jogo_retangulo = nome_jogo.get_rect(center=(625, 90))

while True:
    tela.blit(cena_1, (0, 0))
    tela.blit(nome_jogo, nome_jogo_retangulo)
    if nome_usuario is None:
        nome_usuario = nome()
    render_nome_texto()
    if nome_usuario:
        tela.fill((255, 255, 255))
        render_texto(intro_texto)
    sair()
    pygame.display.update()
    clock.tick(60)
