class Factorial:
	def __call__(self, number):
		if number ==0:
			return 1
		elif number == 1:
			return 1
		else:
			return number * self(number-1)


def tester():
    num = int(input("Enter a number for factorial: "))
    try:
        fac = Factorial() 
        print("The factorial is", fac(num))   
    except:
        print("Sorry, something went wrong.")   

if __name__ == "__main__":
    tester()