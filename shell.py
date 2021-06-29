import bearLang as bear
from time import sleep

print("|------------------------|")
print("| Bear-Lang Shell V0.0.2 |")
print("|------------------------|")
print("Type Help for Commands!")
while True:
    text = input('Bear Lang > ')
    if text == "Exit":
        print("Closing...")
        sleep(1)
        break

    if text == "Help":
        print("Commands:\n")
        print("Help: Shows these commands\n")
        print("Exit: Closes shell\n")
        print("RUN('nameOfProgram'): Runs your program file.\n")
        print("Be sure to replace 'nameOfProgram' with the name of your own file and double quotes.\n")
        print("You can also add, subtract, multiply, and divide, and some other stuff.\n")
        continue

    if text.strip() == "": continue
    result, error = bear.run('<stdin>', text)
    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))