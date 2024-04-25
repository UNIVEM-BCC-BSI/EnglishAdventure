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
        self.start_button = Button(SCREEN_WIDTH // 2 - 100, 400, 200, 50, "Iniciar Jogo")
        self.credits_button = Button(SCREEN_WIDTH // 2 - 100, 470, 200, 50, "Créditos")
        # Criando o campo de entrada para o nickname
        self.nickname_input = pygame.Rect(SCREEN_WIDTH // 2 - 100, 270, 200, 30)

    def update(self):
        pass

    def draw(self, screen):
        # Desenha o cenário inicial
        background_image = pygame.image.load("imagens/cenario1.jpg").convert()
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


class CreditsScreen(BaseScreen):
    def __init__(self):
        super().__init__()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLACK)  # Preenche a tela com preto
        text = ["Jeann", "Joao Vitor", "Joao Pedro", "Kauan", "Jhenifer", "Thamiris"]
        y = 50
        for name in text:
            name_text = font.render(name, True, WHITE)
            name_rect = name_text.get_rect(center=(SCREEN_WIDTH // 2, y))
            screen.blit(name_text, name_rect)
            y += 50


def main():
    # Criando as telas do jogo
    main_menu_screen = MainMenuScreen()
    phase1_screen = Phase1Screen()
    credits_screen = CreditsScreen()

    current_screen = main_menu_screen  # Define a tela inicial como a tela atual

    nickname = ""  # Definindo a variável nickname

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
                        current_screen = phase1_screen
                    elif main_menu_screen.credits_button.is_clicked(pygame.mouse.get_pos()):
                        # Transição para a tela de créditos ao clicar em "Créditos"
                        current_screen = credits_screen
            elif event.type == pygame.KEYDOWN:
                if current_screen == main_menu_screen:  # Verifica se está na tela inicial
                    # Verifica se o evento de tecla é um caractere imprimível e se o cursor está no retângulo de
                    # entrada de texto
                    if event.unicode.isprintable() and main_menu_screen.nickname_input.collidepoint(
                            pygame.mouse.get_pos()):
                        nickname += event.unicode

        # Atualiza e desenha a tela atual
        screen.fill(BLACK)  # Preenche a tela com preto
        current_screen.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
