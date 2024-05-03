import pygame
import sys

pygame.init()

# Tela
TELA_LARG = 1250
TELA_ALT = 650
tela = pygame.display.set_mode((TELA_LARG, TELA_ALT))
pygame.display.set_caption("English Adventure")

# Cores
BRANCA = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (150, 150, 150)

# Fontes
font = pygame.font.Font(None, 48)
font2 = pygame.font.Font(None, 40)
font3 = pygame.font.Font(None, 36)
font4 = pygame.font.Font(None, 33)
nickname_font = pygame.font.Font(None, 24)

jogador_nome = ""


garota = pygame.image.load("imagem/garoto.png").convert_alpha()
rainha = pygame.image.load("imagem/rainha.png").convert_alpha()
imagem_fundo = pygame.image.load("imagem/Cenarioinicio.jpg").convert_alpha()
cenario = pygame.image.load("imagem/cenario1.png").convert_alpha()


class TelaBase:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self, tela):
        pass


class MenuPrincipal(TelaBase):
    def __init__(self):
        super().__init__()
        self.botao_start = Button(TELA_LARG // 2 - 100, 400, 200, 50, "START")
        self.botao_credito = Button(TELA_LARG // 2 - 100, 470, 200, 50, "Credits")
        self.nickname_input = pygame.Rect(TELA_LARG // 2 - 100, 270, 200, 30)
        self.nickname = ''

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(imagem_fundo, (0, 0))

        titulo_texto = font.render("English Adventure", True, PRETO)
        titulo_retangulo = titulo_texto.get_rect(center=(TELA_LARG // 2, 150))
        tela.blit(titulo_texto, titulo_retangulo)

        # Desenha os botões
        self.botao_start.draw(tela)
        self.botao_credito.draw(tela)

        nickname_text = nickname_font.render("Nickname:", True, PRETO)
        tela.blit(nickname_text, (TELA_LARG // 2 - 100, 250))
        pygame.draw.rect(tela, PRETO, self.nickname_input, 2)

        nickname_input_text = nickname_font.render(self.nickname, True, PRETO)
        tela.blit(nickname_input_text, (TELA_LARG // 2 - 90, 275))

    def lidar_keydown_event(self, event):
        if event.unicode.isprintable() and self.nickname_input.collidepoint(pygame.mouse.get_pos()):
            self.nickname += event.unicode
        elif event.key == pygame.K_BACKSPACE:
            self.nickname = self.nickname[:-1]

    def lidar_mouse_button_down_event(self, pos):
        global jogador_nome
        if self.botao_start.is_clicked(pos):
            self.nickname = self.nickname.strip()
            jogador_nome = self.nickname


class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.ret = pygame.Rect(x, y, width, height)
        self.cor = CINZA
        self.texto = text
        self.acao = action

    def draw(self, tela):
        pygame.draw.rect(tela, self.cor, self.ret)
        superficie_texto = font.render(self.texto, True, PRETO)
        texto_ret = superficie_texto.get_rect(center=self.ret.center)
        tela.blit(superficie_texto, texto_ret)

    def is_clicked(self, pos):
        return self.ret.collidepoint(pos)


class TelaCreditos(TelaBase):
    def __init__(self):
        super().__init__()
        self.voltar_butao = Button(1, 1, 200, 50, "Return")

    def update(self):
        pass

    def draw(self, tela):
        tela.fill(PRETO)
        texto = ["Jeann Garçoni Alves", "Jhenifer Gonçalves Januário", "João Pedro de Oliveira Peres",
                "João Vitor Gaiato", "Kauan Omura Lopes", "Tamires Ledo da Silva Alves"]
        y = 100
        for nome in texto:
            nome_texto = font.render(nome, True, BRANCA)
            nome_ret = nome_texto.get_rect(center=(TELA_LARG // 2, y))
            tela.blit(nome_texto, nome_ret)
            y += 100

        self.voltar_butao.draw(tela)


class TelaIntro(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("FASE 1", "Press SPACE to continue..."),
            (f"{jogador_nome}, é um(a) jovem determinado(a) e com um grande espírito aventureiro",
             f"que nasceu em uma cidade pequena no interior do São Paulo, ",
             f"ele(a) tinha o sonho de viajar pelo mundo e conhecer novas culturas.",
             f"Em um certo dia, {jogador_nome} acaba se inscrevendo em um concurso",
             f"que daria como prêmio uma longa viagem pelos países., ",
             f"Para a surpresa de todos e de si próprio(a),",
             f"{jogador_nome} acaba ganhando e então embarca na maior aventura de sua vida.",
             f"Mas espera aí...  {jogador_nome} não sabe inglês, ",
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

        self.requere_transicao = [4]  # Índices dos textos que exigem transição para outra tela

    def update(self):
        pass

    def draw(self, tela):
        tela.fill(PRETO)

        if self.indice_texto == 0:
            texto1 = font.render(self.textos[self.indice_texto][0], True, BRANCA)
            texto1_ret = texto1.get_rect(center=(TELA_LARG // 2, TELA_ALT // 2))
            tela.blit(texto1, texto1_ret)

            texto2 = font2.render(self.textos[self.indice_texto][1], True, BRANCA)
            texto2_ret = texto2.get_rect(center=(TELA_LARG // 2, 550))
            tela.blit(texto2, texto2_ret)
        elif 0 < self.indice_texto < 4:
            y = 50
            for texto1_ret in self.textos[self.indice_texto]:
                texto3 = font.render(texto1_ret, True, BRANCA)
                texto3_ret = texto3.get_rect(center=(TELA_LARG // 2, y))
                tela.blit(texto3, texto3_ret)
                y += 50
        elif self.indice_texto >= 4:
            if self.indice_texto == 4:
                y = 50
                for texto1_ret in self.textos[self.indice_texto][0:3]:
                    texto3 = font.render(texto1_ret, True, BRANCA)
                    texto3_ret = texto3.get_rect(center=(TELA_LARG // 2, y))
                    tela.blit(texto3, texto3_ret)
                    y += 50

                texto4 = font2.render(self.textos[self.indice_texto][3], True, BRANCA)
                texto4_ret = texto4.get_rect(center=(TELA_LARG // 2, 550))
                tela.blit(texto4, texto4_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return  # Não muda mais o texto se for um texto que requer transição
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Vidas:
    def __init__(self):
        self.max_vidas = 5
        self.vidas_atual = self.max_vidas
        self.coracao_cheio = pygame.image.load("imagem/coracaocheio.png").convert_alpha()
        self.coracao_vazio = pygame.image.load("imagem/coracaovazio.png").convert_alpha()
        self.coracao_larg = self.coracao_cheio.get_width()
        self.coracao_alt = self.coracao_cheio.get_height()
        self.espacamento = 10
        self.posicao = (TELA_LARG - self.max_vidas * (self.coracao_larg + self.espacamento), 10)

    def draw(self, tela):
        x, y = self.posicao
        for i in range(self.vidas_atual):
            tela.blit(self.coracao_cheio, (x + i * (self.coracao_larg + self.espacamento), y))
        for i in range(self.vidas_atual, self.max_vidas):
            tela.blit(self.coracao_vazio, (x + i * (self.coracao_larg + self.espacamento), y))

    def perder_vida(self):
        if self.vidas_atual > 0:
            self.vidas_atual -= 1


class Cenario2(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
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
        self.personagem_imagem = garota
        self.rainha_imagem = rainha
        self.requere_transicao = [4]

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(cenario, (0, 0))

        # Define a margem lateral
        margem = 50

        # Desenhar personagens
        tela.blit(self.personagem_imagem, (margem, TELA_ALT - self.personagem_imagem.get_height() - 50))
        tela.blit(self.rainha_imagem, (
            TELA_LARG - self.rainha_imagem.get_width() - margem, TELA_ALT - self.rainha_imagem.get_height() - 50))

        # Calcular posição do balão de fala
        max_texto_larg = 1200
        texto_larg = min(max(len(text) for text in self.textos[self.indice_texto]) * 17, max_texto_larg)
        texto_alt = len(self.textos[self.indice_texto]) * 55
        x = margem + self.personagem_imagem.get_width() + (
                TELA_LARG - 2 * margem - self.personagem_imagem.get_width() -
                self.rainha_imagem.get_width() - texto_larg) // 2
        y = TELA_ALT - self.rainha_imagem.get_height() - texto_alt - 80

        # Desenhar balão de fala
        pygame.draw.rect(tela, PRETO, (x - 5, y - 5, texto_larg + 10, texto_alt + 10), border_radius=25)
        pygame.draw.rect(tela, BRANCA, (x, y, texto_larg, texto_alt), border_radius=25)

        # Desenhar texto no balão de fala
        y_offset = 0
        for texto in self.textos[self.indice_texto]:
            texto = font.render(texto, True, PRETO)
            texto_ret = texto.get_rect(topleft=(x + 20, y + 20 + y_offset))
            tela.blit(texto, texto_ret)
            y_offset += 45

        if self.indice_texto == 4:
            texto2 = font4.render("Press -> to continue...", True, PRETO)
            texto2_ret = texto2.get_rect(center=(1100, 605))
            tela.blit(texto2, texto2_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Desafio1(TelaBase):
    def __init__(self):
        super().__init__()
        self.pergunta_atual = 0
        self.perguntas = [
            {
                "enunciado": "Preencha as lacunas com as saudações corretas:",
                "pergunta": "___ significa 'Olá'",
                "opcoes": ["1.Hello", "2.Bye Bye", "3.Queen"],
                "resp_correta": 0
            },
            {
                "enunciado": "Preencha as lacunas com as saudações corretas:",
                "pergunta": "___ é usado para desejar um bom dia.",
                "opcoes": ["1.Good afternoon", "2.Good Morning", "3.Queen"],
                "resp_correta": 1
            },
            {
                "enunciado": "Preencha as lacunas com as saudações corretas:",
                "pergunta": "___ é utilizado para cumprimentar alguém à noite.",
                "opcoes": ["1.Hello", "2.Good Morning", "3.Good Night"],
                "resp_correta": 2
            },
            {
                "enunciado": "Reorganize as palavras para formar frases de saudação:",
                "pergunta": "Queen Elizabeth/ night/ !/ Good / ?",
                "opcoes": ["1.Queen Good night, Elizabeth!", "2.Good Night, Queen Elizabeth!", "3.Good Night"],
                "resp_correta": 1
            },
            {
                "enunciado": "Reorganize as palavras para formar frases de saudação:",
                "pergunta": "good / morning / Hello / !",
                "opcoes": ["1.Hello, good morning!", "2.Hello, Morning Good!", "3.Good Night"],
                "resp_correta": 0
            },
            {
                "enunciado": "Reorganize as palavras para formar frases de saudação:",
                "pergunta": "afternoon / Good / !",
                "opcoes": ["1.afternoon, good, !", "2.Good afternoon!", "3.Good Night"],
                "resp_correta": 1
            }
        ]
        self.personagem_imagem = garota
        self.escolha_atual = None

    def update(self):
        pass

    def draw(self, tela):
        global tela_atual
        tela.blit(cenario, (0, 0))
        tela.blit(self.personagem_imagem, (50, TELA_ALT - self.personagem_imagem.get_height() - 50))

        if self.pergunta_atual < len(self.perguntas):
            num_opcoes = len(self.perguntas[self.pergunta_atual]["opcoes"])
            ret_pergunta_altura = num_opcoes * 80 + 160
            ret_pergunta_largura = 800
            pergunta_ret_x = (TELA_LARG - ret_pergunta_largura) // 2
            pergunta_ret_y = (TELA_ALT - ret_pergunta_altura) // 2

            superficie_transparente = pygame.Surface((ret_pergunta_largura, ret_pergunta_altura), pygame.SRCALPHA)
            superficie_transparente.fill((0, 0, 0, 128))
            tela.blit(superficie_transparente, (pergunta_ret_x, pergunta_ret_y))

            enunciado_texto = font2.render(self.perguntas[self.pergunta_atual]["enunciado"], True, PRETO)
            tela.blit(enunciado_texto, (pergunta_ret_x + 20, pergunta_ret_y + 20))

            pergunta_texto = font2.render(self.perguntas[self.pergunta_atual]["pergunta"], True, PRETO)
            tela.blit(pergunta_texto, (pergunta_ret_x + 20, pergunta_ret_y + 60))

            y = pergunta_ret_y + 120
            for indice, opcao in enumerate(self.perguntas[self.pergunta_atual]["opcoes"]):
                opcao_texto = font2.render(opcao, True, PRETO)
                tela.blit(opcao_texto, (pergunta_ret_x + 40, y))
                y += 80
        else:
            tela_atual = cenario3  # Avança para o Cenario3

    def lidar_mouse_button_down_event(self, pos):
        pass

    def lidar_keydown_event(self, event):
        global tela_atual
        if event.key == pygame.K_1:
            self.escolha_atual = 0
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()  # Subtrai uma vida ao errar a pergunta
        elif event.key == pygame.K_2:
            self.escolha_atual = 1
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_3:
            self.escolha_atual = 2
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()

        # Avança para a próxima pergunta
        self.pergunta_atual = (self.pergunta_atual + 1) % len(self.perguntas)

        # Verifica se todas as perguntas foram respondidas
        if self.pergunta_atual == 0:  # Se a próxima pergunta for a primeira, significa que todas foram respondidas
            tela_atual = cenario3


class Cenario3(TelaBase):
    def __init__(self):
        super().__init__()

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(cenario, (0, 0))


vidas = Vidas()
menu_principal = MenuPrincipal()
tela_intro = TelaIntro()
tela_creditos = TelaCreditos()
cenario2 = Cenario2()
desafio1 = Desafio1()
cenario3 = Cenario3()
tela_atual = menu_principal


def main():
    global jogador_nome, tela_atual

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if tela_atual == menu_principal:
                    if menu_principal.botao_start.is_clicked(pygame.mouse.get_pos()):
                        menu_principal.lidar_mouse_button_down_event(pygame.mouse.get_pos())
                        tela_atual = tela_intro
                    elif menu_principal.botao_credito.is_clicked(pygame.mouse.get_pos()):
                        tela_atual = tela_creditos
                if tela_atual == tela_creditos:
                    if tela_creditos.voltar_butao.is_clicked(pygame.mouse.get_pos()):
                        tela_atual = menu_principal
                if tela_atual == desafio1:
                    desafio1.lidar_mouse_button_down_event(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                menu_principal.lidar_keydown_event(event)
                if tela_atual == tela_intro:
                    if event.key == pygame.K_SPACE:
                        tela_intro.change_text()
                    elif event.key == pygame.K_RIGHT:
                        if tela_intro.indice_texto in tela_intro.requere_transicao:
                            tela_atual = cenario2
                elif tela_atual == cenario2:
                    if event.key == pygame.K_SPACE:
                        cenario2.change_text()
                    if event.key == pygame.K_RIGHT:
                        if cenario2.indice_texto in cenario2.requere_transicao:
                            tela_atual = desafio1
                elif tela_atual == desafio1:
                    if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                        desafio1.lidar_keydown_event(event)
                elif tela_atual == cenario3:
                    if event.key == pygame.K_RIGHT:
                        tela_atual = cenario2

        tela.fill(PRETO)
        tela_atual.draw(tela)
        vidas.draw(tela)
        pygame.display.flip()


if __name__ == "__main__":
    main()
