import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_of_failures = 5
number_of_failures = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
ok = False
while not ok:
    difficulty = input ("""Selecciona el nivel de dificultad: 
                    1. Fácil
                    2. Media
                    3. Difícil
""")
    if difficulty.isdigit():
        difficulty = int(difficulty)
        if difficulty in (1,2,3):
            break
        else:
            print ("Ingrese un valor entre 1 y 3")
    else:
        print ("No ingresó un numero. Ingrese un valor entre 1 y 3")
lista_de_vocales = ['a','e','i','o','ó','u']
lista_inicial = []
match difficulty:
    case 1: 
        print ("Has seleccionado fácil") 
        for letter in secret_word:
            if letter in lista_de_vocales:
                guessed_letters.append(letter)
                lista_inicial.append (letter)
            else:
                lista_inicial.append("_")
        word_displayed = "".join(lista_inicial)
    case 2:
        print ('Has seleccionado dificultad media')
        guessed_letters.append(secret_word[0])
        lista_inicial.append (secret_word[0])
        for letter in secret_word[1:-1]:
            lista_inicial.append("_")
        guessed_letters.append(secret_word[-1])
        lista_inicial.append (secret_word[-1])
        word_displayed = "".join(lista_inicial)
    case 3:
        print ("Has seleccionado dificil")
        word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
while (number_of_failures< max_of_failures):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verificar si la letra ya ha sido adivinada
    if letter == '':
        number_of_failures +=1
        print("Has ingresado un string vacío. Hazlo nuevamente con una letra." +" Vas " + str(number_of_failures) + " intento/s")
        continue
    if not letter.isalpha():
        number_of_failures +=1
        print ("Pierdes un intento al no ingresar una letra. Vas " + str(number_of_failures) + " intento/s. " "Intentalo nuevamente.")
        continue
    if letter in guessed_letters:
        number_of_failures +=1
        print("Ya está esa letra. Vas " + str(number_of_failures) + " intento/s. " "Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        number_of_failures +=1
        print("Lo siento, la letra no está en la palabra. Vas " + str(number_of_failures) + " intento/s")
    # Mostrar la palabra parcialmente adivinada
    letters= []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has incurrido en {number_of_failures} fallos. Perdiste el juego")
    print(f"La palabra secreta era: {secret_word}")