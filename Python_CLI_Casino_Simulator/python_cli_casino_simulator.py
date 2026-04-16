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
    26: "black"
}

outside_bets = {
    1: "Red or Black - czerwone czy czarne?",
    2: "Even or Odd - parzyste czy nieparzyste?,",
    3: "Low or High - Niskie / Wysokie (1-18 / 19-36)",
    4: "Dozens - tuziny: (1-12), (13-24) czy (25-36)"
}

inside_bets = {
    1: "Straight up",
    2: "Split",
    3: "Street",
    4: "Corner",
    5: "Six line",
    6: "Green"
}

bets = {
    1: "Outside bets (niskie ryzyko, mniejsza wygrana)",
    2: "Inside bets (wysokie ryzyko, wysoka wygrana)",
}

black_red = {
    1: "Red (czerwone)",
    2: "Black (czarne)"
}

even_odd = {
    1: "Even (parzyste)",
    2: "Odd (nieparzyste)"
}

low_high = {
    1: "Low (1-18)",
    2: "High (19-36)"
}

dozens = {
    1: "Tuzin pierwszy (1-12)",
    2: "Tuzin drugi (13-24)",
    3: "Tuzin trzeci (25-36)"
}

#POGLĄDOWE!
roulette_table = [
	  [""],
    ["             \U0001f7e9 0 \U0001f7e9         "],
    ["  \U0001f7e5 1 \U0001f7e5   \u2b1b 2 \u2b1b    \U0001f7e5 3 \U0001f7e5  "],
    ["  \u2b1b 4 \u2b1b   \U0001f7e5 5 \U0001f7e5    \u2b1b 6 \u2b1b  "],
    ["  \U0001f7e5 7 \U0001f7e5   \u2b1b 8 \u2b1b    \U0001f7e5 9 \U0001f7e5  "],
    [" \u2b1b 10 \u2b1b ", " \u2b1b 11 \u2b1b ", " \U0001f7e5 12 \U0001f7e5 "],
    [" \u2b1b 13 \u2b1b ", " \U0001f7e5 14 \U0001f7e5 ", " \u2b1b 15 \u2b1b "],
    [" \U0001f7e5 16 \U0001f7e5 ", " \u2b1b 17 \u2b1b ", " \U0001f7e5 18 \U0001f7e5 "],
    [" \U0001f7e5 19 \U0001f7e5 ", " \u2b1b 20 \u2b1b ", " \U0001f7e5 21 \U0001f7e5 "],
    [" \u2b1b 22 \u2b1b ", " \U0001f7e5 23 \U0001f7e5 ", " \u2b1b 24 \u2b1b "],
    [" \U0001f7e5 25 \U0001f7e5 ", " \u2b1b 26 \u2b1b ", " \U0001f7e5 27 \U0001f7e5 "],
    [" \u2b1b 28 \u2b1b ", " \u2b1b 29 \u2b1b ", " \U0001f7e5 30 \U0001f7e5 "],
    [" \u2b1b 31 \u2b1b ", " \U0001f7e5 32 \U0001f7e5 ", " \u2b1b 33 \u2b1b "],
    [" \U0001f7e5 34 \U0001f7e5 ", " \u2b1b 35 \u2b1b ", " \U0001f7e5 36 \U0001f7e5 "],
    [""]
]



# --- FUNKCJE ---

    # --- Pobieranie inputu (int)

def get_int_input(prompt):
    while True:
        int_input = input(prompt)
        try:
            int(int_input)
            menu_choice = int(int_input)
            return menu_choice

        except ValueError:
            print("Podaj poprawną liczbę!")



    # --- Pobieranie inputu (float)


def get_float_input(prompt):
    while True:
        float_input = input(prompt)
        try:
            float(float_input)
            money_input = float(float_input)
            if money_input > 0:
                return money_input
            else:
                print("Kwota musi być większa od 0!")
        except ValueError:
            print("Podaj poprawną liczbę!")




    # --- Główne menu i wybór gry


