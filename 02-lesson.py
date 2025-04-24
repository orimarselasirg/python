# FOR

number = 0
word = "ana"

# for i in range(5):
#     print(i)

# for i in range(5):
#   number = number + 1
#   print(number)



# texto = "ABCDEF"
# texto[::1]   # A B C D E F   (normal)
# texto[::-1]  # F E D C B A   (reverso)
# texto[::2]   # A C E         (uno sí, uno no)
# texto[1::2]  # B D F         (empieza desde el índice 1)

# for i in word[::-1]:
#   print(i)


# newWord = ""
# for letter in word[::1]:
#   newWord = letter + newWord

# print(newWord)

# if(word == newWord):
#   print(True)
# else:
#   print(False)


# While

# count = 0

# while True:
#   print(count)
#   count = count +1


# option = ""

# while option != "3":
#     print("\n📋 Menú Principal")
#     print("1. Saludar")
#     print("2. Decir una curiosidad")
#     print("3. Salir")

#     option = input("Elige una opción: ")

#     if option == "1":
#         print("¡Hola! ¿Cómo estás?")
#     elif option == "2":
#         print("Sabías que... ¡las abejas pueden reconocer rostros humanos!")
#     elif option == "3":
#         print("Saliendo del programa...")
#     else:
#         print("Opción no válida. Intenta otra vez.")


# Switch

operation = input("Elige una operación (sumar, restar, multiplicar, dividir): ").lower()
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

match operation:
    case "sumar":
        result = num1 + num2
        print(f"Resultado: {result}")
    case "restar":
        result = num1 - num2
        print(f"Resultado: {result}")
    case "multiplicar":
        result = num1 * num2
        print(f"Resultado: {result}")
    case "dividir":
        if num2 != 0:
            result = num1 / num2
            print(f"Resultado: {result}")
        else:
            print("No se puede dividir por cero.")
    case _:
        print("Operación no reconocida.")
