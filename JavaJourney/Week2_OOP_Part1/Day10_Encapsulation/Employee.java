/*
### Bonus Challenge: Employee Payroll Record
Create a class `Employee` with private fields: `name` (String), `hourlyRate` (double), and `hoursWorked` (int).
- The class should have a parameterized constructor.
- Add getters and setters for all fields.
  - `hourlyRate` must be at least `15.00` (minimum wage). If lower is provided, automatically set it to `15.00`.
  - `hoursWorked` must be between `0` and `80` (maximum 80 hours per pay period). Do not update if invalid.
- Add a public method `calculateSalary()` that returns the total salary (`hourlyRate * hoursWorked`). If `hoursWorked` exceeds `40`, pay double-time (`2.0 * hourlyRate`) for the overtime hours!
- In `main`, test an employee with regular hours and one with overtime hours, and verify all validations and calculations are correct.
*/

package Week2_OOP_Part1.Day10_Encapsulation;

public class Employee {
    private String name;
    private double hourlyRate;
    private int hoursWorked;

    public Employee(String name, double hourlyRate, int hoursWorked) {
        setName(name);
        setHourlyRate(hourlyRate);
        setHoursWorked(hoursWorked);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getHourlyRate() {
        return hourlyRate;
    }

    public void setHourlyRate(double hourlyRate) {
        if (hourlyRate < 15.00) {
            this.hourlyRate = 15.00;
        } else {
            this.hourlyRate = hourlyRate;
        }
    }

    public int getHoursWorked() {
        return hoursWorked;
    }

    public void setHoursWorked(int hoursWorked) {
        if (hoursWorked >= 0 && hoursWorked <= 80) {
            this.hoursWorked = hoursWorked;
        }
    }

    public double calculateSalary() {
        if (hoursWorked <= 40) {
            return hourlyRate * hoursWorked;
        } else {
            int overtimeHours = hoursWorked - 40;
            return (hourlyRate * 40) + (overtimeHours * hourlyRate * 2.0);
        }
    }

    // Main method for testing
    public static void main(String[] args) {
        Employee regularEmployee = new Employee("Gokul", 25.00, 40);
        System.out.println("Regular Employee Name: " + regularEmployee.getName());
        System.out.println("Regular Employee Salary: " + regularEmployee.calculateSalary());

        Employee overtimeEmployee = new Employee("Arun", 15.00, 45);
        System.out.println("Overtime Employee Name: " + overtimeEmployee.getName());
        System.out.println("Overtime Employee Salary: " + overtimeEmployee.calculateSalary());

        // Testing validations
        Employee invalidRateEmployee = new Employee("John", 10.00, 30);
        System.out.println("Invalid Rate Employee Name: " + invalidRateEmployee.getName());
        System.out.println("Invalid Rate Employee Salary: " + invalidRateEmployee.calculateSalary());

        Employee invalidHoursEmployee = new Employee("Jane", 20.00, 90);
        System.out.println("Invalid Hours Employee Name: " + invalidHoursEmployee.getName());
        System.out.println("Invalid Hours Employee Salary: " + invalidHoursEmployee.calculateSalary());
    }
}