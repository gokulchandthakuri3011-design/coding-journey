import math_utils
import string_utils
import temp_converter


def main():
    # === Math Utility ===
    print("\n--- Math Utility Section ---\n")
    num = 22
    print(math_utils.is_even(num))
    print(math_utils.is_odd(num))
    print(math_utils.square(num))

    # === String Utility ===
    print("\n--- String Utility Section ---\n")
    string = input("Enter a string: ")
    print(f"The reverse of {string} is: {string_utils.reverse_string(string)}")
    print(string_utils.is_palindrome(string))
    print(f"There are {string_utils.count_vowels(string)} vowels in {string}.")

    # === Temperature Conversion Section ===
    print("\n--- Temperature Conversion Section ---\n")
    temp_cels = float(input("Enter temp in celsius to convert it into F/K: "))
    temp_fah = float(input("Enter temperature in fahrenheit to convert it into C/K: "))
    print(f"Temperature {temp_cels} into Fahrenheit: {temp_converter.celsius_to_fahrenheit(temp_cels)}")
    print(f"Temperature {temp_fah} into Celsius: {temp_converter.fahrenheit_to_celsius(temp_fah)}")
    print(f"Temperature {temp_cels} into Kelvin: {temp_converter.celsius_to_kelvin(temp_cels)}")


if __name__ == "__main__":
    main()