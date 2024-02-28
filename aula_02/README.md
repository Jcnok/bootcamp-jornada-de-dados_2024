# Aula 02: TypeError, Type Check, Type Conversion, try-except e if

### Indice dos Exercícios
<a id="ancora"></a>
#### Inteiros (`int`)

1. [Escreva um programa que soma dois números inteiros inseridos pelo usuário.](#ancora01)
2. [Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.](#ancora02)
3. [Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.](#ancora03)
4. [Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.](#ancora04)
5. [Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.](#ancora05)

<a id="ancora1"></a>
#### Números de Ponto Flutuante (`float`)

6. [Escreva um programa que receba dois números flutuantes e realize sua adição.](#ancora06)
7. [Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.](#ancora07)
8. [Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).](#ancora08)
9. [Faça um programa que converta a temperatura de Celsius para Fahrenheit.](#ancora09)
10. [Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.](#ancora10)

<a id="ancora2"></a>
#### Strings (`str`)

11. [Escreva um programa que receba uma string do usuário e a converta para maiúsculas.](#ancora11)
12. [Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.](#ancora12)
13. [Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.](#ancora13)
14. [Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.](#ancora14)
15. [Escreva um programa que concatene duas strings fornecidas pelo usuário.](#ancora15)

<a id="ancora3"></a>
#### Booleanos (`bool`)

16. [Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.](#ancora16)
17. [Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.](#ancora17)
18. [Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.](#ancora18)
19. [Faça um programa que compare se dois números fornecidos pelo usuário são iguais.](#ancora19)
20. [Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.](#ancora20)

<a id="ancora4"></a>
#### TypeError, Type Check e Type Conversion

21. [Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.](#ancora21)
22. [Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.](#ancora22)
23. [Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.](#ancora23)
24. [Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".](#ancora24)
25. [Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.dos pelo usuário são diferentes.](#ancora25)
26. [Desafio - Refatorar o projeto da aula 01 evitando possíveis bugs!](#desafio)

### Exercícios Resolução


<a id="ancora01"></a>
1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.


```python
print("="*5,"Cálculo da soma de dois números inteiros","="*5)
n1 = int(input("digite um número inteiro:"))
n2 = int(input("digito um segundo número inteiro:"))
soma = n1 + n2
print(f"A soma dos dois números é: {soma}")
```

    ===== Cálculo da soma de dois números inteiros =====


    digite um número inteiro: 10
    digito um segundo número inteiro: 14


    A soma dos dois números é: 24

<a id="ancora02"></a>
2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.


```python
print("="*5,"Cálculo do resto da divisão de um número por 5","="*5)
n1 = int(input("digite um número inteiro:"))
divisor = 5 
resto = n1 % divisor
print(f"O resto da divisão do número por 5 é:{resto}")
```

    ===== Cálculo do resto da divisão de um número por 5 =====


    digite um número inteiro: 6


    O resto da divisão do número por 5 é:1

<a id="ancora03"></a>
3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.



```python
print("="*5,"Cálculo o produto de dois números inteiros","="*5)
n1 = int(input("digite um número inteiro:"))
n2 = int(input("digito um segundo número inteiro:"))
soma = n1 * n2
print(f"O produto dos dois números é: {soma}")
```

    ===== Cálculo o produto de dois números inteiros =====


    digite um número inteiro: 4
    digito um segundo número inteiro: 2


    O produto dos dois números é: 8

<a id="ancora04"></a>
4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
   


```python
print("="*5,"Cálculo o quociente de dois números inteiros","="*5)
dividendo = int(input("digite um número inteiro para o dividendo:"))
divisor = int(input("digito um número inteiro para o divisor:"))
quociente = n1 // n2
print(f"O quociente é: {quociente}")
```

    ===== Cálculo o quociente de dois números inteiros =====


    digite um número inteiro para o dividendo: 9
    digito um número inteiro para o divisor: 2


    O quociente é: 2

<a id="ancora05"></a>
5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
   


```python
print("="*5,"Cálculo do quadrado de um número","="*5)
num = int(input("digite um número inteiro para calcular quadrado:"))
quadrado = num ** 2
print(f"O quadrado do número é: {quadrado}")
```

    ===== Cálculo do quadrado de um número =====


    digite um número inteiro para calcular quadrado: 3


    O quadrado do número é: 9

[voltar](#ancora)

<a id="ancora06"></a>
6. Escreva um programa que receba dois números flutuantes e realize sua adição.


```python
print("="*5,"Cálculo da soma de dois números floats","="*5)
n1 = float(input("digite um número floats:"))
n2 = float(input("digito um segundo número floats:"))
soma = n1 + n2
print(f"A soma dos dois números é: {soma}")
```

    ===== Cálculo da soma de dois números floats =====


    digite um número floats: 4.5
    digito um segundo número floats: 5.7


    A soma dos dois números é: 10.2

<a id="ancora07"></a>
7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.


```python
print("="*5,"Cálculo da média de dois números floats","="*5)
n1 = float(input("digite um número floats:"))
n2 = float(input("digito um segundo número floats:"))
media = (n1 + n2) / 2
print(f"A média dos dois números é: {media}")
```

    ===== Cálculo da média de dois números floats =====


    digite um número floats: 5.5
    digito um segundo número floats: 6.6


    A média dos dois números é: 6.05

<a id="ancora08"></a>
8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).


```python
print("="*5,"Cálculo da potência de um número","="*5)
base = int(input("digite um número inteiro para base:"))
expoente = int(input("digite um número inteiro para o expoente:"))
potencia = base ** expoente
print(f"O resultado da potência é: {potencia}")
```

    ===== Cálculo da potência de um número =====


    digite um número inteiro para base: 10
    digite um número inteiro para o expoente: 6


    O resultado da potência é: 1000000

<a id="ancora09"></a>
9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.


```python
print("="*5,"Cálculo da conversão de Celsius para fahrenheit","="*5)
celsius = float(input("digite um número em graus ceusius:"))
fahrenheit = celsius * 1.8 + 32
print(f"{celsius} Graus Celsius equivale a: {round(fahrenheit,2)} graus fahrenheit")
```

    ===== Cálculo da conversão de Celsius para fahrenheit =====


    digite um número em graus ceusius: 37


    37.0 Graus Celsius equivale a: 98.6 graus fahrenheit

<a id="ancora10"></a>
10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.


```python
print("="*5,"Cálculo da área de um círculo","="*5)
raio = float(input("digite o valor do raio do círculo:"))
pi = 3.14
area = pi * raio ** 2
print(f"a área do circulo é:{round(area,2)}")
```

    ===== Cálculo da área de um círculo =====


    digite o valor do raio do círculo: 3


    a área do circulo é:28.26

[voltar](#ancora2).

<a id="ancora11"></a>
11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.


```python
print("="*5,"Converte em Maipuscula","="*5)
string = str(input("digite um nome qualquer:"))
string_maiuscula = string.upper()
print(f"resultado:{string_maiuscula}")
```

    ===== Converte uma string em Maipuscula =====


    digite um nome qualquer: julio


    resultado:JULIO

<a id="ancora12"></a>
12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.


```python
print("="*5,"Converte em minúscula","="*5)
string = str(input("digite seu nome completo:"))
string_minuscula = string.lower()
print(f"resultado:{string_minuscula}")
```

    ===== Converte em minúscula =====


    digite seu nome completo: Julio César Okuda


    resultado:julio césar okuda

<a id="ancora13"></a>
13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.


```python
print("-"*5,"Remove espaços no início e final de uma frase.", "-"*5)
frase = str(input("Insira uma frase com espaço no início e final:"))
frase_sem_espaco = frase.strip()
print(frase_sem_espaco)
```

    ----- Remove espaços no início e final de uma frase. -----


    Insira uma frase com espaço no início e final:  Hoje está um dia chuvoso 


    Hoje está um dia chuvoso

<a id="ancora14"></a>
14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.


```python
print("-"*5,"Imprime o dia, mês e ano separadamente","-"*5)
data = str(input("digite uma data no formato 'dd/mm/aaaa':"))
dia, mes, ano = data.split("/")
print(f"dia:{dia}\nmês:{mes}\nano:{ano}")

```

    ----- Imprime o dia, mês e ano separadamente -----


    digite uma data no formato 'dd/mm/aaaa': 11/06/1979


    dia:11
    mês:06
    ano:1979

<a id="ancora15"></a>
15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
    


```python
print("-"*5,"Concatena duas strings.","-"*5) 
str1 = str(input("digite uma palavra qualquer:"))
str2 = str(input("digite uma segunda palavra:")) 
concatena = " ".join([str1,str2])
print(f"As duas palavras foram concatenadas:{concatena}")
```

    ----- Concatena duas strings. -----


    digite uma palavra qualquer: learning
    digite uma segunda palavra: python


    As duas palavras foram concatenadas:learning python

[voltar](#ancora3).

<a id="ancora16"></a>
16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.


```python
print("-"*5,"compara boleanos com AND","-"*5) 
bool1 = input("insira 'True' ou 'False':").lower()
bool2 = input("insira um segundo 'True' ou 'False' para comparação:").lower()
resultado = bool1 and bool2
print(f"O resultado de {bool1} and {bool2} é: {resultado}!")
```

    ----- compara boleanos com AND -----


    insira 'True' ou 'False': true
    insira um segundo 'True' ou 'False' para comparação: false


    O resultado de true and false é: false!

<a id="ancora17"></a>
17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.


```python
print("-"*5,"compara boleanos com OR","-"*5) 
bool1 = input("insira 'True' ou 'False':").lower()
bool2 = input("insira um segundo 'True' ou 'False' para comparação:").lower()
resultado = bool1 or bool2
print(f"O resultado de {bool1} or {bool2} é: {resultado}!")
```

    ----- compara boleanos com OR -----


    insira 'True' ou 'False': TRUE
    insira um segundo 'True' ou 'False' para comparação: False


    O resultado de true or false é: true!

<a id="ancora18"></a>
18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.


```python
print("-"*5,"inverte boleano","-"*5) 
valor = input("insira 'True' ou 'False':").lower()
if valor == 'true':
    booleano = True
else:
    booleano = False

booleano_invertido = not booleano
print(f"O resultado de {booleano} invertido é: {booleano_invertido}!")
```

    ----- inverte boleano -----


    insira 'True' ou 'False': false


    O resultado de False invertido é: True!

<a id="ancora19"></a>
19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.



```python
print("-"*5,"compara se 2 números são iguais","-"*5) 
val1 = int(input("insira o primeiro valor':"))
val2 = int(input("insira um segundo valor para comparação:"))
resultado = val1 == val2 
print(f" O resultado da comparação da igualdade entre {val1} e {val2} é:{resultado}")
```

    ----- compara se 2 números são iguaisR -----


    insira o primeiro valor': 123
    insira um segundo valor para comparação: 213


     O resultado da comparação entre 123 e 213 é:False


<a id="ancora20"></a>
20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.


```python
print("-"*5,"compara se 2 números são diferentes","-"*5) 
val1 = int(input("insira o primeiro valor':"))
val2 = int(input("insira um segundo valor para comparação:"))
resultado = val1 != val2 
print(f" O resultado da comparação da diferença entre {val1} e {val2} é:{resultado}")
```

    ----- compara se 2 números são diferentes -----


    insira o primeiro valor': 123
    insira um segundo valor para comparação: 321


     O resultado da comparação da diferença entre 123 e 321 é:True
[voltar](#ancora4).

<a id="ancora21"></a>
21. Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.


```python
print("="*5,"Cálculo da conversão de Celsius para fahrenheit","="*5)
try:
    celsius = float(input("digite um número em graus celsius:"))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius} Graus Celsius equivale a: {round(fahrenheit,2)} graus fahrenheit")
except ValueError:
    print("Digite um número válido para temperatura!")
```

    ===== Cálculo da conversão de Celsius para fahrenheit =====


    digite um número em graus celsius: 20 graus


    Digite um número válido para temperatura!

<a id="ancora22"></a>
22. Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.


```python
print("="*5,"Verifica se uma palavra ou frase é um palíndromo","="*5)
try:
    texto = input("insira uma frase ou palavra':")     
    #convertendo todo o texto em minúsculo
    texto = texto.lower()
    #Iterando sobre o texto para remover pontuações e espaços
    texto = ''.join([x for x in texto if x.isalnum()])
    #Verifica se a frase é um palíndromo
    resposta = texto == texto[::-1]   
    if resposta:
        print("o texto é um palíndromo!")
    else:
        print("o textto não é um palíndromo!")
except ValueError:
    print("entrada inválida")
    
    
```

    ===== Verifica se uma palavra ou frase é um palíndromo =====


    insira uma frase ou palavra': Anotaram a data da maratona?


    o texto é um palíndromo!

<a id="ancora23"></a>
23. Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.


```python
print("="*5,"Calculadora Simples","="*5)
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
                
        if operador == '+':
             resultado = num1 + num2
        elif operador == '-':
             resultado = num1 - num2
        elif operador == '*':
             resultado = num1 * num2
        elif operador == '/':
             resultado = num1 / num2
        else:
            raise ValueError("Operador inválido.")
            
        print("Resultado:", resultado)
        break
        
    except ValueError as ve:
        print("Erro:", ve)
        print("Certifique-se de que os números são válidos e o operador é válido.")
    except ZeroDivisionError as zde:
        print("Erro:", zde)
        print("Não é possível dividir por zero. Tente novamente.")


```

    ===== Calculadora Simples =====


    Digite o primeiro número:  2
    Digite o operador (+, -, *, /):  -2
    Digite o segundo número:  2


    Erro: Operador inválido.
    Certifique-se de que os números são válidos e o operador é válido.


    Digite o primeiro número:  2
    Digite o operador (+, -, *, /):  0
    Digite o segundo número:  2


    Erro: Operador inválido.
    Certifique-se de que os números são válidos e o operador é válido.


    Digite o primeiro número:  2
    Digite o operador (+, -, *, /):  -
    Digite o segundo número:  2


    Resultado: 0.0

<a id="ancora24"></a>
24. Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".


```python
try:
    numero = int(input("digite um número inteiro:"))
    if numero == 0:
        print("o número é zero")
    elif numero < 0: 
        print("o número é negativo")
    else:
        print("o número é positivo")
    resto = numero % 2
    if resto == 0:
        print(f"o número é par")
    else:
        print(f"o número é impar")    

except ValueError as e:
    print(e)
    print("Certifique-se de que o número inserido é do tipo inteiro.")
```

    digite um número inteiro: 5


    o número é positivo
    o número é impar

<a id="ancora25"></a>
25. Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.


```python
try:

    lista = input("digite uma sequência de números separado por vírgula:")
    lista_ok = [int(x) for x in lista.split(',')]
    print(f"lista dos números inteiros: {lista_ok}")

except ValueError as e:
    print(e)
    print("Digite uma sequência de números inteiros válidos separado por vírgula")
```

    digite uma sequência de números separado por vírgula: 2, 3  , 4,  5


    lista dos números inteiros: [2, 3, 4, 5]

[voltar](#ancora).


<a id="desafio"></a>
## Desafio - Refatorar o projeto da aula 01 evitando possíveis bugs!
![img](img/desafio2.png)

```python

try:
    # Solicita ao usuário que insira seu nome
    nome = input("Digite seu nome: ").strip()
    
    # Verifica se o nome está vazio ou contém números
    if not nome:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")

    # Solicita ao usuário que insira o valor do salário e valida
    salario = float(input("Digite o valor do seu salário: "))
    if salario <= 0:
        print("Por favor, digite um valor positivo para o salário.")
        raise ValueError

    # Solicita ao usuário que insira o valor do bônus recebido e valida
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
        raise ValueError

    # Calcula o total
    kpi = 1000 + salario * bonus_recebido  

    # Imprime as informações para o usuário
    print(f"{nome}, considerando seu salário de R${salario:.2f} o total com bônus é de R${kpi:.2f}.")
except ValueError as e:
    print("Erro:", e)
except Exception as e:
    print("Ocorreu um erro:", e)

```

[voltar](#ancora).