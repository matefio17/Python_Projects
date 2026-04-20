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
<<<<<<< HEAD
    1: "Straight up - konkretny numer",
    2: "Split - dwa sąsiadujące numery",
    3: "Street - trzy liczby w jedym rzędzie poziomym",
    4: "Corner - cztery numery stykające się rogami",
    5: "Six line - dwa sąsiednie poziome rzędy",
=======
    1: "Straight up",
    2: "Split",
    3: "Street",
    4: "Corner",
    5: "Six line",
>>>>>>> 2eb6322d106bdbd8f5d67e5d9820af9d22eea665
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

<<<<<<< HEAD
=======
#POGLĄDOWE!


def roulette_table():
    # Definicje kolorów ANSI -> Uncomment for colored nums
    R =  "" # "\033[91m"  # Czerwony
    G = "" # "\033[92m"  # Zielony
    B = "" # "\033[90m"  # Ciemnoszary 
    RS = "" # "\033[0m"   # Reset kolorów

    nums = {
        0: f"{G} 0{RS}",
        1: f"{R} 1{RS}", 2: f"{B} 2{RS}", 3: f"{R} 3{RS}",
        4: f"{B} 4{RS}", 5: f"{R} 5{RS}", 6: f"{B} 6{RS}",
        7: f"{R} 7{RS}", 8: f"{B} 8{RS}", 9: f"{R} 9{RS}",
        10: f"{B}10{RS}", 11: f"{B}11{RS}", 12: f"{R}12{RS}",
        13: f"{B}13{RS}", 14: f"{R}14{RS}", 15: f"{B}15{RS}",
        16: f"{R}16{RS}", 17: f"{B}17{RS}", 18: f"{R}18{RS}",
        19: f"{R}19{RS}", 20: f"{B}20{RS}", 21: f"{R}21{RS}",
        22: f"{B}22{RS}", 23: f"{R}23{RS}", 24: f"{B}24{RS}",
        25: f"{R}25{RS}", 26: f"{B}26{RS}", 27: f"{R}27{RS}",
        28: f"{B}28{RS}", 29: f"{B}29{RS}", 30: f"{R}30{RS}",
        31: f"{B}31{RS}", 32: f"{R}32{RS}", 33: f"{B}33{RS}",
        34: f"{R}34{RS}", 35: f"{B}35{RS}", 36: f"{R}36{RS}"
    }

    print("  ┌─────────────────┐")
    print(f"  │       {nums[0]}        │")

    print("  ├─────┬─────┬─────┤")
    
      
    for x in range(1, 37):
        print(f"  │ {nums[x]}"  , end="")
            
        
        if x % 3 == 0:
            row = x // 3
        	
            print(f"  │ <- Rząd nr {row}")
            
                
            if x < 36:
                print("  ├─────┼─────┼─────┤")
                    
            elif x == 36:
                print("  └─────┴─────┴─────┘")
        
    print()
>>>>>>> 2eb6322d106bdbd8f5d67e5d9820af9d22eea665

nums_rows_map = {
    1: [1, 2, 3],
    2: [4, 5, 6],
    3: [7, 8, 9],
    4: [10, 11, 12],
    5: [13, 14, 15],
    6: [16, 17, 18],
    7: [19, 20, 21],
    8: [22, 23, 24],
    9: [25, 26, 27],
    10: [28, 29, 30],
    11: [31, 32, 33],
    12: [34, 35, 36]
}


