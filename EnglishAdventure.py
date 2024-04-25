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
        background_image = (pygame.image.load("imagens/cenario1.jpg").convert())
        screen.blit(background_image, (0, 0))

        # Desenha o título do jogo
        title_text = font.render("English Adventure", True, WHITE)
        title_rect = title_text.get_rect(
            center=(SCREEN_WIDTH // 2, 150))  # Centralizando e posicionando na parte superior
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
        if self.start_button.is_clicked(pos):
            self.nickname = self.nickname.strip()  # Remove espaços em branco do início e do fim
            nickname = self.nickname  # Salva o nome na variável nickname


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

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLACK)  # Preenche a tela com preto
        title_text = font.render("FASE 1", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(title_text, title_rect)

        title_text2 = font2.render("Press SPACE to continue...", True, WHITE)
        title_rect2 = title_text2.get_rect(center=(SCREEN_WIDTH // 2, 550))
        screen.blit(title_text2, title_rect2)


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

    def update(self):
        pass

    def draw(self, screen):
        cenario2 = (pygame.image.load("imagens/castelodentro.jpg").convert())
        screen.blit(cenario2, (0, 0))


def main():
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
                        current_screen = cenario2

        # Atualiza e desenha a tela atual
        screen.fill(BLACK)  # Preenche a tela com preto
        current_screen.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