def main_menu(actions):
    print("Witaj w mini Python Casino!\n")
    for number, action in actions.items():
        print(f"{number}. {action}")
    print()

    while True:
        choice = get_int_input("Wybierz grę wpisując liczbę do niej przypisaną np '1'. \nAby wyjść wpisz '0: ")
        print()
        if 0 <= choice <= len(actions):
            return choice
        else:
            print("\nWprowadzono nieprawidłowe dane!")


    # --- Wyświetlanie portfela

def display_wallet(wallet):
    print(f"Stan konta: ${wallet:.2f}\n")

    options = {
        1: "Doładowanie",
        2: "Wypłata"
    }

    for number, option in options.items():
        print(f"{number}. {option}")
    print()


    # --- Doładowania i wypłaty

def wallet_actions(wallet):
    while True:
        display_wallet(wallet)
        wallet_choice = get_int_input("Wybierz opcję. Aby wyjść wybierz '0': ")
        print()

        if wallet_choice == 1:
            money_add = get_float_input("Wpisz kwotę doładowania: $")
            wallet += money_add
            print(f"Stan konta: ${wallet:.2f}")

        elif wallet_choice == 0:
            break

        elif wallet_choice == 2:
            money_back = get_float_input("Wpisz kwotę wypłaty: $")

            if money_back > wallet:
                print("Wypłata nieudana! Zbyt mało środków na koncie.")

            else:
                wallet -= money_back
                print(f"Stan konta: ${wallet:.2f}")

        else:
            print("Wprowadzono nieprawidłowe dane")

    return wallet
    
    # --- Stół ruletka - wizualny
    
def table(roulette_table):
    for row in roulette_table:
        for element in row:
            print(element, end=" ")
        print()
 


    # --- Pobieranie danych do zakładów [IN PROGRESS - dodać walidację!]

def get_roulette_bet(wallet):
    bet_amount = 0
    bet_choice = 0

    for number, name in bets.items():
        print(f"{number}. {name}")
    print()

    while True:
        bet_choice = get_int_input("Wybierz typ zakładu: ")

        if bet_choice == 0:
            break

        elif 1 <= bet_choice <= len(bets):
            break

    outside_bet_choice = None
    inside_bet_choice = None
    color_choice = None
    even_odd_choice = None
    low_high_choice = None
    dozens_choice = None
    straight_up_choice = None
    split_choice = None
    street_choice = None
    corner_choice = None
    six_line_choice = None
    green_choice = None

    if bet_choice == 1:

        for number, name in outside_bets.items():
            print(f"{number}. {name}")
        print()

        outside_bet_choice = get_int_input("Wybierz typ zakładu: ")

        if outside_bet_choice == 1:

            for number, name in black_red.items():
                print(f"{number}. {name}")
            print()

            color_choice = get_int_input("Wybierz kolor: ")

        elif outside_bet_choice == 2:

            for number, name in even_odd.items():
                print(f"{number}. {name}")
            print()

            even_odd_choice = get_int_input("Wybierz - parzyste/nieparzyste: ")

        elif outside_bet_choice == 3:

            for number, name in low_high.items():
                print(f"{number}. {name}")
            print()

            low_high_choice = get_int_input("Wybierz - niskie/wysokie: ")

        else:

            for number, name in dozens.items():
                print(f"{number}. {name}")
            print()

            dozens_choice = get_int_input("Wybierz tuzin: ")


    elif bet_choice == 2:

        for number, name in inside_bets.items():
            print(f"{number}. {name}")
        print()

        inside_bet_choice = get_int_input("Wybierz typ zakładu: ")
        print()
        
        if inside_bet_choice == 1:
            table(roulette_table)
            
            straight_up_choice = get_int_input("Podaj numer pola na który obstawiasz: ")
                
        	
        elif inside_bet_choice == 2:
            table(roulette_table)
            
            split_choice = get_list_input("Obstaw dwa sąsiadujące numery. Oddzial cyfry przecinkiem np. '2, 5': ")
        	
        elif inside_bet_choice == 3:
            table(roulette_table)
            # DODAJ NUMERY RZĘDÓW
            # DODAJ FUNKCJE OBSŁUGUJĄCĄ LIST INPUT
            
            street_choice = get_int_input("Obstaw jeden z poziomych rzędów: ")
        	
        elif inside_bet_choice == 4:
            table(roulette_table)
            
            corner_choice = get_list_input("Obstaw cztery sąsiadujące numery. Oddzial cyfry przecinkiem np. '1, 2, 4, 5': ")
        	
        elif inside_bet_choice == 5:
            table(roulette_table)
            
            six_line_choice = get_list_input("Obstaw dwa sąsiadujące poziomy. Podaj numery poziomów Oddzial cyfry przecinkiem np. '1, 2': ")
        	
        elif inside_bet_choice == 6:
            table(roulette_table)
            
            green_choice = get_int_input("Aby obstawić na zero wpisz '1': ")
        

    while True:

        bet_amount = get_float_input("Podaj kwotę zakładu: $")

        if bet_amount > wallet:
            print(f"Niewystarczające środki na koncie! Doładuj konto lub wpisz niższą kwotę - twoje saldo: ${wallet:.2f}")

        else:
            break

    return {
    				"bet_amount": bet_amount,
            "bet_choice": bet_choice,
            "outside_bet_choice": outside_bet_choice,
            "color_choice": color_choice,
            "even_odd_choice": even_odd_choice,
            "low_high_choice": low_high_choice,
            "dozens_choice": dozens_choice,
            "inside_bet_choice": inside_bet_choice,
            "straight_up_choice": straight_up_choice,
            "split_choice": split_choice,
            "street_choice": street_choice,
            "corner_choice": corner_choice,
            "six_line_choice": six_line_choice,
            "green_choice": green_choice
    }


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
        print(f"---[{x}]---")

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

    draw_color = roulette.get(draw_result)
    print(f"{draw_result} {draw_color}")
    print()
    return (draw_result, draw_color)


    # --- Ocena zakładu red/black

