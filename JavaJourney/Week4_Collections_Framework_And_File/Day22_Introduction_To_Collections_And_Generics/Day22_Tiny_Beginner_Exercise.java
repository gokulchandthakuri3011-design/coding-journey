/*
## Tiny beginner exercises
1. Create `List<String> colors`, add three names, print the first item.
2. Create `Set<Integer> ids`, add numbers with duplicates, print `size()` (duplicates removed).
3. Create `Map<String,String> phonebook`, add two entries, and retrieve a value by key.
*/

package Week4_Collections_Framework_And_File.Day22_Introduction_To_Collections_And_Generics;

import java.util.*;

public class Day22_Tiny_Beginner_Exercise {
    public static void main(String[] args) {
        // 1. Creating list and adding 3 names and printing first item
        List<String> names = new ArrayList<>();
        names.add("Gokul");
        names.add("Arun");
        names.add("Lalita");
        System.out.println("First item: " + names.get(0));

        // 2. Creating a Set & adding numbers with duplicates and printing size
        Set<Integer> numbers = new HashSet<>();
        numbers.add(0);
        numbers.add(1);
        numbers.add(2);
        numbers.add(1);
        System.out.println("Size of set after duplication removal: " + numbers.size());

        // 3. Creating Map phonebook & adding 2 entries and retrieving them using key
        Map<String,String> phonebook = new HashMap<>();
        phonebook.put("name", "Gokul");
        phonebook.put("age", "22");
        System.out.println("Name: " + phonebook.get("name") + " , age: " + phonebook.get("age"));
    }
}
