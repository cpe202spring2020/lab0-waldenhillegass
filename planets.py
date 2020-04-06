def weight_on_planets():
   # write your code here
   str = input("What do you weigh on earth? ")
   weight = float(str)
   mars = weight * 0.38
   jupiter = weight * 2.34

   print("\nOn Mars you would weigh %.2f pounds." %mars)
   print("On Jupiter you would weigh %.2f pounds." %jupiter)
   
   
if __name__ == '__main__':
   weight_on_planets()