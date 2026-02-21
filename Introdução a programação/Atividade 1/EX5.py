letra = input("Digite uma letra: ").lower() # o .lower() transforma a letra em minúscula caso digitem em maiúscula


if letra in "aeiou": # O in é um operador usado para verificar se um valor está dentro do outro, como no caso do 'aeiou1. Caso eu digite um valor e ele esteja dentro do 'aeiou' ele me retorna o pirnt como verdadeiro.
    print("Vogal")
else:
    print("Consoante")