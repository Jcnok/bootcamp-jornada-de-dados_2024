```python
# conferindo o ambiente virtual
import site 
site.getsitepackages()
```




    ['/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages']




```python
# conferindo a versão do python 
!python --version
```

    Python 3.11.3


# Aula 04 | Type hint, Tipos complexos (Dicionários vs DataFrames Vs Tabelas Vs Excel) e Funções

## Resolução dos exercícios e desafio

<a id="voltar"></a>

1. [Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.](#ancora01)
2. [Dada a lista `["Python", "Java", "C++", "JavaScript"]`, remova o item "C++" e adicione "Ruby".](#ancora02)
3. [Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.](#ancora03)
4. [Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.](#ancora04)
5. [Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, calcule o preço total da lista de compras.](#ancora05)
6. [Eliminação de Duplicatas:](#ancora06)
* **Objetivo:** Dada uma lista de emails, remover todos os duplicados.
7. [Filtragem de Dados:](#ancora07)

* **Objetivo:** Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
8. [Ordenação Personalizada:](#ancora08)

* **Objetivo:** Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
9. [Agregação de Dados:](#ancora09)

* **Objetivo:** Dado um conjunto de números, calcular a média.
10. [Divisão de Dados em Grupos](#ancora10)

* **Objetivo:** Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
11. [Atualização de Dados](#ancora11)

* **Objetivo:** Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
12. [Fusão de Dicionários](#ancora12)

* **Objetivo:** Dados dois dicionários, fundi-los em um único dicionário.
13. [Filtragem de Dados em Dicionário](#ancora13)

* **Objetivo:** Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
14. [Extração de Chaves e Valores](#ancora14)

* **Objetivo:** Dado um dicionário, criar listas separadas para suas chaves e valores.
15. [Contagem de Frequência de Itens](#ancora15)

* **Objetivo:** Dada uma string, contar a frequência de cada caractere usando um dicionário.
16. [Escreva uma função que receba uma lista de números e retorne a soma de todos os números.](#ancora16)
17. [Crie uma função que receba um número como argumento e retorne `True` se o número for primo e `False` caso contrário.](#ancora17)
18. [Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.](#ancora18)
19. [Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.](#ancora19)
20. [Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.](#ancora20)
21. [Desafio será tipar o desafio da aula 03](#desafio)  


<a id="ancora01"></a>
1. **Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.**


```python
#1. [Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.]
# Cria uma lista de números de 1 a 10
numeros = list(range(1, 11))
# Loop para imprimir cada número e seu quadrado
for numero in numeros:
    quadrado = numero ** 2
    print(f"{numero} elevado ao quadrado é: {quadrado}")

```

    1 elevado ao quadrado é: 1
    2 elevado ao quadrado é: 4
    3 elevado ao quadrado é: 9
    4 elevado ao quadrado é: 16
    5 elevado ao quadrado é: 25
    6 elevado ao quadrado é: 36
    7 elevado ao quadrado é: 49
    8 elevado ao quadrado é: 64
    9 elevado ao quadrado é: 81
    10 elevado ao quadrado é: 100


<a id="ancora02"></a>
 2. **Dada a lista `["Python", "Java", "C++", "JavaScript"]`, remova o item "C++" e adicione "Ruby"**


```python
#2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby"
lista = ["Python", "Java", "C++", "JavaScript"]
lista[2] = "Ruby"
lista
```




    ['Python', 'Java', 'Ruby', 'JavaScript']



<a id="ancora03"></a>
3. **Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.**


```python
#3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# Cria um dicionário com informações do livro
livro = {
    "titulo": "Inteligência Artificial",
    "autor": "Kai-Fu Lee",
    "ano_publicacao": 2019
}

# Imprime cada informação do livro
for chave, valor in livro.items():
    print(f"{chave}: {valor}")

```

    titulo: Inteligência Artificial
    autor: Kai-Fu Lee
    ano_publicacao: 2019


<a id="ancora04"></a>
4. **Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.**


```python
# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
string = "A única maneira de fazer um ótimo trabalho é amar o que você faz."
conta_caractere = {}
for caractere in string:
    if caractere in conta_caractere:
        conta_caractere[caractere] +=1
    else:
        conta_caractere[caractere] = 1
print(conta_caractere)
    
```

    {'A': 1, ' ': 13, 'ú': 1, 'n': 2, 'i': 3, 'c': 2, 'a': 9, 'm': 4, 'e': 4, 'r': 4, 'd': 1, 'f': 2, 'z': 2, 'u': 2, 'ó': 1, 't': 2, 'o': 4, 'b': 1, 'l': 1, 'h': 1, 'é': 1, 'q': 1, 'v': 1, 'ê': 1, '.': 1}


<a id="ancora05"></a>
5. **Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, calcule o preço total da lista de compras.**


```python
#5. Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, calcule o preço total da lista de compras.
lista_compras = ["maçã", "banana", "cereja"]
preco_produto = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = 0
for lista in lista_compras:
    if lista in preco_produto:
        total += preco_produto[lista]
        print(f"produto: {lista.ljust(10)}    -------------- R$ {preco_produto[lista]:.2f}")
    else:
        print(f"produto: {lista.ljust(10)}    -------------- em falta!")

print(f"Total:   ---------------------------- R$ {total:.2f}")
```

    produto: maçã          -------------- R$ 0.45
    produto: banana        -------------- R$ 0.30
    produto: cereja        -------------- R$ 0.65
    Total:   ---------------------------- R$ 1.40


[voltar](#voltar)

<a id="ancora06"></a>
6. **Eliminação de Duplicatas:**
* **Objetivo:** Dada uma lista de emails, remover todos os duplicados.


```python
#6. Eliminação de Duplicatas: Dada uma lista de emails, remover todos os duplicados.
emails = ["joaosilva@email.com", "mariagomes@email.com", "pedrodutra@email.com","joaosilva@email.com",
          "marialopes@email.com", "carlosbarbosa@email.com", "anagomes@email.com","carlosbarbosa@email.com"]
print(f"{'='*10}Os emails duplicados foram removidos com sucesso!{'='*10}\n{list(set(emails))}")
```

    ==========Os emails duplicados foram removidos com sucesso!==========
    ['joaosilva@email.com', 'anagomes@email.com', 'mariagomes@email.com', 'pedrodutra@email.com', 'carlosbarbosa@email.com', 'marialopes@email.com']


<a id="ancora07"></a>
7. **Filtragem de Dados:**
* **Objetivo:** Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.


```python
# 7. Filtragem de Dados: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [10, 20, 45, 18, 12, 16, 5]
resultado = [x for x in idades if x >= 18]
# outra forma list(filter(lambda x: x >= 18, idades))
print(f"Idades maiores ou iguais a 18:{resultado}")
```

    Idades maiores ou iguais a 18:[20, 45, 18]


<a id="ancora08"></a>
8. **Ordenação Personalizada:**
* **Objetivo:** Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.


```python
# 8. Ordenação Personalizada: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas =[
  {"nome": "Ana", "idade": 25},
  {"nome": "Pedro", "idade": 30},
  {"nome": "Maria", "idade": 22},
  {"nome": "Julio", "idade": 28},
]

pessoas_ordenadas = list(sorted(pessoas, key=lambda pessoa: pessoa["nome"]))
print(f"lista ordenada por nome:{pessoas_ordenadas}")
```

    lista ordenada por nome:[{'nome': 'Ana', 'idade': 25}, {'nome': 'Julio', 'idade': 28}, {'nome': 'Maria', 'idade': 22}, {'nome': 'Pedro', 'idade': 30}]


<a id="ancora09"></a>
9. Agregação de Dados:
* **Objetivo:** Dado um conjunto de números, calcular a média.


```python
# 9. Agregação de Dados: Dado um conjunto de números, calcular a média.

conjunto = [6, 7, 8, 6, 5]
media = sum(conjunto)/len(conjunto)
print(f"Média = {media}")
```

    Média = 6.4


<a id="ancora10"></a>
10. Divisão de Dados em Grupos

* **Objetivo:** Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.


```python
# 10. Divisão de Dados em Grupos: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
lista = [ 1, 2, 3, 5, 9, 8 , 15, 36]
lista_pares = []
lista_impares = []
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
print(f"lista de pares = {lista_pares} \n")
print(f"lista de ímpares = {lista_impares}")
```

    lista de pares = [2, 8, 36] 
    
    lista de ímpares = [1, 3, 5, 9, 15]


[voltar](#voltar)

<a id="ancora11"></a>
11. Atualização de Dados

* **Objetivo:** Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.


```python
# 11. Atualização de Dados:Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos = [
  {"nome": "Camiseta","preco": 50.00},
  {"nome": "Calça Jeans","preco": 100.00},
  {"nome": "Tênis", "preco": 150.00},
  {"nome": "Casaco", "preco": 200.00},
  {"nome": "Vestido", "preco": 250.00},
]

nome_produto = 'Camiseta'
novo_preco = 60.00
for produto in produtos:
    if (produto['nome'] == nome_produto):
        produto['preco'] = novo_preco
        print(f"produto {produto['nome']} foi atualizado para: R$ {produto['preco']:.2f}")
```

    produto Camiseta foi atualizado para: R$ 60.00


<a id="ancora12"></a>
12. Fusão de Dicionários

* **Objetivo:** Dado dois dicionários, fundi-los em um único dicionário.


```python
# 12. Fusão de Dicionários: Dado dois dicionários, fundi-los em um único dicionário.
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}
# outra forma de fazer: dict = dicionario1 | dicionario2
dicionario1.update(dicionario2)
print(dicionario1)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}


<a id="ancora13"></a>
13. Filtragem de Dados em Dicionário

* **Objetivo:** Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.


```python
# 13. Filtragem de Dados em Dicionário: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque = {
  "produto1": {"quantidade": 10},
  "produto2": {"quantidade": 0},
  "produto3": {"quantidade": 5},
}
for produto in estoque:
    if (estoque[produto]['quantidade']) > 0:
        print(f"Produto:{produto} em estoque:{estoque[produto]['quantidade']}")  

```

    Produto:produto1 em estoque:10
    Produto:produto3 em estoque:5


<a id="ancora14"></a>
14. Extração de Chaves e Valores

* **Objetivo:** Dado um dicionário, criar listas separadas para suas chaves e valores.


```python
# 14. Extração de Chaves e Valores: Dado um dicionário, criar listas separadas para suas chaves e valores.
estoque = {
  "produto1": 10,
  "produto2": 0,
  "produto3": 5,
}
lista_chave = list(estoque.keys())
lista_valor = list(estoque.values())
print(f"chave:{lista_chave}")
print(f"valor:{lista_valor}")
```

    chave:['produto1', 'produto2', 'produto3']
    valor:[10, 0, 5]


<a id="ancora15"></a>
15. Contagem de Frequência de Itens

* **Objetivo:** Dada uma string, contar a frequência de cada caractere usando um dicionário.


```python
# 15. Contagem de Frequência de Itens: Dada uma string, contar a frequência de cada caractere usando um dicionário.
string = "A única maneira de fazer um ótimo trabalho é amar o que você faz."
conta_caractere = {}
for caractere in string:
    if caractere in conta_caractere:
        conta_caractere[caractere] +=1
    else:
        conta_caractere[caractere] = 1
print(conta_caractere)
```

    {'A': 1, ' ': 13, 'ú': 1, 'n': 2, 'i': 3, 'c': 2, 'a': 9, 'm': 4, 'e': 4, 'r': 4, 'd': 1, 'f': 2, 'z': 2, 'u': 2, 'ó': 1, 't': 2, 'o': 4, 'b': 1, 'l': 1, 'h': 1, 'é': 1, 'q': 1, 'v': 1, 'ê': 1, '.': 1}


[voltar](#voltar)

<a id="ancora16"></a>
16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.


```python
# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def soma_lista_de_numeros(lista):
    return sum(lista)
    
lista_numeros = [2, 5, 6, 8, 34, 87]
soma_lista_de_numeros(lista_numeros)
```




    142



<a id="ancora17"></a>
17.Crie uma função que receba um número como argumento e retorne `True` se o número for primo e `False` caso contrário.


```python
# 17.Crie uma função que receba um número como argumento e retorne `True` se o número for primo e `False` caso contrário. 
# algoritmo de Sieve of Eratosthenes
def num_primo(num):
    if num <= 1: 
        return False 
    elif num <= 3:
        return True
    elif (num % 2 == 0) or (num % 3 == 0):
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
          return False
        i += 6
    return True
    
numero = int(input("Digite um número: "))

if num_primo(numero):
  print(f"O número {numero} é primo.")
else:
  print(f"O número {numero} não é primo.")
    
```

    Digite um número:  143


    O número 143 não é primo.


<a id="ancora18"></a>
18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.


```python
# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def inverte_texto(texto: str) -> str:
    return texto[::-1]
texto = input("insira um texto:")
print(f"O texto revertido é: {inverte_texto(texto)}")  
```

    insira um texto: reverta o texto digitado


    O texto revertido é: odatigid otxet o atrever


<a id="ancora19"></a>
19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.


```python
#19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def encontrar_pares(lista, numero):
  """
  Encontra todas as combinações de pares em uma lista que somam um número dado.

  Argumentos:
    lista: A lista de números a ser pesquisada.
    numero: O número que a soma dos pares deve ser igual.

  Retorno:
    Uma lista de pares que somam o número dado.
  """
  pares = []
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      if lista[i] + lista[j] == numero:
        pares.append((lista[i], lista[j]))

  return pares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = 10

pares = encontrar_pares(lista, numero)

print(f"Pares que somam {numero}: {pares}")

```

    Pares que somam 10: [(1, 9), (2, 8), (3, 7), (4, 6)]


<a id="ancora20"></a>
20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.


```python
# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.
def obter_chaves_ordenadas(dicionario):
  """
  Retorna uma lista de chaves ordenadas de um dicionário.

  Argumentos:
    dicionario: O dicionário a ser usado.

  Retorno:
    Uma lista de chaves ordenadas.
  """
  chaves = list(dicionario.keys())
  chaves.sort()
  return chaves

dicionario = {"b": 6, "d": 2, "a": 3, "e": 4, "c": 5}

chaves_ordenadas = obter_chaves_ordenadas(dicionario)

print(f"Chaves ordenadas: {chaves_ordenadas}")

```

    Chaves ordenadas: ['a', 'b', 'c', 'd', 'e']


[voltar](#voltar)

<a id="desafio"></a>
21.Desafio será tipar o desafio da aula 03


```python
# 21.Desafio será tipar o desafio da aula 03 
from typing import Dict

def solicitar_dados_usuario() -> Dict[str, float]:
    """
    Solicita ao usuário que insira seu nome, salário e percentual de bônus.
    
    Returns:
        Dict[str, float]: Um dicionário contendo o nome, salário e bônus recebido.
    """
    while True:
        try:
            nome = input("Digite seu nome: ").strip()
            if not nome:
                raise ValueError("O nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            
            salario = float(input("Digite o valor do seu salário: "))
            if salario <= 0:
                print("Por favor, digite um valor positivo para o salário.")
                raise ValueError
            
            bonus_recebido = float(input("Digite o percentual do bônus recebido: "))
            if bonus_recebido < 0:
                print("Por favor, digite um valor positivo para o bônus.")
                raise ValueError
            
            return {'nome': nome, 'salario': salario, 'bonus_recebido': bonus_recebido}
        
        except ValueError as e:
            print("Erro:", e)

def calcular_kpi(dados: Dict[str, float]) -> float:
    """
    Calcula o indicador de desempenho (KPI) com base nos dados fornecidos.

    Args:
        dados (Dict[str, float]): Um dicionário contendo o nome, salário e bônus recebido.

    Returns:
        float: O valor do KPI calculado.
    """
    return 1000 + dados['salario'] * dados['bonus_recebido']

def imprimir_informacoes(dados: Dict[str, float], kpi: float) -> None:
    """
    Imprime as informações do usuário e o valor do KPI.

    Args:
        dados (Dict[str, float]): Um dicionário contendo o nome, salário e bônus recebido.
        kpi (float): O valor do indicador de desempenho (KPI).
    """
    print(f"{dados['nome']}, considerando seu salário de R${dados['salario']:.2f}, o total com bônus é de R${kpi:.2f}.")

def main() -> None:
    """
    Função principal do programa.
    """
    while True:
        try:
            dados_usuario = solicitar_dados_usuario()
            kpi = calcular_kpi(dados_usuario)
            imprimir_informacoes(dados_usuario, kpi)
            break
        except Exception as e:
            print("Ocorreu um erro:", e)

if __name__ == "__main__":
    main()

```

    Digite seu nome:  Julio Okuda
    Digite o valor do seu salário:  10000
    Digite o percentual do bônus recebido:  1.5


    Julio Okuda, considerando seu salário de R$10000.00 o total com bônus é de R$16000.00.


[voltar](#voltar)


```python

```
