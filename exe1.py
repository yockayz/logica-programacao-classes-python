class Livro:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        
    def emprestar(self):
        if self.available:
            self.available = False
            print(f"Livro {self.title} foi emprestado")
        else:
            print("Livro não disponível")
            
    def devolver(self):
        if self.available:
            print("Livro já devolvido")
        else:
            self.available = True
            print("Livro devolvido")
    
    def consultar_status(self):
        if self.available:
            print("Livro disponível")
        else:
            print("Livro indisponível")
            
livro = Livro("Turma da Mônica", "Maurício de Sousa")
livro.consultar_status()
livro.emprestar()
livro.consultar_status()
livro.devolver()
livro.consultar_status()
            