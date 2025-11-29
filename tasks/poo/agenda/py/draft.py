class contato:
    def _init_(self, telefone: str, favorito: bool = False):
        self.telefone = telefone
        self.favorito = favorito

    def str(self):
        return f"{self.nome}:{self.number}"
    

    