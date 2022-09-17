import random

num = random.randrange(1,10)
print(num)
resp= "s"
tentativas = 10
while tentativas>=0:
    chute = int(input(" Dê o seu chute entre 1 e 10:"))
    if num==chute:
       print("Parabens, você acertou!!!")
       resp = "n"
       print(f"Você acertou em {tentativas}")
    else:
       print('VOCÊ ERROU!!!!! :((((')
       tentativas= tentativas-1


print(f"Você chutou {tentativas}x")