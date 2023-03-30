# Los números primos son aquellos que solo son divisibles
# entre ellos mismos y el 1

# prime number calculator: find all primes up to n
max = int(input("Find primes up to what number? : "))
primeList = []
# for loop for checking each number
for x in range(2, max + 1):
    isPrime = True
    index = 0
    root = int(x ** 0.5) + 1
    # Itera para determinar si "x" es primo o no lo es
    while index < len(primeList) and primeList[index] <= root:
        if x % primeList[index] == 0:
            isPrime = False
            break
        index += 1
    # Si es primo lo agrega a "primeList"
    if isPrime:
        primeList.append(x)
print(primeList)
# -------------------------------------------------------------
# prime number calculator: find the first n primes
count = int(input("Find how many primes?: "))
primeList = []
x = 2
while len(primeList) < count:
    isPrime = True
    index = 0
    root = int(x ** 0.5) + 1
    # Itera para determinar si "x" es primo o no lo es
    while index < len(primeList) and primeList[index] <= root:
        if x % primeList[index] == 0:
            isPrime = False
            break
        index += 1
    # Si es primo lo agrega a "primeList"
    if isPrime:
        primeList.append(x)
    x += 1
print(primeList)
