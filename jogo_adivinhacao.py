''''O programa é um jogo de adivinhação com uma narrativa divertida e quebra de linha de forma estilizada usando print_slowly. 
O jogo desafia o usuário a adivinhar o número secreto (42), com três tentativas, fornecendo dicas após os erros.'''
import time

def print_slowly(text):
    for line in text.split('\n'):
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.07)
        print()

def jogo_adivinhacao():
    j = input("\nOlá, diga seu nome: ")

    intro_text = (
        f"Olá {j}, prazer em te conhecer.\n"
        "Eu sou o que vocês chamam de tudo, sou o que pode ser considerado divino, eu sou a verdade, eu sou você!\n"
        "Vamos jogar um pouco, um jogo de adivinhação.\n"
        "Eu guardo um segredo, um número, um número que guarda o segredo do universo, curioso não?\n"
        "Você terá 3 chances de adivinhar o número, se falhar... bem, isso não importa no momento.\n"
    )
    print_slowly(intro_text)

    secret = 42
    tentativas = 3

    for i in range(tentativas):
        while True:
            try:
                palpite_input = input("Insira o seu palpite: ")
                palpite = int(palpite_input)
                break
            except ValueError:
                print("Por favor, insira um número válido. Sabe o que é um número, não sabe? ")

        if palpite == secret:
            print_slowly("Parabéns, você acertou!")
            break
        else:
            if i == 0:
                dica1 = "Você errou, hahaha, Mas aqui vai uma dica:  Sabe ler, não sabe? O segredo está em um livro publicado em 1979."
                print_slowly(dica1)
            elif i == 1:
                dica2 = "Você errou novamente, hahahaha. Aqui vai outra dica: O número é a resposta definitiva para a Questão Fundamental da Vida, do Universo e de Tudo Mais."
                print_slowly(dica2)
            else:
                fim = "Suas tentativas acabaram, esperava mais de ti."
                print_slowly(fim)

if __name__ == "__main__":
    jogo_adivinhacao()
