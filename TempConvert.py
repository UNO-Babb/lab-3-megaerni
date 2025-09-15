#TempConvert.py
#Name: Meg Aerni
#Date: 9/14/2025
#Assignment: Lab 3, Part 1


def main():
  #Prompt the user for a Fahrenheit temperature
  fahrentemp = input("Enter the temperature in Fahrenheit: ")
  fahrentemp = int(fahrentemp)
  #Convert that temperature to celsius, rounding to 1 decimal percision
  celsiustemp = (fahrentemp - 32)/1.8
  celsiustemp = round(celsiustemp, 2)
  #Output converted temperature.
  print(fahrentemp, "degrees Fahrenheit is ", celsiustemp, "degrees celsius.")
if __name__ == '__main__':
  main()
