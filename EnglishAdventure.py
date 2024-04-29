import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("English Adventure")

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Definindo a fonte
font = pygame.font.Font(None, 48)  # Aumentando o tamanho da fonte do nome do jogo
font2 = pygame.font.Font(None, 40)
nickname_font = pygame.font.Font(None, 24)  # Aumentando um pouco a fonte do Nickname

# Definindo a variável global player_name
player_name = ''


class BaseScreen:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass


class MainMenuScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        # Criando os botões
        self.start_button = Button(SCREEN_WIDTH // 2 - 100, 400, 200, 50, "START")
        self.credits_button = Button(SCREEN_WIDTH // 2 - 100, 470, 200, 50, "Credits")
        # Criando o campo de entrada para o nickname
        self.nickname_input = pygame.Rect(SCREEN_WIDTH // 2 - 100, 270, 200, 30)
        self.nickname = ''

    def update(self):
        pass

    def draw(self, screen):
        # Desenha o cenário inicial
        background_image = pygame.image.load("imagens/cenario1.jpg").convert()
        screen.blit(background_image, (0, 0))

        # Desenha o título do jogo
        title_text = font.render("English Adventure", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 150))  # Centralizando e posicionando na parte superior
        screen.blit(title_text, title_rect)

        # Desenha os botões
        self.start_button.draw(screen)
        self.credits_button.draw(screen)

        # Desenha o campo de entrada para o nickname
        nickname_text = nickname_font.render("Nickname:", True, WHITE)
        screen.blit(nickname_text, (SCREEN_WIDTH // 2 - 100, 250))
        pygame.draw.rect(screen, WHITE, self.nickname_input, 2)  # Desenhando o retângulo de entrada do nickname

        # Renderiza dinamicamente o nome do usuário no retângulo de entrada de texto
        nickname_input_text = nickname_font.render(self.nickname, True, WHITE)
        screen.blit(nickname_input_text, (SCREEN_WIDTH // 2 - 90, 275))

    # Dentro do loop principal (while running), no bloco de eventos KEYDOWN
    # Verifica se o evento de tecla é um caractere imprimível e se o cursor está no retângulo de entrada de texto
    def handle_keydown_event(self, event):
        if event.unicode.isprintable() and self.nickname_input.collidepoint(pygame.mouse.get_pos()):
            self.nickname += event.unicode
        elif event.key == pygame.K_BACKSPACE:
            self.nickname = self.nickname[:-1]  # Remove o último caractere do nome, se houver algum

    # Dentro do bloco de eventos MOUSEBUTTONDOWN, após a verificação para o botão "START" ser clicado
    # Adiciona a linha para salvar o nome atual do usuário na variável nickname
    def handle_mouse_button_down_event(self, pos):
        global player_name
        if self.start_button.is_clicked(pos):
            self.nickname = self.nickname.strip()  # Remove espaços em branco do início e do fim
            player_name = self.nickname  # Salva o nome na variável player_name


class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.text = text
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class Phase1Screen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.text_index = 0  # Índice do texto atual
        self.texts = [
            ("FASE 1", "Press SPACE to continue..."),
            (f'{player_name}, é um(a) jovem determinado(a) e com um grande espírito aventureiro',
             f'que nasceu em uma cidade pequena no interior do São Paulo, ',
             f'ele(a) tinha o sonho de viajar pelo mundo e conhecer novas culturas.',
             f'Em um certo dia, {player_name} acaba se inscrevendo em um concurso',
             f'que daria como prêmio uma longa viagem pelos países., ',
             f'Para a surpresa de todos e de si próprio(a),',
             f'{player_name} acaba ganhando e então embarca na maior aventura de sua vida.',
             f'Mas espera aí...  {player_name} não sabe inglês, ',
             f'então essa viagem também será uma grande aprendizagem.')
        ]

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLACK)  # Preenche a tela com preto

        if self.text_index == 0:  # Se for o primeiro texto
            text1 = font.render(self.texts[self.text_index][0], True, WHITE)
            text1_rect = text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text1, text1_rect)

            text2 = font2.render(self.texts[self.text_index][1], True, WHITE)
            text2_rect = text2.get_rect(center=(SCREEN_WIDTH // 2, 550))
            screen.blit(text2, text2_rect)
        elif self.text_index == 1:
            y = 50
            for texto in self.texts[self.text_index]:
                text3 = font.render(texto, True, WHITE)
                text3_rect = text3.get_rect(center=(SCREEN_WIDTH // 2, y))
                screen.blit(text3, text3_rect)
                y += 50

    def change_text(self):
        self.text_index = (self.text_index + 1) % len(self.texts)  # Avança para o próximo texto


class CreditsScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        # Criando os botões
        self.voltar_button = Button(1, 1, 200, 50, "Return")

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLACK)  # Preenche a tela com preto
        text = ["Jeann Garçoni Alves", "Jhenifer Gonçalves Januário", "João Pedro de Oliveira Peres",
                "João Vitor Gaiato", "Kauan Omura Lopes", "Tamires Ledo da Silva Alves"]
        y = 100
        for name in text:
            name_text = font.render(name, True, WHITE)
            name_rect = name_text.get_rect(center=(SCREEN_WIDTH // 2, y))
            screen.blit(name_text, name_rect)
            y += 100

        self.voltar_button.draw(screen)


class Cenario2(BaseScreen):
    def __init__(self):
        super().__init__()
        self.text_index = 0  # Índice do texto atual
        self.texts = [
            ("O seu primeiro destino será Londres, Inglaterra.",
             "Lá você vai conhecer vários monumentos turísticos. ",
             "E aprender muito com personagens locais históricos!"),
            ('Bem-vindo a Londres, capital da Inglaterra e do Reino Unido,',
             'é uma cidade do século 21 com uma história que remonta à era romana.',
             'Seu centro abriga as sedes imponentes do Parlamento ',
             'e a famosa torre do relógio do Big Ben.'),
            (f'Parabéns, você recebeu o convite para um tour pelo palacio real',
             'acompanhado(a) pessoalmente pela própria Rainha,',
             'essa é uma oportunidade muito especial e única!'),
            ('Welcome to the Buckingham Palace! I am Queen Elizabeth,',
             'e estou aqui para ensinar-lhes várias importantes em inglês.',
             "Let's start with the greetings, as saudações, ",
             "que são essenciais para qualquer conversa educada. ",
             "'Hello' significa 'Olá'. Temos também 'Good morning' para desejar um bom dia.",
             "And 'Good afternoon' para dizer boa tarde. Very good!!!Muito bem!!!"),
            ('Agora, para um rápido desafio, vou fazer algumas perguntas simples,',
             'vamos ver se você se lembra:')
        ]
        self.text_surface = None

    def update(self):
        pass

    def draw(self, screen):
        cenario2 = pygame.image.load("imagens/castelodentro.jpg").convert()
        screen.blit(cenario2, (0, 0))
        text_width = max(len(text) for text in self.texts[self.text_index]) * 20
        text_height = len(self.texts[self.text_index]) * 30
        self.text_surface = pygame.Surface((text_width, text_height)).convert_alpha()
        self.text_surface.fill((30, 30, 30, 150))  # Cor do retângulo com transparência

        # Desenha os textos sobre a superfície
        y = 17
        for texto in self.texts[self.text_index]:
            text = font2.render(texto, True, WHITE)
            text_rect = text.get_rect(center=(text_width // 2, y))
            self.text_surface.blit(text, text_rect)
            y += 30

        # Desenha a superfície sobre a tela principal
        screen.blit(self.text_surface, (SCREEN_WIDTH // 2 - text_width // 2, SCREEN_HEIGHT // 2 - text_height // 2))

    def change_text(self):
        self.text_index = (self.text_index + 1) % len(self.texts)  # Avança para o próximo texto


def main():
    global player_name
    # Criando as telas do jogo
    main_menu_screen = MainMenuScreen()
    phase1_screen = Phase1Screen()
    credits_screen = CreditsScreen()
    cenario2 = Cenario2()
    current_screen = main_menu_screen  # Define a tela inicial como a tela atual

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_screen == main_menu_screen:  # Verifica se está na tela inicial
                    if main_menu_screen.start_button.is_clicked(pygame.mouse.get_pos()):
                        # Transição para a tela da fase 1 ao clicar em "Iniciar Jogo"
                        main_menu_screen.handle_mouse_button_down_event(pygame.mouse.get_pos())
                        current_screen = phase1_screen
                    elif main_menu_screen.credits_button.is_clicked(pygame.mouse.get_pos()):
                        # Transição para a tela de créditos ao clicar em "Créditos"
                        current_screen = credits_screen
                if current_screen == credits_screen:
                    if credits_screen.voltar_button.is_clicked(pygame.mouse.get_pos()):
                        current_screen = main_menu_screen

            elif event.type == pygame.KEYDOWN:
                main_menu_screen.handle_keydown_event(event)  # Chama o método para lidar com eventos KEYDOWN

                if current_screen == phase1_screen:
                    if event.key == pygame.K_SPACE:
                        phase1_screen.change_text()

                if current_screen == phase1_screen:
                    if event.key == pygame.K_c:
                        current_screen = cenario2

                if current_screen == cenario2:
                    if event.key == pygame.K_SPACE:
                        cenario2.change_text()

        # Atualiza e desenha a tela atual
        screen.fill(BLACK)  # Preenche a tela com preto
        current_screen.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
