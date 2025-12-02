class contato:
    def _init_(self, telefone: str, favorito: bool = False):
        self.telefone = telefone
        self.favorito = favorito

    def str(self):
        estrela = "*" if self.favorito else "-"
        return f"{estrela} {self.telefone}"

class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
        self.contatos = []

    def adicionar_contato(self, telefone: str, favorito: bool = False):
        for c in self.contatos:
            if c.telefone == telefone:
                print("fail: telefone ja existe para essa pessoa")
                return False
            
        novo = contato(telefone, favorito)
        self.contatos.append(novo)
        return True
    
    def remover_contato(self, telefone: str):
        for c in self.contatos:
            if c.telefone == telefone:
                self.contatos.remove(c)
                return True
            
        print("fail: telefone nao encontrado")
        return False
    
    def favoritar(self, telefone: str):
        for c in self.contatos:
            if c.telefone == telefone:
                c.favorito = True
                return True
            
        print("fail: telefone não encontrado")
        return False
    
    def desfavoritar(self, telefone: str):
        for c in self.contatos:
            if c.telefone == telefone:
                c.favorito = False
                return True
            
        print("fail: telefone nao encontrado")
        return False
    def __str__(self):
        texto = f"-n{self.nome}\n"
        for c in self.contatos:
            texto+= f" {c}\n"
        return texto.strip()
    while True:
        comando = input()

    