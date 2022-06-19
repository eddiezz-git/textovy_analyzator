# prvni_projekt.py: první projekt do Engeto Online Python Akademie
# author: Eda Žáček
# email: eda.zacek@gmail.com
# discord: eddiezz#0433

from task_template import TEXTS

#databaze uzivatelu a jejich hesel
user_details = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
dash_sep = 40 * "-"

login_ok = True
while login_ok:
    user = input(f'username:')
    password = input(f'password:')
    print(dash_sep)

    #kontrola prihlasovacich udaju; pokud jsou udaje v poradku privitani, pokud ne ukonceni programu
    if user in user_details and password == user_details[user]:
        print(f"Welcome to the app, {user}.")
        print(f"We have 3 texts to be analyzed.")
        print(dash_sep)

        #vyber textu
        text_choice = int(input(f"Enter a number btw. 1 and 3 to select:"))-1
        print(dash_sep)

        #cisteni vybraneho textu
        word_list_raw = (TEXTS[text_choice])
        wl_no_comma = word_list_raw.replace(",", "")
        wl_no_dots_comma = wl_no_comma.replace(".", "")
        wl_no_dots_comma_space = wl_no_dots_comma.replace("-", " ")
        word_list = wl_no_dots_comma_space.split()

        #analyza textu a tisk odpovedi
        print("There are", words := len(word_list), "words in the selected text.")
        titlecase_words = sum(1 for word in word_list if word.istitle())
        print("There are", titlecase_words, "titlecase words")
        uppercase_words = sum(1 for word in word_list if word.isupper() and word.isalpha())
        print("There are", uppercase_words, "uppercase words")
        lowercase_words = sum(1 for word in word_list if word.islower())
        print("There are", lowercase_words, "lowercase words")
        numeric_strings = sum(1 for word in word_list if word.isnumeric())
        print(f"There are", numeric_strings, "numeric strings")
        sum_of_numbers = sum(int(word) for word in word_list if word.isnumeric())
        print(f"The sum of all numbers", sum_of_numbers)
        print(dash_sep)

        #tisk grafu
        letters = 1
        print('{:<2s}| {:20s} |{:20s}'.format("LEN", "  OCCURRENCES", "NR"))
        print(dash_sep)
        while letters < 25:
            occurrences = (sum(1 for word in word_list if len(word) == letters))
            if occurrences == 0:
                letters += 1
                continue
            elif occurrences > 0:
                print('{:3s}| {:20s} |{:20s}'.format(str(letters), str("*" * occurrences), str(occurrences)))
                letters += 1
            else:
                print("konec vyhledavani")
                break

        break
    else:
        print(f"unregistered user, terminating the program..")
