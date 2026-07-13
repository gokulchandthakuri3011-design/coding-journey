package Week2_OOP_Part1.Polymorphism2;


/*
2. **Employee System**: Create an `Employee` superclass with `name` and `salary` fields and a `calculateBonus()` method returning 5% of salary.
    Create `Manager` (bonus = 10%) and `Developer` (bonus = 7%) subclasses.
    Use upcasting to store both in an `Employee[]` array and calculate bonuses for all.
*/

public class Employee {
    String name;
    double salary;

    // Constructor
    public Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }

    // method returning 5% of salary
    public double calculateBonus() {
        return 0.05 * salary;
    }
}

class Manager extends Employee {
    public Manager(String name, double salary) {
        super(name, salary); // initialize inherited name and salary
    }

    @Override
    public double calculateBonus() {
        return 0.1 * salary;
    }
} 

class Developer extends Employee {
    public Developer(String name, double salary) {
        super(name, salary); // initialize inherited name and salary
    }

    @Override
    public double calculateBonus() {
        return 0.07 * salary;
    }
}

class EmployeeTest {
    public static void main(String[] args) {
        // Upcasting: store Manager and Developer in Employee array
        Employee[] employees = new Employee[3]; // "employees" is an array with type "Employee" and with 3 slots for its object(form Superclass or subclass) wegen Inheritance and method Polymorphism

        employees[0] = new Employee("Gokul", 50000);
        employees[1] = new Manager("Arun", 60000); 
        employees[2] = new Developer("Lalita", 55000);
        
        // Calculating bonuses for all employees
        for (Employee emp : employees) {
            System.out.println(emp.name + " Bonus: $" + emp.calculateBonus());
        }
    }
}

