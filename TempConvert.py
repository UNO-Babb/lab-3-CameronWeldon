#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = 80
  print("tempF", "is", tempF)

  tempC = (tempF - 32) * 5/9
  

  num = tempC
  rounded_num = round(num, 2)
  print(tempF, "is ", rounded_num, "degrees celsius.")
  
if __name__ == '__main__':
  main()
