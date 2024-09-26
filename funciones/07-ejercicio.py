def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def es_palindromo(texto):
    # es una frase o palabra que se escribe igual del derecho que del reves
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    print(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("amo la paloma"))
print(es_palindromo("hola mundo"))
print(es_palindromo("Reconocer"))
print(es_palindromo("Somos o no somos"))
