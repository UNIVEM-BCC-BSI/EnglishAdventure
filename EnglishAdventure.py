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
TRANSP = (0, 0, 0, 128)

# Fontes
font = pygame.font.Font(None, 48)
font2 = pygame.font.Font(None, 40)
font3 = pygame.font.Font(None, 36)
font4 = pygame.font.Font(None, 33)
font5 = pygame.font.Font('pixelfont.ttf', 60)
font6 = pygame.font.Font('pixelfont.ttf', 48)
font7 = pygame.font.Font('pixelfont.ttf', 42)

# Imagens
garoto = pygame.image.load("imagens/garoto.png").convert_alpha()
rainha = pygame.image.load("imagens/rainha.png").convert_alpha()
guarda = pygame.image.load("imagens/guardareal.png").convert_alpha()
harrypotter = pygame.image.load("imagens/harrypotter1.png").convert_alpha()
imagem_fundo = pygame.image.load("imagens/cenario_inicio.jpeg").convert_alpha()
cenario_img = pygame.image.load("imagens/cenario1.png").convert_alpha()
cenario2_img = pygame.image.load("imagens/insidecastle.png").convert_alpha()
hogwarts = pygame.image.load("imagens/hogwarts.jpg").convert_alpha()


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
        self.botao_start = Button(TELA_LARG // 2 - 100, 300, 200, 50, CINZA, "START")
        self.botao_credito = Button(TELA_LARG // 2 - 100, 370, 200, 50, CINZA, "Credits")

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(imagem_fundo, (0, 0))

        titulo_texto = font5.render("English Adventure", True, PRETO)
        titulo_retangulo = titulo_texto.get_rect(center=(TELA_LARG // 2, 70))
        tela.blit(titulo_texto, titulo_retangulo)

        # Desenha os personagens
        self.botao_start.draw(tela)
        self.botao_credito.draw(tela)


class Button:
    def __init__(self, x, y, width, height, cor, text='', action=None):
        self.ret = pygame.Rect(x, y, width, height)
        self.cor = cor
        self.texto = text
        self.acao = action

    def draw(self, tela):
        pygame.draw.rect(tela, self.cor, self.ret)
        superficie_texto = font6.render(self.texto, True, PRETO)
        texto_ret = superficie_texto.get_rect(center=self.ret.center)
        tela.blit(superficie_texto, texto_ret)

    def is_clicked(self, pos):
        return self.ret.collidepoint(pos)


class TelaCreditos(TelaBase):
    def __init__(self):
        super().__init__()
        self.voltar_butao = Button(1, 1, 200, 50, CINZA, "Return")

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


class TelaIntro1(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("PHASE 1", "Press SPACE to continue..."),
            (f"John, é determinado e com um grande espírito aventureiro",
             "que nasceu em uma cidade pequena no interior do São Paulo, ",
             "e tinha o sonho de viajar pelo mundo e conhecer novas culturas.",
             f"Em um certo dia, John acaba se inscrevendo em um concurso",
             "que daria como prêmio uma longa viagem pelos países., ",
             f"Para a surpresa de todos e de si própria,  John",
             "acaba ganhando e então embarca na maior aventura de sua vida.",
             f"Mas espera aí...  John não sabe inglês, ",
             "então essa viagem também será uma grande aprendizagem."),
            ("O seu primeiro destino será Londres, Inglaterra.",
             f"Lá você, John, vai conhecer vários monumentos turísticos. ",
             "E aprender muito com personagens locais históricos!"),
            ("Bem-vindo a Londres, capital da Inglaterra e do Reino Unido,",
             "é uma cidade do século 21 com uma história que remonta à era romana.",
             "Seu centro abriga as sedes imponentes do Parlamento ",
             "e a famosa torre do relógio do Big Ben."),
            ("Parabéns, você recebeu o convite para um tour pelo palácio real",
             "acompanhado(a) pessoalmente pela própria Rainha,",
             "essa é uma oportunidade muito especial e única!",
             "Press RIGHT(->) to continue... ")
        ]

        self.requere_transicao = [4]

    def update(self):
        pass

    def draw(self, tela):
        tela.fill(PRETO)
        if self.indice_texto == 0:
            texto1 = font5.render(self.textos[self.indice_texto][0], True, BRANCA)
            texto1_ret = texto1.get_rect(center=(TELA_LARG // 2, TELA_ALT // 2))
            tela.blit(texto1, texto1_ret)

            texto2 = font6.render(self.textos[self.indice_texto][1], True, BRANCA)
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

                texto4 = font6.render(self.textos[self.indice_texto][3], True, BRANCA)
                texto4_ret = texto4.get_rect(center=(TELA_LARG // 2, 550))
                tela.blit(texto4, texto4_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Vidas:
    def __init__(self):
        self.max_vidas = 5
        self.vidas_atual = self.max_vidas
        self.coracao_cheio = pygame.image.load("imagens/coracaocheio.png").convert_alpha()
        self.coracao_vazio = pygame.image.load("imagens/coracaovazio.png").convert_alpha()
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
        global tela_atual
        if self.vidas_atual > 0:
            self.vidas_atual -= 1
        if self.vidas_atual == 0:
            tela_atual = falhou
        if tela_atual == falhou:
            self.vidas_atual = 5


class Cenario1(TelaBase):
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
        self.personagem_imagem = garoto
        self.rainha_imagem = rainha
        self.requere_transicao = [4]

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(cenario_img, (0, 0))

        margem = 50

        # Desenhar personagens
        tela.blit(self.personagem_imagem, (margem, TELA_ALT - self.personagem_imagem.get_height() - 50))
        tela.blit(self.rainha_imagem, (
            TELA_LARG - self.rainha_imagem.get_width() - margem, TELA_ALT - self.rainha_imagem.get_height() - 50))

        # Calcular posição do balão de fala
        max_texto_larg = 800
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
            texto = font4.render(texto, True, PRETO)
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
            }
        ]
        self.personagem_imagem = garoto
        self.escolha_atual = None

    def update(self):
        pass

    def draw(self, tela):
        global tela_atual
        tela.blit(cenario_img, (0, 0))
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
            tela_atual = cenario2

    def lidar_mouse_button_down_event(self, pos):
        pass

    def lidar_keydown_event(self, event):
        global tela_atual
        if event.key == pygame.K_1:
            self.escolha_atual = 0
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_2:
            self.escolha_atual = 1
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_3:
            self.escolha_atual = 2
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()

        self.pergunta_atual = (self.pergunta_atual + 1) % len(self.perguntas)

        if self.pergunta_atual == 0:
            tela_atual = cenario2


class Cenario2(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("Bem-vindos novamente, meu aprendiz! Now we already know ",
             "the greetings, vamos dar um passo adiante e aprender sobre ",
             "o tão temido verbo 'to be', que na verdade nem é tão temido assim."),
            ("SO, DON’T BE AFRAID!! Não tenha medo! Este é um",
             "dos verbos mais importantes em inglês, pois nos",
             "ajuda a descrever quem somos e como nos sentimos."),
            ("Vamos começar com os pronomes pessoais. 'I' (eu), 'you' (você), 'he' (ele), ",
             "'she' (ela), 'it' (ele/ela para coisas ou animais), 'we' (nós) e ",
             "'they' (eles/elas)."),
            ("Agora, vamos ver como usar o verb 'to be', que significa: 'Ser' ou 'Estar', ",
             "com essas pessoas. Por exemplo: 'I am the Queen' (Eu sou a Rainha), ",
             "estou falando de mim. 'You are my guests' (Vocês são meus convidados), ",
             "estou falando de você ou vocês."),
            ("'He is a guard' (Ele é um guarda), estou falando dele.",
             "'She is a gracious lady' (Ela é uma dama graciosa), estou ",
             "falando dela.",
             "'It is a beautiful palace' (É um belo palácio), nesse posso falar de ",
             "algo ou um animal."),
            ("'We are friends' (Nós somos amigos), estou falando de mim e de você.",
             "'They are in the castle' (Eles estão dentro do castelo), estou falando deles."),
            ("Note que, modificamos o verbo 'To BE' dependendo de quem estamos ",
             "falando.E se quisermos falar de forma negativa é só colocar o “not” na",
             "frente: 'You are not the queen!'. Agora preciso que você complete o ",
             "próximo desafio para que possamos continuar a nossa jornada! ")
        ]
        self.personagem_imagem = garoto
        self.rainha_imagem = rainha
        self.requere_transicao = [6]

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(cenario2_img, (0, 0))

        # Define a margem lateral
        margem = 50

        # Desenhar personagens
        tela.blit(self.personagem_imagem, (margem, TELA_ALT - self.personagem_imagem.get_height() - 50))
        tela.blit(self.rainha_imagem, (
            TELA_LARG - self.rainha_imagem.get_width() - margem, TELA_ALT - self.rainha_imagem.get_height() - 50))

        # Calcular posição do balão de fala
        max_texto_larg = 1000
        texto_larg = min(max(len(text) for text in self.textos[self.indice_texto]) * 18, max_texto_larg)
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
            texto = font4.render(texto, True, PRETO)
            texto_ret = texto.get_rect(topleft=(x + 20, y + 20 + y_offset))
            tela.blit(texto, texto_ret)
            y_offset += 45

        if self.indice_texto == 6:
            texto2 = font4.render("Press -> to continue...", True, PRETO)
            texto2_ret = texto2.get_rect(center=(1100, 605))
            tela.blit(texto2, texto2_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Desafio2(TelaBase):
    def __init__(self):
        super().__init__()
        self.pergunta_atual = 0
        self.perguntas = [
            {
                "enunciado": "Complete as lacunas com as formas corretas do verbo 'to be':",
                "pergunta": "___ the Queen.",
                "opcoes": ["1.I am", "2.You am", "3.She am"],
                "resp_correta": 0
            },
            {
                "enunciado": "Complete as lacunas com as formas corretas do verbo 'to be':",
                "pergunta": "___ a guard.",
                "opcoes": ["1.She are", "2.We is", "3.He is"],
                "resp_correta": 2
            },
            {
                "enunciado": "Transforme as frases afirmativas em negativas:",
                "pergunta": "He is a noble guard.",
                "opcoes": ["1.He not a noble guard.", "2.He is not a noble guard.", "3.He are not a noble guard"],
                "resp_correta": 1
            },
            {
                "enunciado": "Transforme as frases afirmativas em negativas:",
                "pergunta": "We are friends and family.",
                "opcoes": ["1.We are not friends and family.", "2.We not are friends and not family.",
                           "3.We is not friends and family."],
                "resp_correta": 0
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "He is a noble guard.",
                "opcoes": ["1.Is he a noble guard", "2.Guard night he is?", "3.Is he a noble guard?"],
                "resp_correta": 2
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "We are friends and family.",
                "opcoes": ["1.Are friends and family we?", "2.Are we friends and family?",
                           "3.Is we friends and family?"],
                "resp_correta": 1
            },
            {
                "enunciado": "Responda às perguntas com frases completas:",
                "pergunta": "Are you the Queen?",
                "opcoes": ["1,Yes, I am the Queen!", "2.Yes, I the Queen!", "3.No, I is the queen."],
                "resp_correta": 0
            },
            {
                "enunciado": "Responda às perguntas com frases completas:",
                "pergunta": "Is he a noble guard?",
                "opcoes": ["1.No, he is noble guard!", "2.No, he is not a noble guard!",
                           "3.No, she not is a noble guard."],
                "resp_correta": 1
            }
        ]
        self.personagem_imagem = garoto
        self.escolha_atual = None

    def update(self):
        pass

    def draw(self, tela):
        global tela_atual
        tela.blit(cenario2_img, (0, 0))
        tela.blit(self.personagem_imagem, (50, TELA_ALT - self.personagem_imagem.get_height() - 50))

        if self.pergunta_atual < len(self.perguntas):
            num_opcoes = len(self.perguntas[self.pergunta_atual]["opcoes"])
            ret_pergunta_altura = num_opcoes * 80 + 160
            ret_pergunta_largura = 900
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
            tela_atual = cenario3

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

        self.pergunta_atual = (self.pergunta_atual + 1) % len(self.perguntas)

        if self.pergunta_atual == 0:
            tela_atual = cenario3


class Cenario3(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("Agora, que você também já sabe o 'verb to be', é hora de aprender ",
             "como usar todos os outros verbos para descrever coisas que você ou",
             "ou outras pessoas fazem."),
            ("Here, in the Buckingham Palace, podemos observar várias",
             "pessoas que tem suas funções."),
            ("For example, se eu for falar de mim e o que eu faço,",
             "posso dizer: 'I RULE the kingdom' (Eu GOVERNO o reino)."),
            ("Agora se eu fosse falar de você: 'You STUDY English' (Você ESTUDA ",
             "Inglês.). Ou ainda: 'They LOVE the castle' (Eles AMAM o castelo). ",
             "E também: 'We like London'(Nós GOSTAMOS de Londres).",
             "Agora, um rápido desafio!")
        ]
        self.personagem_imagem = garoto
        self.rainha_imagem = rainha
        self.requere_transicao = [3]

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(cenario2_img, (0, 0))

        # Define a margem lateral
        margem = 50

        # Desenhar personagens
        tela.blit(self.personagem_imagem, (margem, TELA_ALT - self.personagem_imagem.get_height() - 50))
        tela.blit(self.rainha_imagem, (
            TELA_LARG - self.rainha_imagem.get_width() - margem, TELA_ALT - self.rainha_imagem.get_height() - 50))

        # Calcular posição do balão de fala
        max_texto_larg = 800
        texto_larg = min(max(len(text) for text in self.textos[self.indice_texto]) * 18, max_texto_larg)
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
            texto = font4.render(texto, True, PRETO)
            texto_ret = texto.get_rect(topleft=(x + 20, y + 20 + y_offset))
            tela.blit(texto, texto_ret)
            y_offset += 45

        if self.indice_texto == 3:
            texto2 = font4.render("Press -> to continue...", True, PRETO)
            texto2_ret = texto2.get_rect(center=(1100, 605))
            tela.blit(texto2, texto2_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Desafio3(TelaBase):
    def __init__(self):
        super().__init__()
        self.pergunta_atual = 0
        self.perguntas = [
            {
                "enunciado": "Reorganize as palavras para formar frases afirmativas:",
                "pergunta": "the castle / they / love.",
                "opcoes": ["1.love the castle they", "2.Castle love the they", "3.They love the castle!"],
                "resp_correta": 2
            },
            {
                "enunciado": "Reorganize as palavras para formar frases afirmativas:",
                "pergunta": "like / I /and/ the queen/ London.",
                "opcoes": ["1.I like London and the queen!", "2.London and the queen like I",
                           "3.Quenn like London and me"],
                "resp_correta": 0
            },
            {
                "enunciado": "Reorganize as palavras para formar frases afirmativas:",
                "pergunta": "rule / You / the kingdom.",
                "opcoes": ["1. Kingdom the you rule", "2.You rule the kingdom!", "3.rule the kingdom you!"],
                "resp_correta": 1
            }
        ]
        self.personagem_imagem = garoto
        self.escolha_atual = None

    def update(self):
        pass

    def draw(self, tela):
        global tela_atual
        tela.blit(cenario2_img, (0, 0))
        tela.blit(self.personagem_imagem, (50, TELA_ALT - self.personagem_imagem.get_height() - 50))

        if self.pergunta_atual < len(self.perguntas):
            num_opcoes = len(self.perguntas[self.pergunta_atual]["opcoes"])
            ret_pergunta_altura = num_opcoes * 80 + 160
            ret_pergunta_largura = 900
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
            tela_atual = cenario4

    def lidar_mouse_button_down_event(self, pos):
        pass

    def lidar_keydown_event(self, event):
        global tela_atual
        if event.key == pygame.K_1:
            self.escolha_atual = 0
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_2:
            self.escolha_atual = 1
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_3:
            self.escolha_atual = 2
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()

        self.pergunta_atual = (self.pergunta_atual + 1) % len(self.perguntas)

        if self.pergunta_atual == 0:
            tela_atual = cenario4


class Cenario4(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("A simple, but very importante detail, quando usamos",
             "dois verbos juntos em uma frase, como 'I like to dance'",
             "(Eu gosto de dançar), usamos a palavra 'to' antes",
             "do segundo verbo."),
            ("Isso nos ajuda a conectar os dois verbos e indicar a ação pretendida.",
             "Por exemplo: 'You love TO explore' (Vocês adoram explorar) ou",
             "'We need TO learn' (Nós precisamos aprender)."),
            ("Para expressar frases na forma negativa, assim como no usamos agora ",
             "pouco você só precisa colocar o DON’T na frente da pessoa da frase."),
            ("Por exemplo: 'You don’t rule the kingdom' (Você não governa o reino),",
             "'We don’t explore the gardens' (Nós não exploramos os jardins),",
             "'They don’t admire the architecture' (Eles não admiram a arquitetura).",
             "That simple!!!"),
            ("Para perguntar algo a alguem ou sobre alguem é tão simples quanto!",
             "É só colocar o 'DO' no começo da frase e o ponto '?' no final1!"),
            ("Por exemplo: 'Do you rule the kingdom?' (Você governa o reino?),",
             "'Do we explore the gardens?' (Nós exploramos os jardins?),",
             "'Do they admire the architecture?' (Eles admiram a arquitetura?)."),
            ("Agora que você já sabe muita coisa, está na hora de praticar,",
             "se você conseguir passar desse desafio eu vou te levar",
             "para conhecer um amigo meu!")
        ]
        self.personagem_imagem = garoto
        self.rainha_imagem = rainha
        self.requere_transicao = [6]

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(cenario2_img, (0, 0))

        # Define a margem lateral
        margem = 50

        # Desenhar personagens
        tela.blit(self.personagem_imagem, (margem, TELA_ALT - self.personagem_imagem.get_height() - 50))
        tela.blit(self.rainha_imagem, (
            TELA_LARG - self.rainha_imagem.get_width() - margem, TELA_ALT - self.rainha_imagem.get_height() - 50))

        # Calcular posição do balão de fala
        max_texto_larg = 900
        texto_larg = min(max(len(text) for text in self.textos[self.indice_texto]) * 18, max_texto_larg)
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
            texto = font4.render(texto, True, PRETO)
            texto_ret = texto.get_rect(topleft=(x + 20, y + 20 + y_offset))
            tela.blit(texto, texto_ret)
            y_offset += 45

        if self.indice_texto == 6:
            texto2 = font4.render("Press -> to continue...", True, PRETO)
            texto2_ret = texto2.get_rect(center=(1100, 605))
            tela.blit(texto2, texto2_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Desafio4(TelaBase):
    def __init__(self):
        super().__init__()
        self.pergunta_atual = 0
        self.perguntas = [
            {
                "enunciado": "Qual a tradução correta?",
                "pergunta": "Eles gostam de estudar",
                "opcoes": ["1.They love to explore", "2.They like to study", "3.They want to visit"],
                "resp_correta": 1
            },
            {
                "enunciado": "Qual a tradução correta?",
                "pergunta": "Eu gosto de ler",
                "opcoes": ["1.I need to buy", "2.I want to play", "3.I like to read"],
                "resp_correta": 2
            },
            {
                "enunciado": "Complete as lacunas com as frases NEGATIVAS corretas:",
                "pergunta": "___ rule the kingdom.",
                "opcoes": ["1.We", "2.You don’t", "3.She is"],
                "resp_correta": 1
            },
            {
                "enunciado": "Complete as lacunas com as frases NEGATIVAS corretas:",
                "pergunta": "___like ___ explore the gardens.",
                "opcoes": ["1.They don’t/ to", "2.He don’t/ is", "3.We/don’t"],
                "resp_correta": 0
            },
            {
                "enunciado": "Transforme as frases afirmativas em perguntas:",
                "pergunta": "You explore the gardens.",
                "opcoes": ["1.Do you explore the gardens?", "2.You explore the gardens?",
                           "3.Do to explore the gardens!"],
                "resp_correta": 0
            },
            {
                "enunciado": "Transforme as frases afirmativas em perguntas:",
                "pergunta": "They admire the architecture. →",
                "opcoes": ["1.Do you admire the architecture?", "2.Do they admire the architecture?",
                           "3.The queen admire the architecture?"],
                "resp_correta": 1
            }
        ]
        self.personagem_imagem = garoto
        self.escolha_atual = None

    def update(self):
        pass

    def draw(self, tela):
        global tela_atual
        tela.blit(cenario2_img, (0, 0))
        tela.blit(self.personagem_imagem, (50, TELA_ALT - self.personagem_imagem.get_height() - 50))

        if self.pergunta_atual < len(self.perguntas):
            num_opcoes = len(self.perguntas[self.pergunta_atual]["opcoes"])
            ret_pergunta_altura = num_opcoes * 80 + 160
            ret_pergunta_largura = 900
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
            tela_atual = cenario5

    def lidar_mouse_button_down_event(self, pos):
        pass

    def lidar_keydown_event(self, event):
        global tela_atual
        if event.key == pygame.K_1:
            self.escolha_atual = 0
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_2:
            self.escolha_atual = 1
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_3:
            self.escolha_atual = 2
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()

        self.pergunta_atual = (self.pergunta_atual + 1) % len(self.perguntas)

        if self.pergunta_atual == 0:
            tela_atual = cenario5


class Cenario5(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("Você está vendo aquela pessoa lá na frente? So far!",
             "That is my friend, ‘The guard', para eu poder te",
             "apresentar a ele, you have to learn, você tem que aprender",
             "a como falar de alguem que não está na conversa."),
            ("Do you remember: 'He is, She is, It is?', então",
             "com todos os outros verbos é quase a mesma coisa, só temos",
             "que adicionar um little detail no final1.",
             "The letter 's' nas frases afirmativas:"),
            ("He protects the Queen! (Ele protege a rainha).",
             "The gardener (a jardineira), ela deixa o jardim bonito:",
             "The gardener cuts the grass!(A jardineira corta a grama)."),
            ("Ou podemos falar até daquele dog, 'the dog loves to play'",
             "or 'it loves to play!'."),
            ("Percebeu que podemos falar de alguem tanto usando o nome,",
             "ou profissão, como os pronomes."),
            ("Agora, para falarmos na negativa temos que adicionar o",
             "'DOESN'T' entre a pessoa e o verbo(verbo volta a forma normal.",
             "Ex: The queen doesn't play football."),
            ("E se quisermos perguntar algo sobre alguem? Muito simples!",
             "É só colocar o 'Does' no começo e manter o resto igual, com '?'",
             "no final1. Ex: 'Does the queen play football?",
             "Agora vamos praticar!")
        ]
        self.personagem_imagem = garoto
        self.rainha_imagem = rainha
        # self.guarda_imagem = guarda
        self.requere_transicao = [6]

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(cenario_img, (0, 0))

        # Define a margem lateral
        margem = 50

        # Desenhar personagens
        tela.blit(self.personagem_imagem, (margem, TELA_ALT - self.personagem_imagem.get_height() - 50))
        tela.blit(self.rainha_imagem, (
            TELA_LARG - self.rainha_imagem.get_width() - margem, TELA_ALT - self.rainha_imagem.get_height() - 50))

        # Calcular posição do balão de fala
        max_texto_larg = 900
        texto_larg = min(max(len(text) for text in self.textos[self.indice_texto]) * 18, max_texto_larg)
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
            texto = font4.render(texto, True, PRETO)
            texto_ret = texto.get_rect(topleft=(x + 20, y + 20 + y_offset))
            tela.blit(texto, texto_ret)
            y_offset += 45

        if self.indice_texto == 6:
            texto2 = font4.render("Press -> to continue...", True, PRETO)
            texto2_ret = texto2.get_rect(center=(1100, 605))
            tela.blit(texto2, texto2_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Desafio5(TelaBase):
    def __init__(self):
        super().__init__()
        self.pergunta_atual = 0
        self.perguntas = [
            {
                "enunciado": "Complete as lacunas com as formas corretas para 'he', 'she' e 'it':",
                "pergunta": "He ___ the Queen.",
                "opcoes": ["1.protect", "2.protects", "3.like"],
                "resp_correta": 1
            },
            {
                "enunciado": "Complete as lacunas com as formas corretas para 'he', 'she' e 'it':",
                "pergunta": "She ___ the grass.",
                "opcoes": ["1.cuts", "2.cleans", "3.plays"],
                "resp_correta": 0
            },
            {
                "enunciado": "Complete as lacunas com as formas corretas para 'he', 'she' e 'it':",
                "pergunta": "The queen __ a crown!(curiosidade,To have(ter) vira 'HAS'!)",
                "opcoes": ["1.to have", "2.have", "3.has"],
                "resp_correta": 2
            },
            {
                "enunciado": "Transforme as frases afirmativas em frases negativas:",
                "pergunta": "He rules the kingdom",
                "opcoes": ["1.He don’t rules the kingdom.", "2.He doesn’t kingdom.", "3.He doesn’t rule the kingdom."],
                "resp_correta": 2
            },
            {
                "enunciado": "Transforme as frases afirmativas em frases negativas:",
                "pergunta": "It guards the gates.",
                "opcoes": ["1.It don’t guard!", "2.It doesn’t guard the gates.", "3.It guards doesn’t the gates."],
                "resp_correta": 1
            },
            {
                "enunciado": "Transforme as frases afirmativas em frases negativas:",
                "pergunta": "The queen __ a crown!",
                "opcoes": ["1.The queen doesn’t have a crown!", "2.The queen don’t has a crown!",
                           "3.The queen doesn’t has a crown!"],
                "resp_correta": 0
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "She admires the architecture.",
                "opcoes": ["1.Do she admire architecture?", "2.Does she admire the architecture?",
                           "3.Does she admires the architecture?"],
                "resp_correta": 1
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "The queen has a crown.",
                "opcoes": ["1.Does the queen have a crown?", "2.Does the queen has a crown?",
                           "3.Do queen haves a crown?"],
                "resp_correta": 0
            }
        ]
        self.personagem_imagem = garoto
        self.escolha_atual = None

    def update(self):
        pass

    def draw(self, tela):
        global tela_atual
        tela.blit(cenario_img, (0, 0))
        tela.blit(self.personagem_imagem, (50, TELA_ALT - self.personagem_imagem.get_height() - 50))

        if self.pergunta_atual < len(self.perguntas):
            num_opcoes = len(self.perguntas[self.pergunta_atual]["opcoes"])
            ret_pergunta_altura = num_opcoes * 80 + 160
            ret_pergunta_largura = 900
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
            tela_atual = cenario6

    def lidar_mouse_button_down_event(self, pos):
        pass

    def lidar_keydown_event(self, event):
        global tela_atual
        if event.key == pygame.K_1:
            self.escolha_atual = 0
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_2:
            self.escolha_atual = 1
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_3:
            self.escolha_atual = 2
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()

        self.pergunta_atual = (self.pergunta_atual + 1) % len(self.perguntas)

        if self.pergunta_atual == 0:
            tela_atual = cenario6


class Cenario6(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("Guard: Hey you!! STOP!!! Pare de incomodar a rainha e ",
             "venha comigo agora!"),
            ("Rainha: Calm down Guard! He is with me! This is John,",
             "e está aprendendo inglês aqui comigo, e agora está a ",
             "caminho de conhecer the wonderful city of London!"),
            ("Talvez, no caminho do portão você possa ensiná-lo ",
             "alguma coisa também! E depois guiá-lo para os melhores ",
             "destinos da cidade!"),
            ("Guard: Very good, young John!!! I am on it my Queen! So, ",
             "pelo visto você aprendeu muitas coisas com a rainha, e já que",
             "você vai sair cidade a fora, vou te ajudar a melhorar as suas ",
             "perguntas, para que você chegue aos seus destinos desejados!"),
            ("Vamos ver agora as 'WH questions', vou te apresentar ela e ",
             "você ira praticando em seguida!"),
            ("The first one is 'WHAT', podemos usar para: O que e Qual:",
             "Exemplo: 'What is your favorite color?' (Qual é a sua cor favorita?)"),
            ("The second is 'WHICH', usamos na maioria das vezes como qual e",
             "com exemplos sendo dado: 'Which do you prefer: cake or pizza?'",
             "(Qual você prefere: bolo ou pizza?)"),
            ("The next one is 'WHERE', que significa 'Onde e aonde'. ",
             "Ex: Where do you live? I live in Brazil!"),
            ("Same thing, mesma coisa para quando usarmos 'WHEN' que significa ",
             "'Quando'.")
        ]
        self.personagem_imagem = garoto
        self.rainha_imagem = rainha
        self.guarda_imagem = guarda
        self.requere_transicao = [8]

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(cenario_img, (0, 0))

        # Define a margem lateral
        margem = 50

        # Desenhar personagens
        tela.blit(self.personagem_imagem, (margem, TELA_ALT - self.personagem_imagem.get_height() - 50))
        tela.blit(self.guarda_imagem, (margem + 500, TELA_ALT - self.guarda_imagem.get_height() - 50))
        tela.blit(self.rainha_imagem, (
            TELA_LARG - self.rainha_imagem.get_width() - margem, TELA_ALT - self.rainha_imagem.get_height() - 50))

        # Calcular posição do balão de fala
        max_texto_larg = 1000
        texto_larg = min(max(len(text) for text in self.textos[self.indice_texto]) * 18, max_texto_larg)
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
            texto = font4.render(texto, True, PRETO)
            texto_ret = texto.get_rect(topleft=(x + 20, y + 20 + y_offset))
            tela.blit(texto, texto_ret)
            y_offset += 45

        if self.indice_texto == 8:
            texto2 = font4.render("Press -> to continue...", True, PRETO)
            texto2_ret = texto2.get_rect(center=(1100, 605))
            tela.blit(texto2, texto2_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Desafio6(TelaBase):
    def __init__(self):
        super().__init__()
        self.pergunta_atual = 0
        self.perguntas = [
            {
                "enunciado": "Qual seria a melhor opção para perguntar:",
                "pergunta": "'O que você gosta de comer?'",
                "opcoes": ["1.A-What is your name?   B- My name is Peter.", "2.A-What do you like to eat?   B- I like "
                                                                            "to eat fish and chips."],
                "resp_correta": 1
            },
            {
                "enunciado": "Qual é a pergunta para a seguinte resposta?",
                "pergunta": "B- They prefer to drink water.",
                "opcoes": ["1.A- Which do they prefer to drink: milk or water?", "2.A- Which does they prefer: milk "
                                                                                 "or water?"],
                "resp_correta": 0
            },
            {
                "enunciado": "Como você falaria:",
                "pergunta": "Olá, boa tarde. Onde voce come fish and chips em Londres?",
                "opcoes": ["1.Hello, good morning. Where do we eat fish and chips in London?", "2.Hello, good "
                                                                                               "afternoon. Where do "
                                                                                               "you eat fish and "
                                                                                               "chips in London?"],
                "resp_correta": 1
            }
        ]
        self.personagem_imagem = garoto
        self.escolha_atual = None

    def update(self):
        pass

    def draw(self, tela):
        global tela_atual
        tela.blit(cenario_img, (0, 0))
        tela.blit(self.personagem_imagem, (50, TELA_ALT - self.personagem_imagem.get_height() - 50))

        if self.pergunta_atual < len(self.perguntas):
            num_opcoes = len(self.perguntas[self.pergunta_atual]["opcoes"])
            ret_pergunta_altura = num_opcoes * 80 + 160
            ret_pergunta_largura = 900
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
            tela_atual = intro_desaf1

    def lidar_mouse_button_down_event(self, pos):
        pass

    def lidar_keydown_event(self, event):
        global tela_atual
        if event.key == pygame.K_1:
            self.escolha_atual = 0
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_2:
            self.escolha_atual = 1
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()

        self.pergunta_atual = (self.pergunta_atual + 1) % len(self.perguntas)

        if self.pergunta_atual == 0:
            tela_atual = intro_desaf1


class IntroDesaf1(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("Very good!! Now, para que você possa sair do castelo ",
             "precisa completar o THE BIG CHALLENGE! E se você passar ",
             "terá uma grande surpresa!",
             "Good Luck!!!!"),
            ("THE BIG CHALLENGE 1", "Press ENTER to continue..."),
        ]

        self.requere_transicao = [1]
        self.guarda_imagem = guarda

    def update(self):
        pass

    def draw(self, tela):
        tela.fill(PRETO)
        if self.indice_texto == 0:
            tela.blit(self.guarda_imagem, (1000, TELA_ALT - self.guarda_imagem.get_height() - 50))
            y = 50
            for texto1_ret in self.textos[self.indice_texto]:
                texto3 = font2.render(texto1_ret, True, BRANCA)
                texto3_ret = texto3.get_rect(center=(TELA_LARG // 2, y))
                tela.blit(texto3, texto3_ret)
                y += 50
        elif self.indice_texto == 1:
            texto1 = font5.render(self.textos[self.indice_texto][0], True, BRANCA)
            texto1_ret = texto1.get_rect(center=(TELA_LARG // 2, TELA_ALT // 2))
            tela.blit(texto1, texto1_ret)

            texto2 = font6.render(self.textos[self.indice_texto][1], True, BRANCA)
            texto2_ret = texto2.get_rect(center=(TELA_LARG // 2, 550))
            tela.blit(texto2, texto2_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class GD1(TelaBase):
    def __init__(self):
        super().__init__()
        self.pergunta_atual = 0
        self.perguntas = [
            {
                "enunciado": "Complete as lacunas com os pronomes corretos:",
                "pergunta": "___ am the Queen.",
                "opcoes": ["1.You", "2.I", "3.He"],
                "resp_correta": 1
            },
            {
                "enunciado": "Complete as lacunas com os pronomes corretos:",
                "pergunta": "___ explore the gardens.",
                "opcoes": ["1.She", "2.He", "3.They"],
                "resp_correta": 2
            },
            {
                "enunciado": "Complete as lacunas com os pronomes corretos:",
                "pergunta": "___ guard the gates.",
                "opcoes": ["1.The gardener", "2.The guards", "3.The Queen"],
                "resp_correta": 1
            },
            {
                "enunciado": "Transforme as frases afirmativas em negativas:",
                "pergunta": "I need to study English.",
                "opcoes": ["1.I don’t need to study English!", "2.I not need study English.",
                           "3.I not need to study English."],
                "resp_correta": 0
            },
            {
                "enunciado": "Transforme as frases afirmativas em negativas:",
                "pergunta": "She wants to visit the museum.",
                "opcoes": ["1.She don’t want to visit the museum.", "2.She don’t wants to visit the museum.",
                           "3.She doesn’t want to visit the museum."],
                "resp_correta": 2
            },
            {
                "enunciado": "Transforme as frases afirmativas em negativas:",
                "pergunta": "They want to eat pizza for dinner tonight.",
                "opcoes": ["1.They doesn’t want to eat pizza for dinner tonight.",
                           "2.They don’t want to eat pizza for dinner tonight.",
                           "3.They don’t to want eat pizza for dinner tonight."],
                "resp_correta": 1
            },
            {
                "enunciado": "Transforme as frases afirmativas em negativas:",
                "pergunta": "He loves to eat Fish and Chips.",
                "opcoes": ["1.He don’t loves to eat Fish and Chips", "2.He doesn’t loves eat Fish and Chips",
                           "3.He doesn’t love to eat Fish and Chips"],
                "resp_correta": 2
            },
            {
                "enunciado": "Transforme as frases afirmativas em negativas:",
                "pergunta": "It is important to drink water. (to drink = beber)",
                "opcoes": ["1.It is not important to drink water.", "2.It doesn’t is not important to drink water",
                           "3.It not important to drink water"],
                "resp_correta": 0
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "She admires the history of London.",
                "opcoes": ["1.Does she admire the history of London?", "2.Do she admires the history of London?",
                           "3.Does she admires to history of London?"],
                "resp_correta": 0
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "He drinks a lot of coffee. (a lot = Muito)",
                "opcoes": ["1.Does he drinks a lot of coffee?", "2.Does he drink a lot of coffee?",
                           "3.Do he drinks a lot of coffee?"],
                "resp_correta": 1
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "They protect the entrance to the palace.",
                "opcoes": ["1.Do they to protects the entrance to the palace?",
                           "2.Does they protect the entrance to the palace?",
                           "3.Do they protect the entrance to the palace?"],
                "resp_correta": 2
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "The queen has an expensive crown. (expensive = caro/cara)",
                "opcoes": ["1.Do queen has an expensive crown?", "2.Does the queen have an expensive crown?",
                           "3.Does the queen has an expensive crown?"],
                "resp_correta": 1
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "We love to dance at the park.",
                "opcoes": ["1.Do we love to dance at the park?", "2.Does we love to dance at the park?",
                           "3.Do we love dance at park?"],
                "resp_correta": 0
            },
            {
                "enunciado": "Responda a seguinte pergunta:",
                "pergunta": "What is the typical British food?",
                "opcoes": ["1.Pizza", "2.Mashed Potatoes", "3.Fish and chips"],
                "resp_correta": 2
            },
            {
                "enunciado": "Qual pergunta com 'Which' faz mais sentido?",
                "pergunta": "*de acordo com o que você aprendeu",
                "opcoes": ["1.Which do you like: cookies?", "2.Which do you prefer: cookies or chocolate?",
                           "3.Which do you want to go to London?"],
                "resp_correta": 1
            },
            {
                "enunciado": "Selecione a resposta que melhor responde a seguinte pergunta:",
                "pergunta": "When do you want to go to London? (to go = ir)",
                "opcoes": ["1.I to go to London tomorrow", "2.I want go to Paris tomorrow.",
                           "3.I want to go to London next week."],
                "resp_correta": 2
            },
            {
                "enunciado": "Qual é a tradução das seguintes frases?",
                "pergunta": "O que ela gosta de comer em Londres?",
                "opcoes": ["1.What does she like to eat in London?", "2.What do she like to drink in London?",
                           "3.Which does she like eat in London?"],
                "resp_correta": 0
            },
            {
                "enunciado": "Qual é a tradução das seguintes frases?",
                "pergunta": "Quando ele quer ver o Big Ben?",
                "opcoes": ["1.Where does he want to see the Big Ben?", "2.When does he want to see the Big Ben?",
                           "3.When does he need to see the Big Ben?"],
                "resp_correta": 1
            },
            {
                "enunciado": "Qual é a tradução das seguintes frases?",
                "pergunta": "Ela tem 2 coroas e um castelo.",
                "opcoes": ["1.She has one crowns and two castle.", "2.She doesn’t have two crowns and one castle.",
                           "3.She has two crowns and one castle."],
                "resp_correta": 2
            }
        ]
        self.personagem_imagem = garoto
        self.escolha_atual = None

    def update(self):
        pass

    def draw(self, tela):
        global tela_atual
        tela.blit(cenario_img, (0, 0))
        tela.blit(self.personagem_imagem, (50, TELA_ALT - self.personagem_imagem.get_height() - 50))

        if self.pergunta_atual < len(self.perguntas):
            num_opcoes = len(self.perguntas[self.pergunta_atual]["opcoes"])
            ret_pergunta_altura = num_opcoes * 80 + 160
            ret_pergunta_largura = 900
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
            tela_atual = final1

    def lidar_mouse_button_down_event(self, pos):
        pass

    def lidar_keydown_event(self, event):
        global tela_atual
        if event.key == pygame.K_1:
            self.escolha_atual = 0
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_2:
            self.escolha_atual = 1
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_3:
            self.escolha_atual = 2
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()

        self.pergunta_atual = (self.pergunta_atual + 1) % len(self.perguntas)

        if self.pergunta_atual == 0:
            tela_atual = final1


class Final1(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("Rainha Elizabeth: Parabéns John, você concluiu a primeira parte",
             "de sua jornada com excelência, continue assim e termine a sua viagem",
             "por Londres. Guard, please! Acompanhe o jovem viajante até a saída!"),
            ("Guard: Assim como prometido young traveler, você terá uma surpresa!",
             "Não vou te revelar agora, porém se você pegar o subway, o metrô,",
             "vá até King’s Cross, e entre as plataformas 9 e 10, meu amigo irá te",
             "receber o te acompanhar para o restante da sua jornada!")
        ]
        self.personagem_imagem = garoto
        self.rainha_imagem = rainha
        self.guarda_imagem = guarda
        self.requere_transicao = [1]

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(cenario_img, (0, 0))

        # Define a margem lateral
        margem = 50

        # Desenhar personagens
        tela.blit(self.personagem_imagem, (margem, TELA_ALT - self.personagem_imagem.get_height() - 50))
        tela.blit(self.guarda_imagem, (margem + 500, TELA_ALT - self.guarda_imagem.get_height() - 50))
        tela.blit(self.rainha_imagem, (
            TELA_LARG - self.rainha_imagem.get_width() - margem, TELA_ALT - self.rainha_imagem.get_height() - 50))

        # Calcular posição do balão de fala
        max_texto_larg = 900
        texto_larg = min(max(len(text) for text in self.textos[self.indice_texto]) * 18, max_texto_larg)
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
            texto = font4.render(texto, True, PRETO)
            texto_ret = texto.get_rect(topleft=(x + 20, y + 20 + y_offset))
            tela.blit(texto, texto_ret)
            y_offset += 45

        if self.indice_texto == 1:
            texto2 = font4.render("Press -> to continue...", True, PRETO)
            texto2_ret = texto2.get_rect(center=(1100, 605))
            tela.blit(texto2, texto2_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Fase2(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("PHASE 2", "Press SPACE to continue..."),
        ]

    def update(self):
        pass

    def draw(self, tela):
        tela.fill(PRETO)
        if self.indice_texto == 0:
            texto1 = font5.render(self.textos[self.indice_texto][0], True, BRANCA)
            texto1_ret = texto1.get_rect(center=(TELA_LARG // 2, TELA_ALT // 2))
            tela.blit(texto1, texto1_ret)

            texto2 = font6.render(self.textos[self.indice_texto][1], True, BRANCA)
            texto2_ret = texto2.get_rect(center=(TELA_LARG // 2, 550))
            tela.blit(texto2, texto2_ret)


class IntroF2(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("Bem-vindo a King's Cross, ela é dos principais cenários",
             "de Harry Potter, afinal, é nela que Harry e outros jovens",
             "bruxos embarcam no Expresso de Hogwarts e viajam para ",
             "Escola de Magia e Bruxaria, Hogwarts."),
            ("Ao visitar a famosa Plataforma 9¾ você se depara com um",
             "jovem em vestimentas pretas e longas parado em frente a ",
             "plataforma como se esperasse alguém chegar, então você",
             "decide ir falar com ele para pedir informações.")
        ]
        self.personagem_imagem = garoto
        self.harry_imagem = harrypotter
        self.requere_transicao = [1]

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(hogwarts, (0, 0))

        # Define a margem lateral
        margem = 50

        # Calcular posição do balão de fala
        max_texto_larg = 1000
        texto_larg = min(max(len(text) for text in self.textos[self.indice_texto]) * 18, max_texto_larg)
        texto_alt = len(self.textos[self.indice_texto]) * 55
        x = margem + self.personagem_imagem.get_width() + (
                TELA_LARG - 2 * margem - self.personagem_imagem.get_width() -
                self.harry_imagem.get_width() - texto_larg) // 2
        y = TELA_ALT - self.harry_imagem.get_height() - texto_alt - 80

        # Desenhar balão de fala
        pygame.draw.rect(tela, PRETO, (x - 5, y - 5, texto_larg + 10, texto_alt + 10), border_radius=25)
        pygame.draw.rect(tela, BRANCA, (x, y, texto_larg, texto_alt), border_radius=25)

        # Desenhar texto no balão de fala
        y_offset = 0
        for texto in self.textos[self.indice_texto]:
            texto = font4.render(texto, True, PRETO)
            texto_ret = texto.get_rect(topleft=(x + 20, y + 20 + y_offset))
            tela.blit(texto, texto_ret)
            y_offset += 45

        if self.indice_texto == 1:
            texto2 = font4.render("Press -> to continue...", True, BRANCA)
            texto2_ret = texto2.get_rect(center=(1100, 605))
            tela.blit(texto2, texto2_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Cenario7(TelaBase):
    def __init__(self):
        super().__init__()
        self.indice_texto = 0
        self.textos = [
            ("Hello John, você deve estar curioso sobre como eu sei o seu nome certo?",
             "I am Harry Potter, and my friend, the guard me disse que alguém aqui",
             "precisaria da minha ajuda e então fui designado pela associação de bruxo",
             "de Hogwarts para ajudá-lo na segunda parte da sua jornada por Londres."),
            ("This is the King's Cross Station! The train station que usamos para ir ",
             "para hogwarts and I am very excited to teach you the 'present continuous'.",
             "É uma parte essencial do inglês que usamos para descrever ações que estão",
             "acontecendo no momento. Por exemplo:"),
            ("'I am flying on a broomstick' (Eu estou voando em uma vassoura)",
             "Agora, vamos ver como formar o 'present continuous'. Primeiro, usamos o",
             "verbo 'to be' no presente (am, are, is) e depois adicionamos o 'ing' na",
             "ação. Por exemplo:"),
            ("•I am reading a book. (Eu estou lendo um livro.)",
             "•You are listening to music. (Você está ouvindo música.)",
             "•He is studying for exams. (Ele está estudando para os exames.)",
             "•She is playing Quidditch. (Ela está jogando Quadribol.)",
             "•It is raining outside. (Está chovendo lá fora.)"),
            ("•We are waiting for the train. (Nós estamos esperando pelo trem.)",
             "•They are talking about their plans. (Eles estão conversando",
             "sobre seus planos.)"),
            ("Se eu quisesse falar a frase negativa dessas anteriores, é só colocar o",
             "'NOT' entre o 'to be' e a ação+ing. Por exemplo:",
             "'You are NOT listening to music' (Você não está ouvindo música)."),
            ("E se eu quiser pergutar se alguém está fazendo algo ou não?",
             "Invertemos o verb to be e a pessoa da frase, e colocamos '?' no final.",
             "Simples assim: 'ARE you listening to music?' (Você está ouvindo música?)",
             "Agora, vamos para um desafio para praticar o que aprendemos até agora!")
        ]
        self.personagem_imagem = garoto
        self.harry_imagem = harrypotter
        self.requere_transicao = [6]

    def update(self):
        pass

    def draw(self, tela):
        tela.blit(hogwarts, (0, 0))

        # Define a margem lateral
        margem = 50

        # Desenhar personagens
        tela.blit(self.personagem_imagem, (margem, TELA_ALT - self.personagem_imagem.get_height() - 50))
        tela.blit(self.harry_imagem, (
            TELA_LARG - self.harry_imagem.get_width() - margem, TELA_ALT - self.harry_imagem.get_height() - 50))

        # Calcular posição do balão de fala
        max_texto_larg = 850
        texto_larg = min(max(len(text) for text in self.textos[self.indice_texto]) * 18, max_texto_larg)
        texto_alt = len(self.textos[self.indice_texto]) * 55
        x = margem + self.personagem_imagem.get_width() + (
                TELA_LARG - 2 * margem - self.personagem_imagem.get_width() -
                self.harry_imagem.get_width() - texto_larg) // 2
        y = TELA_ALT - self.harry_imagem.get_height() - texto_alt - 80

        # Desenhar balão de fala
        pygame.draw.rect(tela, PRETO, (x - 5, y - 5, texto_larg + 10, texto_alt + 10), border_radius=25)
        pygame.draw.rect(tela, BRANCA, (x, y, texto_larg, texto_alt), border_radius=25)

        # Desenhar texto no balão de fala
        y_offset = 0
        for texto in self.textos[self.indice_texto]:
            texto = font4.render(texto, True, PRETO)
            texto_ret = texto.get_rect(topleft=(x + 20, y + 20 + y_offset))
            tela.blit(texto, texto_ret)
            y_offset += 45

        if self.indice_texto == 6:
            texto2 = font4.render("Press -> to continue...", True, BRANCA)
            texto2_ret = texto2.get_rect(center=(1100, 605))
            tela.blit(texto2, texto2_ret)

    def change_text(self):
        if self.indice_texto in self.requere_transicao:
            return
        self.indice_texto = (self.indice_texto + 1) % len(self.textos)


class Desafio7(TelaBase):
    def __init__(self):
        super().__init__()
        self.pergunta_atual = 0
        self.perguntas = [
            {
                "enunciado": "Complete as lacunas com as formas corretas do 'present continuous':",
                "pergunta": "I ___ (watch) a movie.",
                "opcoes": ["1.am watching", "2.is watching", "3.are watching"],
                "resp_correta": 0
            },
            {
                "enunciado": "Complete as lacunas com as formas corretas do 'present continuous':",
                "pergunta": "We ___ (study) for the test.",
                "opcoes": ["1.is studying", "2.am studying", "3.are studying"],
                "resp_correta": 2
            },
            {
                "enunciado": "Complete as lacunas com as formas corretas do 'present continuous':",
                "pergunta": "He ___ (play) video games.",
                "opcoes": ["1.am playing", "2.is playing", "3.are playing"],
                "resp_correta": 1
            },
            {
                "enunciado": "Transforme as frases afirmativas em negativas:",
                "pergunta": "She is dancing in the living room.",
                "opcoes": ["1.She is not dancing in the living room.", "2.She are not dancing in the living room.",
                           "3.She not dancing in the living room."],
                "resp_correta": 0
            },
            {
                "enunciado": "Transforme as frases afirmativas em negativas:",
                "pergunta": "It is raining in London.",
                "opcoes": ["1.Not is raining in London", "2.It is not rain in London", "3.It is not raining in London"],
                "resp_correta": 2
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "You are planning a trip.",
                "opcoes": ["1.Am you planning a trip?", "2.Are you planning a trip?", "3.Is you planning a trip?"],
                "resp_correta": 1
            },
            {
                "enunciado": "Forme perguntas com as frases dadas:",
                "pergunta": "He is playing video games.",
                "opcoes": ["1.Does he play video games?", "2.Is she playing video games?",
                           "3.Is he playing video games?"],
                "resp_correta": 2
            }

        ]
        self.personagem_imagem = garoto
        self.escolha_atual = None

    def update(self):
        pass

    def draw(self, tela):
        global tela_atual
        tela.blit(hogwarts, (0, 0))
        tela.blit(self.personagem_imagem, (50, TELA_ALT - self.personagem_imagem.get_height() - 50))

        if self.pergunta_atual < len(self.perguntas):
            num_opcoes = len(self.perguntas[self.pergunta_atual]["opcoes"])
            ret_pergunta_altura = num_opcoes * 80 + 160
            ret_pergunta_largura = 900
            pergunta_ret_x = (TELA_LARG - ret_pergunta_largura) // 2
            pergunta_ret_y = (TELA_ALT - ret_pergunta_altura) // 2

            superficie_transparente = pygame.Surface((ret_pergunta_largura, ret_pergunta_altura), pygame.SRCALPHA)
            superficie_transparente.fill((0, 0, 0, 128))
            tela.blit(superficie_transparente, (pergunta_ret_x, pergunta_ret_y))

            enunciado_texto = font2.render(self.perguntas[self.pergunta_atual]["enunciado"], True, BRANCA)
            tela.blit(enunciado_texto, (pergunta_ret_x + 20, pergunta_ret_y + 20))

            pergunta_texto = font2.render(self.perguntas[self.pergunta_atual]["pergunta"], True, BRANCA)
            tela.blit(pergunta_texto, (pergunta_ret_x + 20, pergunta_ret_y + 60))

            y = pergunta_ret_y + 120
            for indice, opcao in enumerate(self.perguntas[self.pergunta_atual]["opcoes"]):
                opcao_texto = font2.render(opcao, True, BRANCA)
                tela.blit(opcao_texto, (pergunta_ret_x + 40, y))
                y += 80
        else:
            tela_atual = menu_principal

    def lidar_mouse_button_down_event(self, pos):
        pass

    def lidar_keydown_event(self, event):
        global tela_atual
        if event.key == pygame.K_1:
            self.escolha_atual = 0
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_2:
            self.escolha_atual = 1
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        elif event.key == pygame.K_3:
            self.escolha_atual = 2
            if self.escolha_atual != self.perguntas[self.pergunta_atual]["resp_correta"]:
                vidas.perder_vida()
        self.pergunta_atual = (self.pergunta_atual + 1) % len(self.perguntas)

        if self.pergunta_atual == 0:
            tela_atual = menu_principal


vidas = Vidas()
menu_principal = MenuPrincipal()
tela_intro1 = TelaIntro1()
tela_creditos = TelaCreditos()
cenario1 = Cenario1()
desafio1 = Desafio1()
cenario2 = Cenario2()
desafio2 = Desafio2()
cenario3 = Cenario3()
desafio3 = Desafio3()
cenario4 = Cenario4()
desafio4 = Desafio4()
cenario5 = Cenario5()
desafio5 = Desafio5()
cenario6 = Cenario6()
desafio6 = Desafio6()
intro_desaf1 = IntroDesaf1()
grande_desafio1 = GD1()
final1 = Final1()
fase2 = Fase2()
introf2 = IntroF2()
cenario7 = Cenario7()
desafio7 = Desafio7()
falhou = Falhou()
tela_atual = menu_principal


def main():
    global tela_atual

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if tela_atual == menu_principal:
                    if menu_principal.botao_start.is_clicked(pygame.mouse.get_pos()):
                        tela_atual = tela_intro1
                    elif menu_principal.botao_credito.is_clicked(pygame.mouse.get_pos()):
                        tela_atual = tela_creditos
                if tela_atual == tela_creditos:
                    if tela_creditos.voltar_butao.is_clicked(pygame.mouse.get_pos()):
                        tela_atual = menu_principal
            elif event.type == pygame.KEYDOWN:
                if tela_atual == tela_intro1:
                    if event.key == pygame.K_SPACE:
                        tela_intro1.change_text()
                    elif event.key == pygame.K_RIGHT:
                        if tela_intro1.indice_texto in tela_intro1.requere_transicao:
                            tela_atual = cenario1
                elif tela_atual == cenario1:
                    if event.key == pygame.K_SPACE:
                        cenario1.change_text()
                    if event.key == pygame.K_RIGHT:
                        if cenario1.indice_texto in cenario1.requere_transicao:
                            tela_atual = desafio1
                elif tela_atual == desafio1:
                    if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                        desafio1.lidar_keydown_event(event)
                elif tela_atual == cenario2:
                    if event.key == pygame.K_SPACE:
                        cenario2.change_text()
                    if event.key == pygame.K_RIGHT:
                        if cenario2.indice_texto in cenario2.requere_transicao:
                            tela_atual = desafio2
                elif tela_atual == desafio2:
                    if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                        desafio2.lidar_keydown_event(event)
                elif tela_atual == cenario3:
                    if event.key == pygame.K_SPACE:
                        cenario3.change_text()
                    if event.key == pygame.K_RIGHT:
                        if cenario3.indice_texto in cenario3.requere_transicao:
                            tela_atual = desafio3
                elif tela_atual == desafio3:
                    if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                        desafio3.lidar_keydown_event(event)
                elif tela_atual == cenario4:
                    if event.key == pygame.K_SPACE:
                        cenario4.change_text()
                    if event.key == pygame.K_RIGHT:
                        if cenario4.indice_texto in cenario4.requere_transicao:
                            tela_atual = desafio4
                elif tela_atual == desafio4:
                    if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                        desafio4.lidar_keydown_event(event)
                elif tela_atual == cenario5:
                    if event.key == pygame.K_SPACE:
                        cenario5.change_text()
                    if event.key == pygame.K_RIGHT:
                        if cenario5.indice_texto in cenario5.requere_transicao:
                            tela_atual = desafio5
                elif tela_atual == desafio5:
                    if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                        desafio5.lidar_keydown_event(event)
                elif tela_atual == cenario6:
                    if event.key == pygame.K_SPACE:
                        cenario6.change_text()
                    if event.key == pygame.K_RIGHT:
                        if cenario6.indice_texto in cenario6.requere_transicao:
                            tela_atual = desafio6
                elif tela_atual == desafio6:
                    if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                        desafio6.lidar_keydown_event(event)
                elif tela_atual == intro_desaf1:
                    if event.key == pygame.K_SPACE:
                        intro_desaf1.change_text()
                    elif event.key == pygame.K_RETURN:
                        tela_atual = grande_desafio1
                elif tela_atual == grande_desafio1:
                    if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                        grande_desafio1.lidar_keydown_event(event)
                elif tela_atual == final1:
                    if event.key == pygame.K_SPACE:
                        final1.change_text()
                    if event.key == pygame.K_RIGHT:
                        if final1.indice_texto in final1.requere_transicao:
                            tela_atual = fase2
                elif tela_atual == falhou:
                    if event.key == pygame.K_RETURN:
                        tela_atual = menu_principal
                elif tela_atual == fase2:
                    if event.key == pygame.K_SPACE:
                        tela_atual = introf2
                elif tela_atual == introf2:
                    if event.key == pygame.K_SPACE:
                        introf2.change_text()
                    if event.key == pygame.K_RIGHT:
                        if introf2.indice_texto in introf2.requere_transicao:
                            tela_atual = cenario7
                elif tela_atual == cenario7:
                    if event.key == pygame.K_SPACE:
                        cenario7.change_text()
                    if event.key == pygame.K_RIGHT:
                        if cenario7.indice_texto in cenario7.requere_transicao:
                            tela_atual = desafio7
                elif tela_atual == desafio7:
                    if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                        desafio7.lidar_keydown_event(event)
        tela.fill(PRETO)
        tela_atual.draw(tela)
        vidas.draw(tela)
        pygame.display.flip()


if __name__ == "__main__":
    main()
