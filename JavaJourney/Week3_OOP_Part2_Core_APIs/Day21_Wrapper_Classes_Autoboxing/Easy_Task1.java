package Week3_OOP_Part2_Core_APIs.Day21_Wrapper_Classes_Autoboxing;

/*
**1. Wrapper Conversion Practice**
- Create variables: `int`, `double`, `boolean`, `char`
- Convert each to its wrapper class using autoboxing
- Convert each back to primitive using unboxing
- Print all values before and after conversion
*/

public class Easy_Task1 {
    public static void main(String[] args) {
        // Creating variables
        int age = 22;
        double height = 5.10;
        boolean isStudent = true;
        char lovingLetter = 'L';

        // Printing before conversion
        System.out.println("--- Before Conversion ---");
        System.out.println("Age: " + age);
        System.out.println("Height: " + String.format("%.2f", height) + " feet");
        System.out.println("Is Student: " + isStudent);
        System.out.println("Most Favourite Letter: " + lovingLetter);
        System.out.println();

        // Converting to wrapper class(Autoboxing)
        Integer age1 = age;
        Double height1 = height;
        Boolean isStudent1 = isStudent;
        Character lovingLetter1 = lovingLetter;

        // Printing after the Wrapper
        System.out.println("--- After Conversion to Wrapper ---");
        System.out.println("Age: " + age1);
        System.out.println("Height: " + String.format("%.2f", height1) + " feet");
        System.out.println("Is Student: " + isStudent1);
        System.out.println("Most Favourite Letter: " + lovingLetter1);
        System.out.println();

        // Converting each back to primitive(Unboxing)
        int age2 = age1;
        double height2 = height1;
        boolean isStudent2 = isStudent1;
        char lovingLetter2 = lovingLetter1;

        // Printing after unboxing
        System.out.println("--- After Unboxing ---");
        System.out.println("Age: " + age2);
        System.out.println("Height: " + String.format("%.2f", height2) + " feet");
        System.out.println("Is Student: " + isStudent2);
        System.out.println("Most Favourite Letter: " + lovingLetter2);
    }
}