def roulette_table():
    # Definicje kolorów ANSI -> Uncomment for colored nums
    R = ""   "\033[91m"  # Czerwony
    G = ""   "\033[92m"  # Zielony
    B = ""   "\033[90m"  # Ciemnoszary
    RS = ""  "\033[0m"   # Reset kolorów

    nums = {
        0: f"{G} 0{RS}",
        1: f"{R} 1{RS}", 2: f"{B} 2{RS}", 3: f"{R} 3{RS}",
        4: f"{B} 4{RS}", 5: f"{R} 5{RS}", 6: f"{B} 6{RS}",
        7: f"{R} 7{RS}", 8: f"{B} 8{RS}", 9: f"{R} 9{RS}",
        10: f"{B}10{RS}", 11: f"{B}11{RS}", 12: f"{R}12{RS}",
        13: f"{B}13{RS}", 14: f"{R}14{RS}", 15: f"{B}15{RS}",
        16: f"{R}16{RS}", 17: f"{B}17{RS}", 18: f"{R}18{RS}",
        19: f"{R}19{RS}", 20: f"{B}20{RS}", 21: f"{R}21{RS}",
        22: f"{B}22{RS}", 23: f"{R}23{RS}", 24: f"{B}24{RS}",
        25: f"{R}25{RS}", 26: f"{B}26{RS}", 27: f"{R}27{RS}",
        28: f"{B}28{RS}", 29: f"{B}29{RS}", 30: f"{R}30{RS}",
        31: f"{B}31{RS}", 32: f"{R}32{RS}", 33: f"{B}33{RS}",
        34: f"{R}34{RS}", 35: f"{B}35{RS}", 36: f"{R}36{RS}"
    }

    print("  ┌─────────────────┐")
    print(f"  │       {nums[0]}        │")

    print("  ├─────┬─────┬─────┤")

    for x in range(1, 37):
        print(f"  │ {nums[x]}", end="")

        if x % 3 == 0:
            row = x // 3

            print(f"  │ <- Rząd nr {row}")

            if x < 36:
                print("  ├─────┼─────┼─────┤")

            elif x == 36:
                print("  └─────┴─────┴─────┘")

    print()


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


<<<<<<< HEAD
# --- Pobieranie imputu (list)
=======
   # --- Pobieranie imputu (list) 
   
def get_list_input(prompt):
    while True:
        user_input = input(prompt)
        list_input = user_input.split()
        list_input_checked = []
        try:
            for x in list_input:
                num = int(x)
                list_input_checked.append(num)
            
            return list_input_checked
            
        except ValueError:
            print("Podaj poprawne wartości!")
        
         
>>>>>>> 2eb6322d106bdbd8f5d67e5d9820af9d22eea665

def get_list_input(prompt):
    while True:
        user_input = input(prompt)
        list_input = user_input.split()
        list_input_checked = []
        try:
            for x in list_input:
                num = int(x)
                list_input_checked.append(num)

            return list_input_checked

        except ValueError:
            print("Podaj poprawne wartości!")

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
            roulette_table()

<<<<<<< HEAD
            while True:

                straight_up_choice = get_int_input("Podaj numer pola na który obstawiasz: ")
                if 0 <= straight_up_choice <= 36:
                    break

                else:
                    print("Podaj poprawną wartość! Upewnij się, że twój numer jest na ruletce!")



        elif inside_bet_choice == 2:
            roulette_table()

            while True:

                split_choice = get_list_input("Obstaw dwa sąsiadujące numery. Oddzial cyfry spacją np. '2 5': ")

                diff = max(split_choice) - min(split_choice)

                if diff == 1 or diff == 3:
                    if len(split_choice) == 2:
                        break

                else:
                    print("Podaj poprawną wartość! Upewnij się, że obstawiasz sąsiednie numery!")






        elif inside_bet_choice == 3:
            roulette_table()

            while True:
                street_choice = get_int_input("Obstaw jeden z poziomych rzędów: ")
                if street_choice in nums_rows_map.keys():
                    break

                else:
                    print("Podaj poprawną wartość! Upewnij się, że obstawiasz poprawny rząd!")


        elif inside_bet_choice == 4:
            roulette_table()

            while True:
                corner_choice = get_list_input("Obstaw cztery sąsiadujące numery. Oddzial cyfry spacją np. '1 2 4 5': ")
                corner_choice.sort()
                n = min(corner_choice)

                if len(corner_choice) == 4:
                    if n % 3 != 0 and n + 1 == corner_choice[1] and n + 3 == corner_choice[2] and n + 4 == corner_choice[3]:
                        break

                else:

                    print("Podaj poprawne wartości! Upewnij się, że obstawiasz dokładnie cztery pola stykające się rogami!")




        elif inside_bet_choice == 5:
            roulette_table()

            while True:

                six_line_choice = get_list_input("Obstaw dwa sąsiadujące poziomy. Podaj numery poziomów Oddzial cyfry spacją np. '1 2': ")

                diff = max(six_line_choice) - min(six_line_choice)

                if (six_line_choice[0] in nums_rows_map.keys() and six_line_choice[1] in nums_rows_map.keys()):
                    if diff == 1 and len(six_line_choice) == 2:
                        break

                    else:

                        print("Podaj poprawne wartości! Upewnij się, że obstawiasz sąsiednie rzędy!")
                else:

                    print("Podaj poprawne wartości! Upewnij się, że rzędy na które obstawiasz są między 1 i 12!")

