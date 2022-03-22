def fib(n):
    if n == 1 or n==0:
        return n 
    return fib(n-1) + fib(n-2)

def tester():
	# Get Number
    num = int(input("Enter a number: "))
    output = [fib(x+1) for x in range(num)]
    print(*output)


if __name__ == "__main__":
    tester()
