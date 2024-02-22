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

