#Task3
num = input("do you want to delete a data by index or value? ")
numbers = ["1", "2", "3", "4"]

if num == "index":
    numb = int(input("which number are you going to delete? "))
    numbers.pop(numb)
    print(numbers)
    
elif num == "value":
    numb = input("which number are you going to delete? ")
    numbers.remove(numb)
    print(numbers)
