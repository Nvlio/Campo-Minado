import random

class Campo_Minado():
    def __init__(self,dificuldade = "Normal"):
        self._dificuldade = dificuldade.capitalize()
        self._TabelaPublica = []
        self._Tabela_Minada = []
        self._bombas=0

    #metodo que monta as tabelas
    def Montar(self,coluna,linha):
        try:
            print('montando')
            for c in range(0,coluna):
                    self._TabelaPublica.append([])
                    self._Tabela_Minada.append([])
                    for l in range(0,linha):
                        self._TabelaPublica[c].append(" ")
                        self._Tabela_Minada[c].append(" ")
            return True
        except:
            print("erro ocorreu no metodo 'Montagem de tabelas'")

    #Metodo que prepara e define as variaveis de acordo com a dificuldade escolhida
    def Preparar(self):
        try:
            print('preparando')
            if self._dificuldade == "Facil":
                    coluna = 8
                    linha = 10
                    self._bombas = 24

            elif self._dificuldade == "Normal":
                    coluna = 16
                    linha = 20
                    self._bombas = 48
            else:
                    coluna = 24
                    linha = 30
                    self._bombas = 72
            self.Montar(coluna,linha)
        except:
            print("erro ocorreu no metodo PreparandoJogo")

    #metodo qeu mostra as tabelas
    def Mostrar(self):
            for c in range(len(self._TabelaPublica)):
                print(self._TabelaPublica[c])
    

    def MostrarMinada(self):
            for c in range(len(self._Tabela_Minada)):
                print(self._Tabela_Minada[c])

    #metodo que adiciona bombas
    def Adicionar_Bombas(self):
        for coluna in range(len(self._Tabela_Minada)):
            bombas = 0
            for linha in range(len(self._Tabela_Minada[coluna])):
                add=random.randint(0,1)
                if (self._bombas>0 and add==1) and bombas <=2:
                    bombas+=1
                    self._bombas-=1
                    self._Tabela_Minada[coluna][linha] = "X"
                elif self._bombas>0 and coluna == self._Tabela_Minada[-1]:
                    bombas+=1
                    self._bombas-=1
                    self._Tabela_Minada[coluna][linha]="X"

        return

    #metodo que inicia o jogo
    def Iniciar(self):
        print('iniciando Jogo ...')
        print("Preparando Estrutura...")
        self.Preparar()
        print("adicionando bombas...")
        self.Adicionar_Bombas()
        self.Mostrar()

    #metodo que verifica se há alguma bomba do lado da escolhida, se tiver ele retorna o numero que tem do lado dele, se não ele marca e vai para as proximas se retro fazendo
    def Marcar(self,c,l,Mhistory,ind):
        try:
            historico=[]
            permitido=[[c-1,l],[c+1,l],[c,l-1],[c,l+1]]
            cf=0
            lf=0
            qntBomb = 0
            for ci in range(3):
                for li in range(3):
                    if(c-1+ci==-1):
                        cf=0
                    else:
                        cf = c-1+ci
                    if(l-1+li==-1):
                        lf=0
                    else:
                        lf = l-1+li

                    if(self._Tabela_Minada[cf][lf]=="X" and [cf,lf] not in historico):
                        qntBomb+=1
                        historico.append([cf,lf])
                    elif( [cf,lf] not in Mhistory and [cf,lf] in permitido and self._Tabela_Minada[cf][lf]!="X"):
                        Mhistory.append([cf,lf])
                        self.Marcar(cf,lf,Mhistory,1)
            self._TabelaPublica[c][l] = qntBomb     
            if(ind==0):
                self.Mostrar()  
        except:
            return 

    #metodo que verifica o local
    def Verifica(self,c,l):
            if self._Tabela_Minada[c][l]=="X":
                print("BOOOOOOOOOOOOOOM!!!!")
            else:
                self.Marcar(c,l,[[c,l]],0)

    #metodo resposavel por realizar jogada
    def Jogar(self,c,l):
        print("Iniciando Jogada")
        self.Verifica(c-1,l-1)


jogo = Campo_Minado("Facil")
print("Campo Minado v: 0.1\nby: João Gabriel Caires Fernandes\ncomo jogar:\n            Escreva a posição que você quer adicionando a coluna e a linha dele.\n\n")
jogo.Iniciar()
while True:
    jogo.Jogar(int(input("coluna: ")),int(input("linha: ")))