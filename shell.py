import bearLang as bear

while True:
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