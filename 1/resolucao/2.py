# 2. Construa um programa que receba do usuário a variação do deslocamento de um objeto (em metros) e a variação do tempo percorrido (em segundo). Ao fim, o programa deve calcular a velocidade média, em m/s, do objeto. 

delta_s = float(input("Digite o deslocamento (em metros): "))
delta_t = float(input("Digite o tempo (em segundos): "))
velocidade = delta_s / delta_t
print(f"Vm = {velocidade:.2f} m/s")


# ---

# O que significa o :.2f?

x = 2.3456
print(f"{x:.2f}")   # 2.35  (arredonda)
print(f"{3:.2f}")   # 3.00
print(f"{x:8.2f}")  # '    2.35' (largura 8, alinhado à direita)
print(f"{x:.0f}")   # 2     (sem casas decimais)