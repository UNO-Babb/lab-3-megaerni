#ApproxPi.py
#Name: Meg Aerni
#Date: 9/14/2025
#Assignment: Lab 3, Part 3
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  userChoiceinput = input("How many digits of precisions would you like to use? (enter a number between 0 and 10): ")
  userChoice = int(userChoiceinput)
  start = time.time()
  #calculate pi using the approximation technique
  approxPi = 4/1
  sign = -1
  denom = 3
  while round(approxPi, userChoice) != round(realPi, userChoice):
    #print(approxPi)
    approxPi = approxPi + (sign * 4 / denom)
    sign = sign * -1
    denom = denom + 2

  #Loop until the level of percision is reached

  end = time.time()

  elapsedTime = end - start
  print("It took", elapsedTime, "minutes to approximate pi when calculating to", userChoice, "digits of precision.")

if __name__ == '__main__':
  main()
