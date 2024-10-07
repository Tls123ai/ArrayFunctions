#Task2
num = input("Do you want to clear the list of data?: ")
numbers = ["2", "3", "4", "5"]
if num == "yes":
    numbers.clear()
    print(numbers)
    
elif num == "no":
    print(numbers)
