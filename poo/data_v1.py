# camel case DataNascimento
# Data representa um tipo de dado personalizado
# a partir desse tipo/molde pode se criar n obj
# toda função/método dentro de uma classe começa com a 
# palavra (por convenção) self: def func(self) 
# sempre que o python precisar converter um determinado obj pra um
# tipo str, ele chama __str__
class Data:
    def __str__(self): # objeto que está sendo acessado no momento
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data() # instanciou um objeto
# por conta do python ser uma linguagem de tipos dinamica 
# permite criar atributos do objeto, sem precisar criar na classe
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1)

d2 = Data() # construtor # faz o portal entre classe e objeto
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)
