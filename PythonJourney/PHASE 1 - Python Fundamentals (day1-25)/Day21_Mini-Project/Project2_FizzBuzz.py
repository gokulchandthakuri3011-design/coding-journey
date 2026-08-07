"""
### Project 2: Refactor "FizzBuzz"
Convert FizzBuzz into a function-driven program:
- A function that checks if a number is fizz, buzz, fizzbuzz, or normal
- A function that runs FizzBuzz over a given range
- A main function that asks the user for the range and displays results
"""

def main():
    """Asks user for range and print the result"""
    min_num = int(input("Enter the minimum number for range: "))
    max_num = int(input("Enter the maximum number for range: "))
    fizz_buzz_range(min_num, max_num)


def fizz_buzz_range(min_num, max_num):
    for num in range(min_num, max_num + 1):
        result = fizz_buzz_checker(num)
        if result:
            print(result)
        else:
            print(num)


def fizz_buzz_checker(i):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"
    return result

if __name__ == "__main__":
    main()