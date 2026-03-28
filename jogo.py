import random
palavras = ["autografo", "simplesmente", "abacate", "hemodialise", "sabedoria", "gentileza"]

def feedback(x):
    auxiliar = ""
    while x > 0:
        auxiliar += "_"
        x -= 1
    return auxiliar


def jogo(palavraSorteada):
    game_over = False
    letrasCertas = []
    vidas = 5

    while not game_over:
        chute = input("\nChute uma letra: ").lower()
        display= ""

        if chute in letrasCertas:
            print("Você já chutou essa letra, tente outra!")
        
        for letra in palavraSorteada:
            if letra == chute:
                display += letra
                letrasCertas.append(chute)
            elif letra in letrasCertas:
                display += letra
            else:
                display += "_"
        print(display)

        if chute not in palavraSorteada:
            vidas -= 1
            print("vidas restantes: ", vidas)
    
        if "_" not in display:
            game_over = True
            print("ganhou!")

        if vidas == 0:
            game_over = True
            print("perdeu! sem vidas restantes.")

def main():
   escolha = random.choice(palavras)
   qtdLetras = len(escolha)
   
   print("Vamos começar o jogo 'Forca', as regras são simples:")
   print("\n1-você deve chutar letras e tentar adivinhar a palavra aleatória.")
   print("\n2-você só tem 5 vidas, então caso erre 5 vezes, perderá.")
   print("\n3-não é interessante chutar a mesma letra várias vezes")
   print("\nPara começar, seguir está o display da palavra secreta:")
   interface = feedback(qtdLetras)
   print(interface)

   jogo(escolha)

if __name__ == "__main__" :
   main()
