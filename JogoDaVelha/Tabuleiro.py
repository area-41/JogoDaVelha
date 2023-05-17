# -*- coding: utf-8 -*-

class Tabuleiro:
    def __init__(self):
        # Inicializa todas as posições com ' '
        self._posicoes = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

    def imprime(self):
        # Imprime letras das colunas
        print('\n  A:B:C')
        for cont, linha in enumerate(self._posicoes):
            # Imprime número e posições da linha
            print('--------')
            print(cont + 1, ':' + '|'.join(linha), sep='')

    def jogada(self, posicao, simbolo):
        # Tratamento de exceções para erros de digitação
        try:
            # A linha é o primeiro caractere digitado
            linha = int(posicao[0]) - 1
            # A coluna é o segunda caractere (letra)
            letra = posicao[1].upper()
            # Converte letra para número
            coluna = ord(letra) - ord('A')
            # Verifica se a posição está vazia
            if self._posicoes[linha][coluna] == ' ':
                # Marca a posição com o simbolo do jogador
                self._posicoes[linha][coluna] = simbolo
                return True
        except:
            # Em caso de erro, nenhuma posição é marcada
            pass
        return False

    def tem_jogada(self):
        # Varre o tabuleiro procurando por posições vazias
        for linha in self._posicoes:
            if ' ' in linha:
                return True
        return False

    def todas_linhas(self):
        # Retorna todas as linhas possiveis em formato de tuplas
        # Linhas, colunas, diagonal e transversal
        todas = []
        # Linhas
        for linha in self._posicoes:
            todas.append(tuple(linha))
        # Colunas
        for cont in range(3):
            coluna = [self._posicoes[0][cont],
                      self._posicoes[1][cont],
                      self._posicoes[2][cont]]
            todas.append(tuple(coluna))
        # Diagonal e transversal
        diagonal = []
        transversal = []
        for cont in range(3):
            diagonal.append(self._posicoes[cont][cont])
            transversal.append(self._posicoes[2 - cont][cont])
        todas.append(tuple(diagonal))
        todas.append(tuple(transversal))
        return todas
