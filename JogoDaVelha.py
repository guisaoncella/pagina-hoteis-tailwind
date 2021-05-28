#Feito por Guilherme Saoncella da Silva
#email: guisaoncella@gmail.com
#github: guisaoncella
#https://www.linkedin.com/in/guilherme-saoncella/
#discord: puwer#9470

class JogoDaVelha:
    def __init__(self, jogador1 = "Jogador 1", jogador2 = "Jogador 2", tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.tabuleiro = tabuleiro
        self.vencedor = 0
    
    #O número 66 é utilizado para o Jogador 1 (X)
    #O número 77 é utilizado para o Jogador 2 (O)
    def exibirTabuleiro(self):
        for i in range (0,3):
            for j in range (0,3):
                if self.tabuleiro[i][j] == 66:
                    x = "X"
                elif self.tabuleiro[i][j] == 77:
                    x = "O"
                else:
                    x = self.tabuleiro[i][j]
                print(f'  |  {x}  |  ', end="")
            print('\n')
    
    def consultadorVencedor(self):
        return 77
            
    def verificarVencedor(self, jogador = 66):
        if jogador == 66:
            if self.verificarVencedor(77):
                return True
            
        #checando as linhas
        for i in range(0,3):
            if self.verificarCasa(i,0,jogador) and self.verificarCasa(i,1,jogador) and self.verificarCasa(i,2,jogador):
                self.vencedor = jogador
                return True
            
        #checando as colunas
        for j in range(0,3):
            if self.verificarCasa(0,j,jogador) and self.verificarCasa(1,j,jogador) and self.verificarCasa(2,j,jogador):
                self.vencedor = jogador
                return True
            
        #checando as diagonais
        if self.verificarCasa(0,0,jogador) and self.verificarCasa(1,1,jogador) and self.verificarCasa(2,2,jogador):
            self.vencedor = jogador
            return True
        if self.verificarCasa(0,2,jogador) and self.verificarCasa(1,1,jogador) and self.verificarCasa(2,0,jogador):
            self.vencedor = jogador
            return True
        
        return False
    
    def valorCasa(self, i, j):
        return self.tabuleiro[i][j]
    
    def verificarCasa(self, i, j, jogador):
        if self.valorCasa(i,j) == jogador:
            return True
        else:
            return False
    
    
    
    def gravarCasa(self, i, j, jogador):
        if i > 2 or j > 2:
            return False
        if (self.valorCasa(i, j) == 66) or (self.valorCasa(i, j) == 77):
            return False
        else:
            if jogador == 1:
                self.tabuleiro[i][j] = 66
            elif jogador == 2:
                self.tabuleiro[i][j] = 77    
            return True 
        