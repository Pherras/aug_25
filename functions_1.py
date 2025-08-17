

def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

numbers_above_9 = [10, 20, 30, 40, 50]
numbers_above_0 = [1, 2, 3, 4, 5]

if __name__ == '__main__':




    print(list(map(factorial, range(5))))
    print([factorial(n) for n in range(5)])

    print(list(map(factorial, filter(lambda x: x % 2, range(5)))))
    print([factorial(n) for n in range(5) if n % 2])
