__author__ = 'diogomartins'
__doc__ = """Write a function that computes the list of
            the first 100 Fibonacci numbers. By definition, the first
            two numbers in the Fibonacci sequence are 0 and 1, and each
            subsequent number is the sum of the previous two. As an example,
            here are the first 10 Fibonnaci
            numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34."""

def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    print(fib_list)

if __name__ == "__main__":
    fibonacci(100)