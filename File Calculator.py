# v1.0 - Calculator Python ;D

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
       return x / y
    else:
       return "Erro!"
    

print("Escolha a operação")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Choose the Operation you want (1/2/3/4): ")

num1 = float(input("firt number one: "))
num2 = float(input("second number two: "))

if escolha == '1':
    print(f"Result: {adicionar (num1, num2)}")
elif escolha == '2':
    print(f"Result: {subtrair (num1, num2)}")
elif escolha == '3':
    print(f"Result: {multiplicar (num1, num2)}")
elif escolha == '4':
    print(f"Result: {dividir (num1, num2)}")
else:
    print("Error!")
