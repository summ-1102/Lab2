print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas")

def get_user_input():
    number_string = input()
    number_list= number_string.split(",")
    numbers= [float(num) for num in number_list]
    print(numbers)
    return numbers

def calc_average(numbers):
    average= sum(numbers) / len(numbers)
    print("Average is " + str(average))

def find_min_max(numbers):
    numbers.sort()
    min = numbers[0]
    max = numbers[len(numbers)-1]
    print("Min num is " + str(min))
    print("Max num is " + str(max))
 
display_main_menu()
number = get_user_input()
calc_average(number)
find_min_max(number)

