# Loops : Helps us in iteration

# For loop

# for i in range(0, 11):
#     print(i)

fruits = ["banana", "orange", "apple", "kiwi"]
# print(fruits)
# quit()

# for fruit in fruits:
#     print(fruit)

numbers = [1,5,7,9,21,33]

for number in numbers:
    # print("Adding the number to itself : " + str(number+number))
    result = number * number
    print(f"Multiplying the number to itself : {result}")

for fruit in fruits:
    if "banana" == fruit:
        print('Banana is available!')
    else:
        print('Banana is not available!')

