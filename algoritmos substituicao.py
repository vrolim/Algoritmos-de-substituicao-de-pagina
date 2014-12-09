#############################################
##UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO ##
##DEPARTAMENTO DE ESTATISTICA E INFORMATICA##
##BACHARELADO EM CIENCIA DA COMPUTACAO     ##
##SISTEMAS OPERACIONAIS                    ##
##AUTOR: VITOR ROLIM                       ##
#############################################

class Memoria:
    '''Classe que possui alguns algoritmos de substituicoes de paginas na memoria'''
    def __init__(self,elementos,paginas):
        self.tamanho_mem = paginas
        self.elementos = elementos
        self.memoria = []
        self.ponteiro = 0
        self.miss = 0
        self.hit = 0
        
    def fifo(self):
        '''Algoritmo de substituicao de paginas FIFO'''
        print "--Algoritmo FIFO--"
        for elemento in self.elementos:
            if(len(self.memoria)<self.tamanho_mem):
                if(self.memoria.__contains__(elemento)==False):
                    self.memoria.append(elemento)
                    self.miss+=1
                    print self.memoria
                    
        for elem in range(len(self.elementos)):
            if (self.memoria.__contains__(self.elementos[elem])):
                self.hit+=1
            else:
                self.miss+=1
                self.memoria[self.ponteiro] = self.elementos[elem]
                if (self.ponteiro==self.tamanho_mem-1):
                    self.ponteiro = 0
                else:
                    self.ponteiro+=1
                print self.memoria
        print "Tamanho da String de referencia: %i" % len(self.elementos)
        print "Total de frames: %i" %self.tamanho_mem
        print "O numero de faltas foi %i" % self.miss+" - %d" % ((self.miss*100)/(self.hit+self.miss))+"%"

    def mru(self):
        '''Algoritmo de substituicao de paginas MRU'''
        print "--Algoritmo MRU--"
        for elemento in self.elementos:
            if(len(self.memoria)<self.tamanho_mem):
                if(self.memoria.__contains__(elemento)==False):
                    self.memoria.append(elemento)
                    self.miss+=1
                    print self.memoria
        self.ponteiro = self.tamanho_mem-1
        
        for elem in range(len(self.elementos)):
            if (self.memoria.__contains__(self.elementos[elem])):
                self.hit+=1
                self.ponteiro = self.memoria.index(self.elementos[elem])
            else:
                self.miss+=1
                self.memoria[self.ponteiro] = self.elementos[elem]

                print self.memoria
        print "Tamanho da String de referencia: %i" % len(self.elementos)
        print "Total de frames: %i" %self.tamanho_mem
        print "O numero de faltas foi %i" % self.miss+" - %d" % ((self.miss*100)/(self.hit+self.miss))+"%"
            
    def otimo(self):
        '''Algoritmo de substituicao de paginas OTIMO'''
        print "--Algoritmo OTIMO--"
        for elemento in self.elementos:
            if(len(self.memoria)<self.tamanho_mem):
                if(self.memoria.__contains__(elemento)==False):
                    self.memoria.append(elemento)
                    self.miss+=1
                    print self.memoria

        for elem in range(len(self.elementos)):
            memoria_auxiliar = []
            if (self.memoria.__contains__(self.elementos[elem])):
                self.hit+=1
            else:
                self.miss+=1
                for e in range(elem,len(self.elementos)):
                    if(self.memoria.__contains__(self.elementos[e]) and (len(memoria_auxiliar)!= len(self.memoria)-1)):
                        memoria_auxiliar.append(self.elementos[e])
                for i in self.memoria:
                    if(memoria_auxiliar.__contains__(i) == False):
                        indice = self.memoria.index(i)
                        self.memoria[indice]=self.elementos[elem]
                        print self.memoria
                        break

        print "Tamanho da String de referencia: %i" % len(self.elementos)
        print "Total de frames: %i" %self.tamanho_mem
        print "O numero de faltas foi %i" % self.miss+" - %d" % ((self.miss*100)/(self.hit+self.miss))+"%"
        

##MAIN - coloque aqui o array de teste e a quantidade de paginas da memoria
##Paginacao([array de elementos],tamanho da memoria) como o exemplo abaixo
if __name__=="__main__":
    #mude aqui para alterar os parametros
    configuracao = Memoria([1,2,3,4,5,6,7,8,9],3)
    #mude aqui para alterar o algoritmo
    configuracao.mru()
