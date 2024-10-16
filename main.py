
# This Script finds which numbers within a range are good to use for weekly investments.


def is_useful(from_number, to_number):
    useful_numbers = []

    for i in range(from_number, to_number):
         if (i/12/4) % 3 == 0:
            useful_numbers.append(i)
    return useful_numbers


start_number = int(input("Enter a from number: "))
end_number = int(input("Enter a to number: "))

print(f'From numbers {start_number} to number {end_number} the useful numbers are: {is_useful(start_number, end_number)}')