def mutate_string(string, position, character):
    lista = list(string)
    lista[position]=character
    string = ''.join(lista)
    return string 

