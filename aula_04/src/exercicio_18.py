# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def inverte_texto(texto: str) -> str:
    return texto[::-1]
texto = input("insira um texto:")
print(f"O texto revertido é: {inverte_texto(texto)}")  