=======
            straight_up_choice = get_int_input("Podaj numer pola na który obstawiasz: ")
                
                
                    
                
        	
        elif inside_bet_choice == 2:
            roulette_table()
            
            
            split_choice = get_list_input("Obstaw dwa sąsiadujące numery. Oddzial cyfry spacją np. '2 5': ")
            
                
                    
        	
        elif inside_bet_choice == 3:
            roulette_table()
         
            
            
            street_choice = get_int_input("Obstaw jeden z poziomych rzędów: ")
        	
        elif inside_bet_choice == 4:
            roulette_table()
            
            corner_choice = get_list_input("Obstaw cztery sąsiadujące numery. Oddzial cyfry spacją np. '1 2 4 5': ")
        	
        elif inside_bet_choice == 5:
            roulette_table()
            
            six_line_choice = get_list_input("Obstaw dwa sąsiadujące poziomy. Podaj numery poziomów Oddzial cyfry spacją np. '1 2': ")
        	
        
>>>>>>> 2eb6322d106bdbd8f5d67e5d9820af9d22eea665

    while True:

        bet_amount = get_float_input("Podaj kwotę zakładu: $")

        if bet_amount > wallet:
            print(
                f"Niewystarczające środki na koncie! Doładuj konto lub wpisz niższą kwotę - twoje saldo: ${wallet:.2f}")

        else:
            break

    return {
<<<<<<< HEAD
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
=======
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
>>>>>>> 2eb6322d106bdbd8f5d67e5d9820af9d22eea665
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
<<<<<<< HEAD

=======
        
>>>>>>> 2eb6322d106bdbd8f5d67e5d9820af9d22eea665
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

    draw_color = roulette.get(draw_result)
    print()
    print(f"{draw_result} {draw_color}")
    print()
    return (draw_result, draw_color)

    # --- Ocena zakładu red/black


def win_message(bet_amount):
    print(f"WYGRANA! +${bet_amount}")
    print()
    return bet_amount

def lose_message(bet_amount):
    print(f"PORAŻKA -${bet_amount}")
    print()
    return -bet_amount

def green_lose_message(bet_amount):
    print(f"PORAŻKA - GREEN!!! -${bet_amount}")
    print()
    return -bet_amount


def evaluate_red_black(color_choice, draw_color, bet_amount):
    if color_choice == 1:
        if draw_color == "red":
            return win_message(bet_amount)

        elif draw_color == "black":
            return lose_message(bet_amount)

        else:
            return green_lose_message(bet_amount)



    else:

        if draw_color == "black":
            return win_message(bet_amount)

        elif draw_color == "red":
            return lose_message(bet_amount)

        else:
            return green_lose_message(bet_amount)

    # --- Ocena zakładu even/odd


def evaluate_even_odd(even_odd_choice, draw_result, bet_amount):
    if draw_result == 0:
        return green_lose_message(bet_amount)


    elif even_odd_choice == 1:
        if draw_result % 2 == 0:
            return win_message(bet_amount)

        else:
            return lose_message(bet_amount)

    else:
        if draw_result % 2 != 0:
            return win_message(bet_amount)

        else:
            return lose_message(bet_amount)

    # --- Ocena zakładu low/high


def evaluate_low_high(low_high_choice, draw_result, bet_amount):
    if draw_result == 0:
        return green_lose_message(bet_amount)


    elif low_high_choice == 1:

        if 1 <= draw_result <= 18:
            return win_message(bet_amount)

        else:
            return lose_message(bet_amount)

    else:

        if 19 <= draw_result <= 36:
            return win_message(bet_amount)

        else:
            return lose_message(bet_amount)

    # --- Ocena zakładu dozens


def evaluate_dozens(dozens_choice, draw_result, bet_amount):
    if draw_result == 0:
        return green_lose_message(bet_amount)


    elif dozens_choice == 1:

        if 1 <= draw_result <= 12:
<<<<<<< HEAD
            return win_message(bet_amount * 2)
=======
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount * 2
>>>>>>> 2eb6322d106bdbd8f5d67e5d9820af9d22eea665

        else:
            return lose_message(bet_amount)

    elif dozens_choice == 2:

        if 13 <= draw_result <= 24:
<<<<<<< HEAD
            return win_message(bet_amount * 2)
=======
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount * 2
>>>>>>> 2eb6322d106bdbd8f5d67e5d9820af9d22eea665

        else:
            return lose_message(bet_amount)

    else:

        if 25 <= draw_result <= 36:
<<<<<<< HEAD
            return win_message(bet_amount * 2)

        else:
            return lose_message(bet_amount)

    # --- Ocena wyniku losowania Straight up


def evaluate_straight_up(straight_up_choice, draw_result, bet_amount):
    if straight_up_choice == draw_result:

        return win_message(bet_amount * 35)

    else:

        return lose_message(bet_amount)

    # --- Ocena wyniku losowania Split


def evaluate_split(split_choice, draw_result, bet_amount):
    if draw_result in split_choice:

        return win_message(bet_amount * 17)

    else:

        return lose_message(bet_amount)


    # --- Ocena wyniku losowania Street


def evaluate_street(street_choice, draw_result, bet_amount):

    if draw_result in nums_rows_map.get(street_choice):

        return win_message(bet_amount * 11)

    else:

        return lose_message(bet_amount)

    # --- Ocena wyniku losowania Corner


def evaluate_corner(corner_choice, draw_result, bet_amount):

    if draw_result in corner_choice:

        return win_message(bet_amount * 8)

    else:

        return lose_message(bet_amount)

    # --- Ocena wyniku losowania Six line


def evaluate_six_line(six_line_choice, draw_result, bet_amount):

    row1 = nums_rows_map.get(six_line_choice[0])
    row2 = nums_rows_map.get(six_line_choice[1])

    winning_pool = row1 + row2

    if draw_result in winning_pool:

        return win_message(bet_amount * 5)

    else:

        return lose_message(bet_amount)
=======
            print(f"WYGRANA! +${bet_amount}")
            print()
            return bet_amount * 2

        else:
            print(f"PORAŻKA -${bet_amount}")
            print()
            return -bet_amount
            
            
    # --- Ocena wyniku losowania Straight up
    
def evaluate_straight_up(straight_up_choice, draw_result, bet_amount):

    
    if straight_up_choice == draw_result:
      print(f"WYGRANA! +${bet_amount}")
      print()
      return bet_amount * 35

    else:
        print(f"PORAŻKA -${bet_amount}")
        print()
        return -bet_amount
    		
    
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
    
    
        
	
>>>>>>> 2eb6322d106bdbd8f5d67e5d9820af9d22eea665

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
            return evaluate_split(split_choice, draw_result, bet_amount)
        elif inside_bet_choice == 3:
            return evaluate_street(street_choice, draw_result, bet_amount)
        elif inside_bet_choice == 4:
            return evaluate_corner(corner_choice, draw_result, bet_amount)
        elif inside_bet_choice == 5:
<<<<<<< HEAD
            return evaluate_six_line(six_line_choice, draw_result, bet_amount)
=======
            return evaluate_six_line()
        
            
            
>>>>>>> 2eb6322d106bdbd8f5d67e5d9820af9d22eea665

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
    wallet = 1000

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