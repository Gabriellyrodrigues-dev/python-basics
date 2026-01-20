# condicionais.py
# Exemplos de estruturas condicionais em Python

idade = 20

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


senha_correta = "1234"
senha_digitada = "1234"

if senha_digitada == senha_correta:
    print("Acesso liberado")
else:
    print("Senha incorreta")
