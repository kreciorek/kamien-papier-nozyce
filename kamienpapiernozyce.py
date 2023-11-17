import random

#opcje chyba tu
options = ["Kamien", "Papier", "Nozyce"]

#mowi zebys wybral ten syf
user_choice = input("wybierz Kamien, Papier, lub Nozyce (musisz z duzej): ")

computer_choice = random.choice(options)


print("wybieraj:", user_choice)

print("Konkuter Wybral:", computer_choice)

#tutaj jak to samo wezma wiec essa
if user_choice == computer_choice: 

    print("miernotki, xdd")



elif user_choice == "Kamien" and computer_choice == "Nozyce":
    print("wygrales xdd")

elif user_choice == "Papier" and computer_choice == "Kamien":
    print("wygrales xdd")

elif user_choice == "nozyce" and computer_choice == "Papier":
    print("wygrales xdd")
else:
    print("wyjeba typu robot")
# madeinchina

