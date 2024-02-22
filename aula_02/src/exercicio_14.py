print("-"*5,"Imprime o dia, mês e ano separadamente","-"*5)
data = str(input("digite uma data no formato 'dd/mm/aaaa':"))
dia, mes, ano = data.split("/")
print(f"dia:{dia}\nmês:{mes}\nano:{ano}")
