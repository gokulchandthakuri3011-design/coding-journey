# Importing date_utils, file_utils and geometry 

import geometry
import file_utils
import date_utils

def main():
    print("Entering Dates\n")
    # For date_utils 
    date1 = input("Enter the first date: ")
    date2 = input("Enter the second date: ")
    date = input("Enter the date in Y-m-d format to format:")
    year = int(input("Enter the year for checking wether it is leap year or not: "))

    print("Entering Geometrical Dimensions\n")
    # For geometry
    r = int(input("Enter the radius of circle: "))
    l = int(input("Enter the length of rectangle: "))
    b = int(input("Enter the breadth of rectangle: "))
    ba = int(input("Enter the base of triangle: "))
    h = int(input("Enter the height of triangle: "))

    # For file_utils
    text = """Hallo, mein Name ist Son Goku. Ich bin 22 Jahre alt und bin Student an der HNU.
              Ich arbeite gerade bei einer Bäckerei, also beginnt mein erstes Semester ab kommenden September.
              Ich komme aus Nepal und ich habe nicht so viele Fruenden, aber habe ich viele Relatives and Familienmitglieder.
              Ich habe einen BestFreund und er studiert Medizin in Pokhara, und gibt es eine Mädchen(Freundin), die ich mag, und sie auch studiert Medizin in Bangladesh.
              Sie beide sind auch Freund und wir haben zusammen in Klasse 9 und 10 studiert."""

    # Now calling functions
    print("File Utility Checker\n")
    print(f"There are {file_utils.counting_lines(text)} lines in given text.")
    print(f"There are {file_utils.counting_words(text)} words in given text.")
    print(f"There are {file_utils.counting_char(text)} characters in given text.")

    print("Geometry Checker\n")
    print(f"The Area of Circle with radius: {r} is: {geometry.circle_area(r):.2f} sqr meter.")
    print(f"The Area of Rectangle with l: {l} and b: {b} is: {geometry.rectangle_area(l,b):.2f} sqr meter.")
    print(f"The Area of Triangle with base: {ba} and height: {h} is: {geometry.triangle_area(ba,h):.2f} sqr meter.")

    print("Date Utility Checker\n")
    print(f"The day difference between Date1: {date1} and Date2: {date2} is: {date_utils.day_difference(date1,date2)} days")
    print(f"The formated structure for {date} is: {date_utils.format_date(date)}")
    print(f"The year: {year} is leap year: {date_utils.leap_year_checker(year)}")


if __name__ == "__main__":
    main()