# Exercícios de Programação em Python: Orientação a Objetos e Estruturas de Dados

## Descrição

Este repositório contém uma série de exercícios práticos em Python, abordando conceitos fundamentais de Orientação a Objetos (OO) e Estruturas de Dados. Os exercícios incluem a criação de classes, métodos e a implementação de funcionalidades como herança, polimorfismo e manipulação de filas.

## Exercícios

Os seguintes exercícios estão presentes neste repositório:

1. **ex1.py** - Implementação de uma classe `Livro` com funcionalidades de empréstimo e devolução, além de consulta de disponibilidade.
2. **ex2.py** - Criação de uma classe `Retangulo`, com métodos para calcular área e perímetro, além de métodos getters e setters para atributos privados.
3. **ex3.py** - Definição de uma classe base `Animal` e suas subclasses `Cachorro` e `Gato`, com uso de herança e polimorfismo.
4. **ex4.py** - Implementação de classes para representar diferentes tipos de produtos e serviços (`ProdutoFisico`, `Servico`, `ProdutoDigital`), com um método comum `processar_pedido`, explorando o polimorfismo.
5. **ex5.py** - Criação de uma classe `Fila` com as operações típicas de uma fila: enfileirar, desenfileirar, espiar e verificar se a fila está vazia.

## Como Executar

### Pré-requisitos

1. **Python**: Certifique-se de ter o Python 3 instalado em seu sistema.
   
   Você pode verificar sua versão do Python com o comando:

   ```bash
   python --version
``

2. **Nenhuma dependência adicional** é necessária, já que todos os exercícios utilizam apenas bibliotecas padrão do Python.

### Passos para Execução

1. Clone este repositório ou faça o download dos arquivos.

   ```bash
   git clone https://github.com/yockayz/logica-programacao-classes-python.git
   ```

2. Acesse a pasta do repositório:

   ```bash
   cd logica-programacao-classes-python
   ```

3. Para executar os exercícios, basta rodar cada arquivo Python individualmente. Por exemplo, para rodar o exercício 1:

   ```bash
   python exe1.py
   ```

4. Repita o processo para os outros exercícios, substituindo o nome do arquivo conforme necessário:

   ```bash
   python exe2.py
   python exe3.py
   python exe4.py
   python exe5.py
   ```

## Exemplo de Saída Esperada

Abaixo estão exemplos de saída para os exercícios:

### exe1.py:

```bash
Livro disponível
Livro Turma da Mônica foi emprestado
Livro indisponível
Livro devolvido
Livro disponível
```

### exe2.py:

```bash
Altura: 15 | Largura: 7 | Área: 105 | Perímetro: 44
```

### exe3.py:

```bash
Raaawr!
Woof!
Miau!
```

### exe4.py:

```bash
Seu pedido: Xbox Serie X foi comprado e deve chegar na sua casa em breve
Roberto está a caminho da sua casa para realizar o serviço
Seu pedido: Gift Card foi comprado e deve chegar em seu e-mail em breve
```

### exe5.py:

```bash
Erick removido da lista
Erick é o primeriro item da lista
Érica removido da lista
Fila populada
Érica removido da lista
Fila vazia
```
