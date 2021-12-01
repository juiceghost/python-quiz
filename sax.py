

choice=input(f"\n\nWelcome to the temperature converter. Please choose if you wan't to convert from \n\n1.Fahrenheit to Celsius or \n2.Celsius to Fahrenheit.\n\n")
if choice==("1"):
    def far_to_cel(f):
        far_to_cel_convert=(f-32)*5/9
        return far_to_cel_convert
    num=far_to_cel(float(input(f"\nPlease enter a temperature you would like to convert!\n\n")))
    print(f"{num:.2f} Celsius")

elif choice==("2"):
    def cel_to_far(c):
        cel_to_far_convert=c*9/5+32
        return cel_to_far_convert
    num2=cel_to_far(float(input(f"what temparature?")))
    print(f"{num2:.2f}Fahrenheit")






