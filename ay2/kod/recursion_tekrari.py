# İteratif yaklaşım, işlemi döngüler (for, while) kullanarak adım adım gerçekleştirirken
# Recursive yaklaşım fonksiyonun problemi daha küçük parçalara bölerek kendisini tekrar çağırmasına dayanır.
# 1) FACTORIAL

def factorial_iterative(n):
    total = 1

    for i in range(1, n + 1):
        total *= i

    return total


def factorial_recursive(n):
    if n == 0:          
        return 1
    return n*factorial_recursive(n-1)
    
    


# 2) FIBONACCI

def fibonacci_iterative(n):
    b=0
    a=1
    for i in range (n):
        temp =a 
        a=b
        b=temp+b
    return a # çünkü a şuanki elemanı b ise bir sonrakini taşıyor.

def fibonacci_recursive(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)


# 3) POWER (üs alma)

def power_iterative(base, exp):
    total =1
    for i in range (exp):
        total*=base
    return total 



def power_recursive(base, exp):
    if exp==0:
        return 1
    return power_recursive(base, exp - 1)*base



if __name__ == "__main__":

    # FACTORIAL
    print("FACTORIAL")
    print("Iterative:", factorial_iterative(5))
    print("Recursive:", factorial_recursive(5))

    print()

    # FIBONACCI
    print("FIBONACCI")
    print("Iterative:", fibonacci_iterative(10))
    print("Recursive:", fibonacci_recursive(10))

    print()

    # POWER
    print("POWER")
    print("Iterative:", power_iterative(2, 5))
    print("Recursive:", power_recursive(2, 5))