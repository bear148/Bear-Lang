import bearLang as bear

while True:
    print("|------------------------|")
    print("| Bear-Lang Shell V0.0.1 |")
    print("|------------------------|")
    text = input('Bear Lang > ')
    if text.strip() == "": continue
    result, error = bear.run('<stdin>', text)
    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))