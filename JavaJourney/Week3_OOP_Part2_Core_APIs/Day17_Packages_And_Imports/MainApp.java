package Week3_OOP_Part2_Core_APIs.Day17_Packages_And_Imports;

/*
 * QUICK REFERENCE — How to compile and run:
 *
 * 1. Navigate to this folder:
 *    cd "Week3_OOP_Part2_Core_APIs/Day17_Packages_And_Imports/"
 *
 * 2. Compile all .java files together (so Java can resolve imports):
 *    javac *.java Task1/*.java
 *
 * 3. Go up to the folder ABOVE the package (JavaJourney/):
 *    cd ..
 *    cd ..
 *
 * 4. Run using the FULL package path:
 *    java Week3_OOP_Part2_Core_APIs.Day17_Packages_And_Imports.MainApp
 *
 * WHY?
 * - Step 2: Java needs to see ALL files at once to resolve imports between them.
 * - Step 3: Your package starts with "Week3_OOP_Part2_Core_APIs", so Java
 *           looks for it starting from the folder above that package.
 * - Step 4: Since MainApp belongs to a package, Java needs the full path,
 *           not just "MainApp".
 */

import Week3_OOP_Part2_Core_APIs.Day17_Packages_And_Imports.Task1.Circle;
import Week3_OOP_Part2_Core_APIs.Day17_Packages_And_Imports.Task1.Rectangle;


public class MainApp {
    public static void main(String[] args) {
        Circle circ = new Circle(4.5);
        Rectangle rec = new Rectangle(6.2, 4);

        // Calling thier own respective methods
        circ.circleArea();
        circ.circlePerimeter();

        rec.rectangleArea();
        rec.rectanglePerimeter();
    }

}
