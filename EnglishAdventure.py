import pygame
import sys

pygame.init()

# Tela
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("English Adventure")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Fontes
font = pygame.font.Font(None, 48)
font2 = pygame.font.Font(None, 40)
font3 = pygame.font.Font(None, 36)
font4 = pygame.font.Font(None, 33)
nickname_font = pygame.font.Font(None, 24)

player_name = ""


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
        self.start_button = Button(SCREEN_WIDTH // 2 - 100, 400, 200, 50, "START")
        self.credits_button = Button(SCREEN_WIDTH // 2 - 100, 470, 200, 50, "Credits")
        self.nickname_input = pygame.Rect(SCREEN_WIDTH // 2 - 100, 270, 200, 30)
        self.nickname = ''

    def update(self):
        pass

    def draw(self, screen):
        background_image = pygame.image.load("imagens/cenario1.jpg").convert()
        screen.blit(background_image, (0, 0))

        title_text = font.render("English Adventure", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        screen.blit(title_text, title_rect)

        # Desenha os botões
        self.start_button.draw(screen)
        self.credits_button.draw(screen)

        nickname_text = nickname_font.render("Nickname:", True, BLACK)
        screen.blit(nickname_text, (SCREEN_WIDTH // 2 - 100, 250))
        pygame.draw.rect(screen, BLACK, self.nickname_input, 2)

        nickname_input_text = nickname_font.render(self.nickname, True, BLACK)
        screen.blit(nickname_input_text, (SCREEN_WIDTH // 2 - 90, 275))

    def handle_keydown_event(self, event):
        if event.unicode.isprintable() and self.nickname_input.collidepoint(pygame.mouse.get_pos()):
            self.nickname += event.unicode
        elif event.key == pygame.K_BACKSPACE:
            self.nickname = self.nickname[:-1]

    def handle_mouse_button_down_event(self, pos):
        global player_name
        if self.start_button.is_clicked(pos):
            self.nickname = self.nickname.strip()
            player_name = self.nickname


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


class CreditsScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.voltar_button = Button(1, 1, 200, 50, "Return")

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLACK)
        text = ["Jeann Garçoni Alves", "Jhenifer Gonçalves Januário", "João Pedro de Oliveira Peres",
                "João Vitor Gaiato", "Kauan Omura Lopes", "Tamires Ledo da Silva Alves"]
        y = 100
        for name in text:
            name_text = font.render(name, True, WHITE)
            name_rect = name_text.get_rect(center=(SCREEN_WIDTH // 2, y))
            screen.blit(name_text, name_rect)
            y += 100

        self.voltar_button.draw(screen)


class Phase1Screen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.text_index = 0
        self.texts = [
            ("FASE 1", "Press SPACE to continue..."),
            (f"{player_name}, é um(a) jovem determinado(a) e com um grande espírito aventureiro",
             f"que nasceu em uma cidade pequena no interior do São Paulo, ",
             f"ele(a) tinha o sonho de viajar pelo mundo e conhecer novas culturas.",
             f"Em um certo dia, {player_name} acaba se inscrevendo em um concurso",
             f"que daria como prêmio uma longa viagem pelos países., ",
             f"Para a surpresa de todos e de si próprio(a),",
             f"{player_name} acaba ganhando e então embarca na maior aventura de sua vida.",
             f"Mas espera aí...  {player_name} não sabe inglês, ",
             f"então essa viagem também será uma grande aprendizagem."),
            ("O seu primeiro destino será Londres, Inglaterra.",
             "Lá você vai conhecer vários monumentos turísticos. ",
             "E aprender muito com personagens locais históricos!"),
            ("Bem-vindo a Londres, capital da Inglaterra e do Reino Unido,",
             "é uma cidade do século 21 com uma história que remonta à era romana.",
             "Seu centro abriga as sedes imponentes do Parlamento ",
             "e a famosa torre do relógio do Big Ben."),
            (f"Parabéns, você recebeu o convite para um tour pelo palacio real",
             "acompanhado(a) pessoalmente pela própria Rainha,",
             "essa é uma oportunidade muito especial e única!",
             "Press RIGHT(->) to continue... ")
        ]

        self.requires_transition = [4]  # Índices dos textos que exigem transição para outra tela

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLACK)

        if self.text_index == 0:
            text1 = font.render(self.texts[self.text_index][0], True, WHITE)
            text1_rect = text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text1, text1_rect)

            text2 = font2.render(self.texts[self.text_index][1], True, WHITE)
            text2_rect = text2.get_rect(center=(SCREEN_WIDTH // 2, 550))
            screen.blit(text2, text2_rect)
        elif 0 < self.text_index < 4:
            y = 50
            for texto in self.texts[self.text_index]:
                text3 = font.render(texto, True, WHITE)
                text3_rect = text3.get_rect(center=(SCREEN_WIDTH // 2, y))
                screen.blit(text3, text3_rect)
                y += 50
        elif self.text_index >= 4:
            if self.text_index == 4:
                y = 50
                for texto in self.texts[self.text_index][0:3]:
                    text3 = font.render(texto, True, WHITE)
                    text3_rect = text3.get_rect(center=(SCREEN_WIDTH // 2, y))
                    screen.blit(text3, text3_rect)
                    y += 50

                text4 = font2.render(self.texts[self.text_index][3], True, WHITE)
                text4_rect = text4.get_rect(center=(SCREEN_WIDTH // 2, 550))
                screen.blit(text4, text4_rect)

    def change_text(self):
        if self.text_index in self.requires_transition:
            return  # Não muda mais o texto se for um texto que requer transição
        self.text_index = (self.text_index + 1) % len(self.texts)


class Cenario2(BaseScreen):
    def __init__(self):
        super().__init__()
        self.text_index = 0
        self.texts = [
            ("Welcome to the Buckingham Palace! I am Queen Elizabeth,",
             "e estou aqui para ensinar-lhes várias importantes em inglês."),
            ("Let's start with the greetings, as saudações, ",
             "que são essenciais para qualquer conversa educada. "),
            ("'Hello' significa 'Olá'. Temos também 'Good morning' ",
             "para desejar um bom dia.",
             "And 'Good afternoon' para dizer boa tarde. Very good!!!Muito bem!!!"),
            ("Agora, para um rápido desafio, vou fazer algumas perguntas simples,",
             "vamos ver se você se lembra:"),
            ("Para selecionar a resposta que deseja, aperte as teclas: ",
             "1, 2 ou 3")
        ]
        self.persona_image = pygame.image.load("imagens/Personagem.png").convert_alpha()
        self.rainha_image = pygame.image.load("imagens/Rainha (1).png").convert_alpha()
        self.requires_transition = [4]

    def update(self):
        pass

    def draw(self, screen):
        cenario2 = pygame.image.load("imagens/castelo4.png").convert()
        screen.blit(cenario2, (0, 0))

        # Define a margem lateral
        margin = 50

        # Desenhar personagens
        screen.blit(self.persona_image, (margin, SCREEN_HEIGHT - self.persona_image.get_height() - 50))
        screen.blit(self.rainha_image, (
            SCREEN_WIDTH - self.rainha_image.get_width() - margin, SCREEN_HEIGHT - self.rainha_image.get_height() - 50))

        # Calcular posição do balão de fala
        max_text_width = 1200
        text_width = min(max(len(text) for text in self.texts[self.text_index]) * 17, max_text_width)
        text_height = len(self.texts[self.text_index]) * 55
        x = margin + self.persona_image.get_width() + (
                SCREEN_WIDTH - 2 * margin - self.persona_image.get_width() -
                self.rainha_image.get_width() - text_width) // 2
        y = SCREEN_HEIGHT - self.rainha_image.get_height() - text_height - 80

        # Desenhar balão de fala
        pygame.draw.rect(screen, BLACK, (x - 5, y - 5, text_width + 10, text_height + 10), border_radius=25)
        pygame.draw.rect(screen, WHITE, (x, y, text_width, text_height), border_radius=25)

        # Desenhar texto no balão de fala
        y_offset = 0
        for texto in self.texts[self.text_index]:
            text = font.render(texto, True, BLACK)
            text_rect = text.get_rect(topleft=(x + 20, y + 20 + y_offset))
            screen.blit(text, text_rect)
            y_offset += 45

        if self.text_index == 4:
            text2 = font4.render("Press -> to continue...", True, BLACK)
            text2_rect = text2.get_rect(center=(1100, 605))
            screen.blit(text2, text2_rect)

    def change_text(self):
        if self.text_index in self.requires_transition:
            return
        self.text_index = (self.text_index + 1) % len(self.texts)


class Desafio1(BaseScreen):
    def __init__(self):
        super().__init__()
        self.current_question = 0
        self.questions = [
            {
                "enunciado": "Preencha as lacunas com as saudações corretas:",
                "pergunta": "___ significa 'Olá'",
                "opcoes": ["Hello", "Bye Bye", "Queen"],
                "resposta_correta": 0
            },
            {
                "enunciado": "Preencha as lacunas com as saudações corretas:",
                "pergunta": "___ é usado para desejar um bom dia.",
                "opcoes": ["Good afternoon", "Good Morning", "Queen"],
                "resposta_correta": 1
            },
            {
                "enunciado": "Preencha as lacunas com as saudações corretas:",
                "pergunta": "___ é utilizado para cumprimentar alguém à noite.",
                "opcoes": ["Hello", "Good Morning", "Good Night"],
                "resposta_correta": 2
            }
        ]
        self.persona_image = pygame.image.load("imagens/Personagem.png").convert_alpha()
        self.current_choice = None

    def update(self):
        pass

    def draw(self, screen):
        cenario2 = pygame.image.load("imagens/castelo4.png").convert()
        screen.blit(cenario2, (0, 0))
        screen.blit(self.persona_image, (50, SCREEN_HEIGHT - self.persona_image.get_height() - 50))

        num_opcoes = len(self.questions[self.current_question]["opcoes"])
        question_rect_height = num_opcoes * 80 + 160
        question_rect_width = 800
        question_rect_x = (SCREEN_WIDTH - question_rect_width) // 2
        question_rect_y = (SCREEN_HEIGHT - question_rect_height) // 2

        transparent_surface = pygame.Surface((question_rect_width, question_rect_height), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 128))  # Cor preta com um valor de alfa de 128 (semi-transparente)
        screen.blit(transparent_surface, (question_rect_x, question_rect_y))

        enunciado_text = font2.render(self.questions[self.current_question]["enunciado"], True, BLACK)
        screen.blit(enunciado_text, (question_rect_x + 20, question_rect_y + 20))

        pergunta_text = font2.render(self.questions[self.current_question]["pergunta"], True, BLACK)
        screen.blit(pergunta_text, (question_rect_x + 20, question_rect_y + 60))

        y = question_rect_y + 120
        for index, opcao in enumerate(self.questions[self.current_question]["opcoes"]):
            opcao_text = font2.render(opcao, True, BLACK)
            screen.blit(opcao_text, (question_rect_x + 40, y))
            y += 80

    def handle_mouse_button_down_event(self, pos):
        pass

    def handle_keydown_event(self, event):
        if event.key == pygame.K_1:
            self.current_choice = 0
            if self.current_choice == self.questions[self.current_question]["resposta_correta"]:
                self.current_question = (self.current_question + 1) % len(self.questions)
        elif event.key == pygame.K_2:
            self.current_choice = 1
            if self.current_choice == self.questions[self.current_question]["resposta_correta"]:
                self.current_question = (self.current_question + 1) % len(self.questions)
        elif event.key == pygame.K_3:
            self.current_choice = 2
            if self.current_choice == self.questions[self.current_question]["resposta_correta"]:
                self.current_question = (self.current_question + 1) % len(self.questions)


class Cenario3(BaseScreen):
    def __init__(self):
        super().__init__()
        self.persona_image = pygame.image.load("imagens/Personagem.png").convert_alpha()

    def update(self):
        pass

    def draw(self, screen):
        cenario2 = pygame.image.load("imagens/castelo4.png").convert()
        screen.blit(cenario2, (0, 0))
        screen.blit(self.persona_image, (50, SCREEN_HEIGHT - self.persona_image.get_height() - 50))


def main():
    global player_name
    main_menu_screen = MainMenuScreen()
    phase1_screen = Phase1Screen()
    credits_screen = CreditsScreen()
    cenario2 = Cenario2()
    desafio1 = Desafio1()
    cenario3 = Cenario3()
    current_screen = main_menu_screen

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_screen == main_menu_screen:
                    if main_menu_screen.start_button.is_clicked(pygame.mouse.get_pos()):
                        main_menu_screen.handle_mouse_button_down_event(pygame.mouse.get_pos())
                        current_screen = phase1_screen
                    elif main_menu_screen.credits_button.is_clicked(pygame.mouse.get_pos()):
                        current_screen = credits_screen
                if current_screen == credits_screen:
                    if credits_screen.voltar_button.is_clicked(pygame.mouse.get_pos()):
                        current_screen = main_menu_screen
                if current_screen == desafio1:
                    desafio1.handle_mouse_button_down_event(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                main_menu_screen.handle_keydown_event(event)
                if current_screen == phase1_screen:
                    if event.key == pygame.K_SPACE:
                        phase1_screen.change_text()
                    elif event.key == pygame.K_RIGHT:
                        if phase1_screen.text_index in phase1_screen.requires_transition:
                            current_screen = cenario2
                elif current_screen == cenario2:
                    if event.key == pygame.K_SPACE:
                        cenario2.change_text()
                    if event.key == pygame.K_RIGHT:
                        if cenario2.text_index in cenario2.requires_transition:
                            current_screen = desafio1
                elif current_screen == desafio1:
                    if current_screen == desafio1:
                        desafio1.handle_keydown_event(event)

        screen.fill(BLACK)
        current_screen.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
