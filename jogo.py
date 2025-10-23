import random
import time

print("Bem-Vindo ao jogo de matematica!")
print("Responda o máximo que puder. Digitre 'sair' para encerrar.\n")

pontos = 0
rodada = 1

while True:
    #gera dois numeros e uma operacao aleatoria 
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    operacao = random.choice(["+","-","*"])

  #caucula o resultado certo 
     if operacao == "+":
         resultado_certo = n1 + n2
    elif operacao == "-":
         resultado_certo = n1 + n2
    else:
         resultado_certo = n1 * n2
         
    print(f"Pergunta{rodada}:Quanto é {n1}{operaco}{n2}?")
     resposta = input(">")

    if resposta.lower() =="sair":
        break

#Verifica se e numero
    if not resposta.isdigit() and not (rsposta.startswith("-")and resposta[1:].isdigit()):
         print("por favor, digite um numero ou 'sair'.")
         continue

    if int(resposta) == resultado_certo:
        pontos += 1
        print("correto!")
    else:
      print(f"Errado! A respota certa era {resultado_certo}.")
    
    rodada += 1 
    time.sleep(1)

    print("-"*30)

print(f"\n Fim do jogo! Voce fez {pontos}pontos(s).")
         
         
         
         
         
         
         
         
         
         
         