def evaluate_red_black(color_choice, draw_color, bet_amount):
    if color_choice == 1:
        if draw_color == "red":
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount

        elif draw_color == "black":
            print(f"PORAŻKA -${bet_amount}")
            print()
            return -bet_amount

        else:
            print(f"PORAŻKA - GREEN!!! -${bet_amount}")
            print()
            return -bet_amount



    else:

        if draw_color == "black":
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount

        elif draw_color == "red":
            print(f"PORAŻKA -${bet_amount}")
            print()
            return -bet_amount

        else:
            print(f"PORAŻKA - GREEN!!! -${bet_amount}")
            print()
            return -bet_amount




    # --- Ocena zakładu even/odd

def evaluate_even_odd(even_odd_choice, draw_result, bet_amount):

    if draw_result == 0:
        print(f"PORAŻKA - GREEN!!! -${bet_amount}")
        print()
        return -bet_amount


    elif even_odd_choice == 1:
        if draw_result % 2 == 0:
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount

        else:
            print(f"PORAŻKA -${bet_amount}")
            print()
            return -bet_amount

    else:
        if draw_result % 2 != 0:
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount

        else:
            print(f"PORAŻKA -${bet_amount}")
            print()
            return -bet_amount

    # --- Ocena zakładu low/high

def evaluate_low_high(low_high_choice, draw_result, bet_amount):

    if draw_result == 0:
        print(f"PORAŻKA - GREEN!!! -${bet_amount}")
        print()
        return -bet_amount


    elif low_high_choice == 1:

        if 1 <= draw_result <= 18:
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount

        else:
            print(f"PORAŻKA -${bet_amount}")
            print()
            return -bet_amount

    else:

        if 19 <= draw_result <= 36:
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount

        else:
            print(f"PORAŻKA -${bet_amount}")
            print()
            return -bet_amount

    # --- Ocena zakładu dozens

