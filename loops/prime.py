number = 1
no_of_factors = 0

while number <= 50:
    if number == 1:
        number = number + 1
        continue
    for i in range(1, number + 1):
        if number % i == 0:
            no_of_factors = no_of_factors + 1
    if no_of_factors <= 2:
        print(number)
    number = number + 1
    no_of_factors = 0

