import random

user_points = 0
computer_points = 0

options = ["r", "t", "p"]

while True:
    user_choise = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").lower()

    if user_choise == "q":
        break

    if user_choise not in options:
        continue

    computer_choice = random.randint(0, 2)
    # R:0, T:1, P:2
    computer_option = options[computer_choice]

    print("O computador escolheu: " + computer_option)

    if user_choise == computer_option:
        print("Empate!")
    elif user_choise == 'r' and computer_option == 't':
        print("Você Ganhou!")
        user_points = user_points + 1
    elif user_choise == 't' and computer_option == 'p':
        print("Você Ganhou!")
        user_points = user_points + 1
    elif user_choise == 'p' and computer_option == 'r':
        print("Você Ganhou!")
        user_points = user_points + 1
    else:
        print("Você perdeu!")
        computer_points = computer_points + 1

print("Sua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))

if user_points > computer_points:
    print("Vitória!")
elif computer_points == user_points:
    print("Empate!")
else:
    print("Derrota!")

print("Bom Jogo!")
