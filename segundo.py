# usuário informa um número
num = int(input("Informe um número: "))

a = 0
b = 1

while b < num:
    temp = b
    b = a + b
    a = temp

if b == num:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")
    
    
    