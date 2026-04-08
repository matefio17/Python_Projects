# PYTHON CLI CASINO SIMULATOR

import random
import time


# --- DANE GLOBALNE ---

actions = {
    1: "Ruletka",
    2: "Poker Texas Holdem",
    3: "Blackjack",
    4: "Portfel"
}

roulette = {
    0: "green",
    32: "red",
    15: "black",
    19: "red",
    4: "black",
    21: "red",
    2: "black",
    25: "red",
    17: "black",
    34: "red",
    6: "black",
    27: "red",
    13: "black",
    36: "red",
    11: "black",
    30: "red",
    8: "black",
    23: "red",
    10: "black",
    5: "red",
    24: "black",
    16: "red",
    33: "black",
    1: "red",
    20: "black",
    14: "red",
    31: "black",
    9: "red",
    22: "black",
    18: "red",
    29: "black",
    7: "red",
    28: "black",
    12: "red",
    35: "black",
    3: "red",
    26: "black",
}


# --- FUNKCJE ---

	# --- Główne menu i wybór gry
def main_menu(actions):
    print("Witaj w mini Python Casino!\n")

    for number, action in actions.items():
        print(f"{number}. {action}")
    print()

    choice = None

    while not choice:
        user_input = int(input("Wybierz grę wpisując liczbę do niej przypisaną np '1'. Aby wyjść wpisz '0: "))
        if user_input == 0:
            print("Dziękujemy za wizytę w kasynie!\nZapraszamy ponownie.")
            exit()

        elif 1 <= user_input <= len(actions):
            choice = actions.get(user_input)

        else:
            print("\nWprowadzono nieprawidłowe dane!")
    print()
    return choice



   # --- Wyświetlanie portfela            
        
def display_wallet(wallet):
    print(f"Stan konta: ${wallet:.2f}\n")
    
    options = {1 : "Doładowanie",
                2 : "Wypłata"
    }
    
    for number, option in options.items():
        print(f"{number}. {option}")
    
    # --- Doładowania i wypłaty
    
def wallet_actions(wallet):
    
    while True:
        
        display_wallet(wallet)
        wallet_choice = int(input("Wybierz opcję. Aby wyjść wybierz '0': "))
      
        if wallet_choice == 1:
            money_add = float(input("Wpisz kwotę doładowania: "))
            wallet += money_add
            print(f"Stan konta: ${wallet:.2f}")
    
        elif wallet_choice == 2:
            money_back = float(input("Wpisz kwotę wypłaty: "))
        
            if money_back > wallet:
            
                print("Wypłata nieudana! Zbyt mało środków na koncie.")
            
            else:
        
                wallet -= money_back
                print(f"Stan konta: ${wallet:.2f}")
        
        elif wallet_choice == 0:
            break
        
        else:
            print("Wprowadzono nieprawidłowe dane")
    
    
    return wallet

                    

	# --- Losowanie numeru na ruletce
def roulette_spin(roulette):
    nums = list(roulette.keys())

    start_index = random.randint(0, len(nums) - 1)

    is_running = True
    delay = 0.001

    current_pos = start_index

    while is_running:
        x = nums[current_pos % len(nums)]
        time.sleep(delay)
        print(f"\r---[{x}]---", end="")

        if delay <= 0.1:
            delay *= random.uniform(1.02, 1.04)

        elif 0.1 <= delay <= 1.1:
            delay *= 1.2

        elif delay > 1.1:
            is_running = False
            draw_result = x
            break

        current_pos += 1
    print()

    color = roulette.get(draw_result)
    print(f"\n{draw_result} {color} - wygrany")
    return (draw_result, color)




	# --- Ruletka 
def play_roulette(roulette):
    red_black = "Red or Black - czerwone czy czarne?"
    even_odd = "Even or Odd - parzyste czy nieparzyste?,"
    low_high = "Low or High - Niskie / Wysokie (1-18 / 19-36)"
    dozens = "Dozens - tuziny: (1-12), (13-24) czy (25-36)"

    outside_bets = {
        1: red_black,
        2: even_odd,
        3: low_high,
        4: dozens
    }

    inside_bets = ["Straight up", "Split", "Street", "Corner", "Six line"]

    bets = {
        1: "Outside bets (niskie ryzyko, mniejsza wygrana)",
        2: "Inside bets (wysokie ryzyko, wysoka wygrana)",
    }

    black_red = {
        1: "Red",
        2: "Black"
    }

    print("Witaj w Ruletce!\nWybierz rodzaj zakładu:")
    print()

    for counter, name in bets.items():
        print(f"{counter}. {name}")
    print()

    user_choice = None

    while not user_choice:
        user_choice = int(input("Wybierz wpisując numer np. '1'. Aby wstać od stołu wpisz '0': "))
        if user_choice == 0:
            print("Zapraszamy ponownie.")
            break

        elif 1 <= user_choice <= len(bets):
            bet_name = bets.get(user_choice)

            if bet_name == "Outside bets (niskie ryzyko, mniejsza wygrana)":
                user_bet_choice = None

                for number_1, details in outside_bets.items():
                    print(f"{number_1}. {details}")
                print()

                while not user_bet_choice:
                    user_bet_choice = int(input("Wybierz wpisując numer np. '1'. Aby powrócić do wyboru zakładów wpisz '0': "))

                    if user_bet_choice == 0:
                        print("Zapraszamy ponownie.")
                        break

                    elif user_bet_choice == 1:

                        for number_2, details in black_red.items():
                            print(f"{number_2}. {details}")
                        print()

                        user_color_choice = None

                        while not user_color_choice:
                            user_color_choice = int(input("Wybierz wpisując numer np. '1'. Aby powrócić do wyboru zakładów wpisz '0': "))

                            if user_color_choice == 0:
                                print("Zapraszamy ponownie.")
                                break

                            elif user_color_choice == 1:
                                roulette_spin(roulette)

            elif bet_name == "Inside bets (wysokie ryzyko, wysoka wygrana)":
                user_bet_choice = None

        else:
            print("\nWprowadzono nieprawidłowe dane!")
    print()





	# --- Poker
def play_poker():
    print("Dostępne wkrótce")





	# --- Blackjack
def play_blackjack():
    print("Dostępne wkrótce")






def run_casino():
    wallet = 5.50
    
    while True:
        selected_game = main_menu(actions)

        if selected_game == actions.get(1):
            play_roulette(roulette)

        elif selected_game == actions.get(2):
            play_poker()

        elif selected_game == actions.get(3):
            play_blackjack()
        
        else:
            wallet = wallet_actions(wallet)
        


# --- GŁÓWNY KOD ---

if __name__ == "__main__":
    run_casino()
