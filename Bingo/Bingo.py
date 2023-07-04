#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import shuffle
from time import sleep


class Jogador:

    def __init__(self, nome, numeros):
        # Nome do jogador
        self._nome = nome
        # Conjunto de números já marcados
        self._marcados = set()
        # Conjunto com todos os números do jogador
        self._numeros = set(numeros)

    @property
    def nome(self):
        return self._nome

    def marca(self, numero):
        # Testa se o jogador possui o número
        if numero in self._numeros:
            # Adiciona o número aos marcados
            self._marcados.add(numero)

    def faltantes(self):
        # Todos os números menos os números marcados
        return self._numeros - self._marcados

    def imprime(self):
        # Lista com números faltantes
        faltantes = list(self.faltantes())
        # Ordena a lista
        faltantes.sort()
        # Converte números para str
        faltantes_str = [str(n) for n in faltantes]
        # Imprime nome e números faltantes do jogador
        print(self._nome + ':', ' '.join(faltantes_str))


class Bingo:

    def __init__(self, total_numeros):
        # Cria lista de todos os números do jogo
        lista_numeros = list(range(1, total_numeros-1))
        # Lista de números sorteados
        self._sorteados = []
        # Lista de jogadores
        self._jogadores = []
        # Lista de vencedores
        self._vencedores = []
        # Embaralha a lista de números
        shuffle(lista_numeros)
        # Armazena a lista de números como atributo
        self._numeros = lista_numeros

    def adiciona_jogador(self, nome):
        # Copia a lista de números
        lista_numeros = self._numeros[:]
        # Embaralha a lista de números
        shuffle(lista_numeros)
        # Calcula a quantidade de números do jogador (30% to total)
        quantidade_numeros = int(len(lista_numeros)*0.3)
        # Pega apenas a quantidade de números do jogador
        numeros = lista_numeros[:quantidade_numeros]
        # Cria o jogador
        jogador = Jogador(nome, numeros)
        # Adiciona o jogador à lista de jogadores
        self._jogadores.append(jogador)

    def imprime(self):
        # Mostra o estado do jogo
        print('\n'*50)
        print('BINGO\n')
        # Mostra números sorteados
        sorteados = [str(n) for n in self._sorteados]
        print('Sorteados:', ' '.join(sorteados), '\n')
        # Mostra cada jogador
        for jogador in self._jogadores:
            jogador.imprime()

    def sorteia(self):
        # O número sorteado é o último da lista (já embaralhada)
        numero = self._numeros.pop()
        # Adiciona o número aos sorteados
        self._sorteados.append(numero)
        # Percorre a lista d ejogadores
        for jogador in self._jogadores:
            # Marca o número para o jogador
            jogador.marca(numero)
            # Testa se o jogador já marcou todos os números
            if len(jogador.faltantes()) == 0:
                # Adicionar o jogador à lista de vencedores
                self._vencedores.append(jogador)

    def jogar(self):
        # Testa se existem jogadores
        if len(self._jogadores) > 0:
            # Repete até que hajam vencedores
            while not self._vencedores:
                # Mostra o estado do jogo
                self.imprime()
                # input() apenas para o usuário pressionar ENTER
                input('Pressione ENTER para sortear um número.')
                # Sorteia um número
                self.sorteia()
                # Mostra o resultado final do jogo
                self.imprime()
                # Mostra os vencedores
                print('\nVencedor(res):')
                for jogador in self._vencedores:
                    print(jogador.nome)
                    sleep(5)
                    print("\n\nFim de Jogo! Obrigado")


if __name__ == '__main__':
    # Inicia o jogo com 10 números
    bingo = Bingo(10)
    print('Iniciando o jogo')
    print('Informe os nomes dos jogadores (vazio para parar)')
    # Laço para adicionar os jogadores
    cont = 1
    while cont <= 3:
        # Pega o nome do jogador
        nome = input('Jogador '+str(cont) + ': ')
        cont += 1
        # Se o nome estiver em branco, interrompe o laço
        if nome.strip() == '':
            break
        # Adiciona o jogador ao jogo
        bingo.adiciona_jogador(nome)
    # Inicia o jogo
    bingo.jogar()
