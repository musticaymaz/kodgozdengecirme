# Bir sayının faktöriyelini hesaplayan Python kodu

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))
result = factorial(num)
print(f"{num} sayısının faktöriyeli: {result}")
