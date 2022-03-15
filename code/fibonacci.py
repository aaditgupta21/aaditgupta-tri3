def fib(n):
	if n < 0:
		print("Cannot be negative number")

	if n == 0:
		return 0
	if n==1 or n==2:
		return 1

	else:
		return fib(n-1) + fib(n-2)


def tester():
    num = int(input("Enter a number for Fibonacci Sequence: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, Fibonacci Sequence does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", fib(num))

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   tester()
