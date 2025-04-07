num = int(input("Digite o número: "))
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outrubro", "novembro", "dezembro"]

if num <= 0 or num > 12:
    num = int(input("Número Inválido!!\nDigite o novo número: "))

print(f"{meses[num-1]}")