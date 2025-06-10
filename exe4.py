class ProdutoFisico:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        
    def processar_pedido(self):
        self.estoque -= 1
        print(f"Seu pedido: {self.nome} foi comprado e deve chegar na sua casa em breve")
        
class Servico:
    def __init__(self, nome, categoria, prestador):
        self.nome = nome
        self.categoria = categoria
        self.prestador = prestador
        
    def processar_pedido(self):
        print(f"{self.prestador} está a caminho da sua casa para realizar o serviço")
        
class ProdutoDigital:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def processar_pedido(self):
        print(f"Seu pedido: {self.nome} foi comprado e deve chegar em seu e-mail em breve")
        
fisico = ProdutoFisico("Xbox Serie X", 4500, 360)
servico = Servico("Conserto de geladeira", "Manutenção", "Roberto")
digital = ProdutoDigital("Gift Card", 45)

for x in (fisico, servico, digital):
    x.processar_pedido()