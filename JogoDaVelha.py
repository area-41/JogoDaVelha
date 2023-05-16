# -*- coding: utf-8 -*-
from random import random


class Tabuleiro:
    def __init__(self):
        # Inicializa todas as posições com ' '
        self._posicoes = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

    def imprime(self):
        # Imprime letras das colunas
        print('\n |A|B|C')
        for cont, linha in enumerate(self._posicoes):
            # Imprime número e posições da linha
            print('--------')
            print(cont + 1, '|' + '|'.join(linha), sep='')

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


class Velha:

    def __init__(self):
        # Inicializa tabuleiro
        self._tabuleiro = Tabuleiro()
        # Sorteia jogador
        if random() >= 0.5:
            self._jogador = 'X'
        else:
            self._jogador = 'O'

    def imprime(self):
        # Mostra o estado do jogo
        print('\n'*50)
        print('Jogo da velha\n')
        self._tabuleiro.imprime()

    def troca_jogador(self):
        # Troca o jogador
        if self._jogador == 'X':
            self._jogador = 'O'
        else:
            self._jogador = 'X'

    def pega_jogada(self):
        # Laço infinito para o caso de jogadas inválidas
        while True:
            # Mostra o tabuleiro
            self.imprime()
            # Mostra o jogador que está jogando
            print('\nJogador', self._jogador)
            # Pega linha e coluna da jogada
            posicao = input('Informe a jogada: ')
            # Tenta executar a jogada no tabuleiro
            if self._tabuleiro.jogada(posicao, self._jogador):
                # Se a jogada for válida, interrompe o laço
                break

    def eh_vencedor(self, jogador):
        # Testa se um jogador é vencedor
        linhas = self._tabuleiro.todas_linhas()
        # O Jogador é vencedor ter tiver uma linha com 3 posições
        if tuple([jogador] * 3) in linhas:
            return True
        return False

    def jogar(self):
        # Repete enquanto hoverem jogadas possíveis
        while self._tabuleiro.tem_jogada():
            # Motra o estado do jogo
            self.imprime()
            # Pega a jogada
            self.pega_jogada()
            # Testa se o jogador venceu
            if self.eh_vencedor(self._jogador):
                self.imprime()
                print('\nFim de jogo!')
                print('Vitória do jogador', self._jogador)
                # Finaliza se tiver um vencedor
                return
            # Troca de jogador
            self.troca_jogador()
        # Se terminarem as jogadas, o jogo fica empatado
        self.imprime()
        print('\nJogo empatado!')


if __name__ == '__main__':
    jogo = Velha()
    jogo.jogar()
