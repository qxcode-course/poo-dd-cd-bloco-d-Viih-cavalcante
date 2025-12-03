class Telefone:
    def __init__(self, id, numero):
        self.id = id
        self.numero = numero
    @staticmethod
    def valido(numero):
        validos = "0123456789()."
        if numero == "":
            return False
        for c in numero:
            if c not in validos:
                return False
            return True
    def __str__(self):
        return f"{self.id}:{self.numero}"
class Contato:
    def __innit__(self, nome):
        self.nome = nome
        self.favorito = False
        self.telefone = []
        def adicionar_telefone(self,id, numero):
            if not Telefone.valido(numero):
                print("fail: invalid numbere")
                return
            self.telefones.append(telefone(id, numero))
        def remover_telefone(self, indice):
            if indice < 0 or indice >= len(self.telefones):
                print("fail: invalid index")
                return
            del self.telefones[indice]
        def alternar_favorito(self):
            self.favorito = not self.favorito
while True:
        comando = input("$ ").split()
        if comando[0] == "end":
            break
        elif comando [0] == "addPessoa":
            _, nome = comando
            agenda.remover_pessoa(nome)
        elif comando[0] == "addContato":
            _, nome, telefone = comando
            agenda.adicionar_contato(nome, telefone)
        elif comando [0] == "addFav":
            _, nome, telefone = comando
            agenda.favoritar(nome,telefone)
        elif comando [0] == "rmFav" :
            _, nome, telefone = comando
            agenda.desfavoritar(nome, telefone)
        elif comando[0] == "rmContato":
            _, nome, telefone = comando
            agenda.remover_contato(nome, telefone)
        elif comando [0] == "buscar":
            _, padrão = comando
            resultados = agenda.buscar(padrão)
            for p in resultados:
                print(p.nome)
        elif comando[0] == "show":
            agenda.mostrar()
        elif comando[0] == "favoritos":
            agenda.mostrar_favoritos()
        else:
            print("fail: comando invalido")        
            
    