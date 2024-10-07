#Task4
num = input("do you want to sort or reverse the list of numbers? ")
numbers = ["apple", "2", "1", "ball"]

if num == "sort":
    numbers.sort()
    print(numbers)
    
elif num == "reverse":
    numbers.reverse()
    print(numbers)
