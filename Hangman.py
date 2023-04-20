def draw_Hangman(mistakes):
    if mistakes == 5:
        return  ''' \033[34m
                _______
                |     
                |
                |
                |
             ___|___
        \033[0m '''
    elif mistakes == 4:
        return ''' \033[34m
                _______
                |     |
                |     
                |
                |
             ___|___          
        \033[0m '''
    elif mistakes == 3:
        return ''' \033[34m
                _______
                |     |
                |     0
                |     
                |
             ___|___          
        \033[0m '''
    elif mistakes == 2:
        return ''' \033[34m
                _______
                |     |
                |     0
                |     |
                |
             ___|___          
        \033[0m '''
    elif mistakes == 1:
        return ''' \033[34m
                _______
                |     |
                |     0
                |    /|\\
                |    
             ___|___          
        \033[0m '''
    elif mistakes == 0:
        return ''' \033[34m
                _______
        G       |     |
        A  o    |     0
        M  v    |    /|\\
        E  e    |    / \\
           r ___|___  
         \033[0m '''

def choice_word(words):
    import random
    word = random.choice(words).lower().split()
    puzzle_word = random.choice(word)
    print("\033[0;9m Загадане слово тільки для перевірки \033[0m: ", puzzle_word)
    return puzzle_word

max_guesses = 6
guesses = ''
puzzle_word = ""

with open("text.txt", "r", encoding="UTF-8") as f:
    words = f.readlines()
    # print(words)
print("Оберіть літеру якщо цікаво вгадати рідке та незвичне ім'я\n\033[35mАле Ви 100% прогаєте ;)"
      "\033[0m \n'\033[91mж\033[0m' - жіноче ім'я \n або \n'\033[91mм\033[0m' - чоловіче ім'я ")
names = str(input("Ваш вибір : "))


if names == "ж" and len(names) == 1 and names.isalpha():
    female_name = words[0].split()
    puzzle_word = choice_word(female_name)
elif names == "м" and len(names) == 1 and names.isalpha():
    male_name = words[1].split()
    puzzle_word = choice_word(male_name)
elif names != "ж" or names != "м" or names.isdigit():
    print("Оберіть тільки 'ж' або 'м' ")
    max_guesses = 0

while max_guesses > 0:
# Рахуємо, скільки літер у загаданому слові не відгадано
    len_word = 0
    for i in puzzle_word:
        if i in guesses:
            print(i, end="")
        else:
            print("_", end="")
            len_word += 1

# Якщо всі літери відгадано, то виграш
    if len_word == 0:
        print("\nТи виграв")
        break

# Просимо користувача ввести літеру
    guess = input(" Введіть літеру: ").lower()
    if len(guess) == 1 and guess.isalpha():
        print("Будь ласка, введіть літеру.")
    else:
        print("Будь ласка, введіть одну літеру.")

# Перевіряємо, чи введена літера є у слові
    if guess in puzzle_word:
        print("Так буква є!")
        guesses += guess
    else:
        print("Sorry ніт такої ;(")
        max_guesses -= 1

 # Перевіряємо, чи залишилося ще спроб
    if max_guesses == 6:
        print("Ви маєте ", max_guesses - 1, 'спроб якщо....', )
    elif max_guesses == 5:
        print("Гра почалась \nЗалишилося", max_guesses - 1, 'спроб', )
        print((draw_Hangman(5)))
    elif max_guesses == 4:
        print("Залишилося", max_guesses - 1, 'спроб', )
        print((draw_Hangman(4)))
    elif max_guesses == 3:
        print("Залишилося", max_guesses - 1, 'спроб', )
        print((draw_Hangman(3)))
    elif max_guesses == 2:
        print("Залишилося", max_guesses - 1, 'спроб', )
        print((draw_Hangman(2)))
    elif max_guesses == 1:
        print("Залишилося", max_guesses - 1, 'спроб', )
        print((draw_Hangman(1)))
    else:
        print("Game over! Слово було :", puzzle_word.capitalize())
        print(draw_Hangman(0))

        print(draw_Hangman(0))