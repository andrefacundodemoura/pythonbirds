class Pessoa:
    #atributo de classe para valores que nao mudam nos objetos
    olhos = 2
    def __init__(self, *filhos ,nome=None, idade=35):
        #atributos de dados para valores que variam nos objetos
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return 'ola'
if __name__ =='__main__':
    andrezinho = Pessoa(nome = 'Andrezinho', idade = 8)
    davi = Pessoa(nome = 'Davi', idade = 3)
    andre = Pessoa(andrezinho, davi, nome='Andre', idade = 31)

    print(f'{andre.nome} tem {andre.idade} anos esses são seus filhos')

    for filho in andre.filhos:
        print(f'Filho:{filho.nome} com a idade de :{filho.idade} anos')

    print(andre.__dict__)
    print(davi.__dict__)
    print(andrezinho.__dict__)