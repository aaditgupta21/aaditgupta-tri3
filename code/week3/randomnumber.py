import random

n = random.randint(0, 10000)
ans = -1

while(ans != n):
  ans = int(input("Guess a number between 0-10000: "))
  if(ans == n):
    print("You win! The number was: " + str(n))

  elif (ans > n):
    print("lower")

  elif (ans < n):
    print("higher")
