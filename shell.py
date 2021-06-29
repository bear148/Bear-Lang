import bearLang as bear

while True:
    text = input('Bear Lang > ')
    result, error = bear.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)