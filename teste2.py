velocidade = int(input("Digite sua velocidade: "))
limite = 80
multa_por_5km = 100
if velocidade > limite:
  velocidade_acima = velocidade - limite
  if velocidade_acima <= 4:
    print(f"Você excedeu o limite de velocidade em {velocidade_acima} km/h!")
    print(f"Sua multa é de R${multa_por_5km:.2f}.")
  else:
    multa = (velocidade_acima // 5) * multa_por_5km
    print(f"Você excedeu o limite de velocidade em {velocidade_acima} km/h!")
    print(f"Sua multa é de R${multa:.2f}.")
else:
  print("Parabéns, você está dentro do limite!")