def evaluate_dozens(dozens_choice, draw_result, bet_amount):

    if draw_result == 0:
        print(f"PORAŻKA - GREEN!!! -${bet_amount}")
        print()
        return -bet_amount


    elif dozens_choice == 1:

        if 1 <= draw_result <= 12:
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount

        else:
            print(f"PORAŻKA -${bet_amount}")
            print()
            return -bet_amount

    elif dozens_choice == 2:

        if 13 <= draw_result <= 24:
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount

        else:
            print(f"PORAŻKA -${bet_amount}")
            print()
            return -bet_amount

    else:

        if 25 <= draw_result <= 36:
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount

        else:
            print(f"PORAŻKA -${bet_amount}")
            print()
            return -bet_amount
            
            
    # --- Ocena wyniku losowania Straight up
    
def evaluate_straight_up(straight_up_choice, draw_result, bet_amount):
    return 0	
    
    # --- Ocena wyniku losowania Split
    
def evaluate_split():
    return 0
    
    
    # --- Ocena wyniku losowania Street
    
def evaluate_street():
    return 0
    
    # --- Ocena wyniku losowania Corner
    
def evaluate_corner():
    return 0 
    
    # --- Ocena wyniku losowania Six line
    
def evaluate_six_line():
    return 0
    
    
    # --- Ocena wyniku losowania Green

def evaluate_green():
    return 0
	
	

    # --- Ocena wyniku losowania/zakładu (ruletka) ROUTER
def evaluate_roulette_bet(bet_data, spin_result):
    bet_amount = bet_data["bet_amount"]
    bet_choice = bet_data["bet_choice"]
    outside_bet_choice = bet_data["outside_bet_choice"]
    color_choice = bet_data["color_choice"]
    even_odd_choice = bet_data["even_odd_choice"]
    low_high_choice = bet_data["low_high_choice"]
    dozens_choice = bet_data["dozens_choice"]
    inside_bet_choice = bet_data["inside_bet_choice"]
    straight_up_choice = bet_data["straight_up_choice"]
    split_choice = bet_data["split_choice"]
    street_choice = bet_data["street_choice"]
    corner_choice = bet_data["corner_choice"]
    six_line_choice = bet_data["six_line_choice"]
    green_choice = bet_data["green_choice"]
    draw_result, draw_color = spin_result

    if bet_choice == 1:

        if outside_bet_choice == 1:
            return evaluate_red_black(color_choice, draw_color, bet_amount)

        elif outside_bet_choice == 2:
            return evaluate_even_odd(even_odd_choice, draw_result, bet_amount)

        elif outside_bet_choice == 3:
            return evaluate_low_high(low_high_choice, draw_result, bet_amount)

        else:
            return evaluate_dozens(dozens_choice, draw_result, bet_amount)

    else:

        if inside_bet_choice == 1:
            return evaluate_straight_up(straight_up_choice, draw_result, bet_amount)
        elif inside_bet_choice == 2:
            return evaluate_split()
        elif inside_bet_choice == 3:
            return evaluate_street()
        elif inside_bet_choice == 4:
            return evaluate_corner()
        elif inside_bet_choice == 5:
            return evaluate_six_line()
        else:
            return evaluate_green()
            

    # --- Ruletka [IN PROGRESS]


def play_roulette(wallet):
    bet_data = get_roulette_bet(wallet)
    if bet_data["bet_choice"] == 0:
        return wallet

    spin_result = roulette_spin(roulette)
    result = evaluate_roulette_bet(bet_data, spin_result)
    wallet += result
    return wallet


# --- Poker [IN PROGRESS]
def play_poker(wallet):
    print("Dostępne wkrótce")
    return wallet


# --- Blackjack [IN PROGRESS]
def play_blackjack(wallet):
    print("Dostępne wkrótce")
    return wallet


def run_casino():
    wallet = 5.50

    while True:
        selected_game = main_menu(actions)

        if selected_game == 1:
            wallet = play_roulette(wallet)

        elif selected_game == 2:
            wallet = play_poker(wallet)

        elif selected_game == 3:
            wallet = play_blackjack(wallet)

        elif selected_game == 4:
            wallet = wallet_actions(wallet)

        elif selected_game == 0:
            break

        else:
            print("Wystąpił błąd! Spróbuj ponownie!")


# --- GŁÓWNY KOD ---

if __name__ == "__main__":
    run_casino()
