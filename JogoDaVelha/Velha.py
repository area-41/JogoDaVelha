#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Tabuleiro import *
from random import random


class Velha:
    linha = '-' * 50
    titulo = 'Jogo da Veia !!!'

    def __init__(self):
        # Inicializa tabuleiro
        print(Velha.linha)
        print(Velha.titulo.center(50))
        self._tabuleiro = Tabuleiro()
        # Sorteia jogador
        if random() >= 0.5:
            self._jogador = 'X'
        else:
            self._jogador = 'O'

    def imprime(self):
        # Mostrar o estado do jogo
        #print('\n'*50)
        print('-'*50)
        #print('Jogo da Veia')
        self._tabuleiro.imprime()

    def troca_jogador(self):
        # Trocar o jogador
        if self._jogador == 'X':
            self._jogador = 'O'
        else:
            self._jogador = 'X'

    def pega_jogada(self):
        # Laço infinito para o caso de jogadas inválidas
        while True:
            # Mostrar o tabuleiro
            self.imprime()
            # Mostrar o jogador que está jogando
            print('\nVez do Jogador: ', self._jogador)
            # Pegar linha e coluna da jogada
            posicao = input('Informe a jogada: ')
            # Tentar executar a jogada no tabuleiro
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
        # Repetir enquanto houver jogadas possíveis
        while self._tabuleiro.tem_jogada():
            # Mostra o estado do jogo
            #self.imprime()
            # Pegar a jogada
            self.pega_jogada()
            # Testar se o jogador venceu
            if self.eh_vencedor(self._jogador):
                self.imprime()
                print('\nFim de jogo!')
                print('Vitória do jogador ->', self._jogador, ' !!!!')
                # Finalizar se tiver um vencedor
                return
            # Trocar de jogador
            self.troca_jogador()
        # Se terminarem as jogadas, o jogo fica empatado
        self.imprime()
        print('\nJogo empatado!')
