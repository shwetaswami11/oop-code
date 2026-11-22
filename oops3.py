# 1.student management system
class Student:
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course
    def display_details(self):
        print("name:",self.name,"roll_no:",self.roll_no,"course:",self.course)
s1=Student("annu",101,"DA")
s2=Student("shweta",102,"DS")
s3=Student("gouri",103,"CA")   
s1.display_details()
s2.display_details()
s3.display_details()  

# 2.Employee salary details
class Employee:
    def __init__(self,name ,emp_id,basic_salary):
        self.name = name
        self.emp_id = emp_id
        self.basic_salary = basic_salary
    def calculate_salary(self):
        annual_salary=self.basic_salary * 12
        print("employee name:",self.name)
        print("Employee ID:",self.emp_id)
        print("Annual salary:",annual_salary)
E1=Employee("shweta","EMP11",30000)  
E1.calculate_salary()      

# 3.Mobile phone details
class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display_details(self):
        print("Brand:",self.brand)
        print("model:",self.model)
        print("price",self.price)
    def apply_discount(self,discount):
        final_price=self.price-discount
        print("Final Price:",final_price)
m1=Mobile("oneplus","A3",20000)
m1.display_details()
m1.apply_discount(5000)

# 4.Bank Account
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance +=amount
        print("Amount Deposited:",amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")
    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)
b1 = BankAccount("shweta", 10000)
b1.deposit(5000)
b1.withdraw(2000)
b1.display_balance()

# 5.Car rental syatem
class Car:
    def __init__(self,car_name,rent_per_day):
        self.car_name=car_name
        self.rent_per_day=rent_per_day
    def calculate_rent(self,days):
        total_rent = self.rent_per_day * days
        print("Car Name:", self.car_name)
        print("Total Rental Amount:", total_rent)
c1 = Car("Swift", 1500)
c1.calculate_rent(5)
        
#6 Laptop Information
class Laptop:
    def __init__(self):
        self.brand = "Dell"
        self.ram = "16GB"
        self.price = 55000
    def display_details(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Price:", self.price)
l1 = Laptop()
l1.display_details()

# 7 Book Information
class Book:
    def __init__(self,book_name,author_name,price):
        self.book_name=book_name
        self.author_name=author_name
        self.price=price
    def display_details(self):
        print("Book Name:",self.book_name)
        print("Author:", self.author_name)
        print("Price:", self.price)
b1 = Book("Python Basics", "John", 500)
b2 = Book("Java Programming", "Smith", 600)
b1.display_details()
b2.display_details()

#8 Rectangle Area
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        a=self.length * self.width
        print("Area of Rectangle :",a)
a1=Rectangle(10,5)
a1.area() 

# 9 Electricity Bill
class ElectricityBill:
    def __init__(self,customer_name,units):
        self.customer_name=customer_name
        self.units= units
    def calculate_bill(self):
        if self.units<=100:
            bill=self.units*5
        elif self.units<=200:
            bill=(100*5)+((self.units-100)*7)
        else:
            bill=(100*5)+(100*7)+((self.units-200)*100)
            print("customer Name:",self.customer_name)
            print("units consumed:",self.units)
            print("Total bill :",bill)
e1 = ElectricityBill("shweta", 250)
e1.calculate_bill()

# 10 product inventory
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def display_product(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
    def calculate_total_price(self):
        total = self.price * self.quantity
        print("Total Price:", total)
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Updated Quantity:", self.quantity)
p1 = Product("Laptop", 50000, 2)
p1.display_product()
p1.calculate_total_price()
p1.update_quantity(5)

# 11 company Employee counter
class Employee:
    company_name = "TCS"
    employee_count = 0
    def __init__(self, name, emp_id):
        self.employee_name = name
        self.employee_id = emp_id
        Employee.employee_count += 1
    def display_details(self):
        print("Company:", Employee.company_name)
        print("Employee Name:", self.employee_name)
        print("Employee ID:", self.employee_id)
        print("Total Employees:", Employee.employee_count)
e1 = Employee("Rahul", 101)
e2 = Employee("Priya", 102)
e3 = Employee("Amit", 103)
e1.display_details()
e2.display_details()
e3.display_details()

# 12 .School studennt info
class Student:
    school_name = "ABC School"
    def __init__(self, name, roll_number):
        self.student_name = name
        self.roll_number = roll_number
    def display_details(self):
        percentage = 85
        print("School:", Student.school_name)
        print("Student Name:", self.student_name)
        print("Roll Number:", self.roll_number)
        print("Percentage:", percentage)
s1 = Student("Rahul", 101)
s1.display_details()

# 13.shopping cart
class ShoppingCart:
    discount_percentage = 10
    def __init__(self, customer_name, total_amount):
        self.customer_name = customer_name
        self.total_amount = total_amount
    def calculate_discount(self):
        discount = self.total_amount * ShoppingCart.discount_percentage / 100
        final_amount = self.total_amount - discount
        print("Customer:", self.customer_name)
        print("Total Amount:", self.total_amount)
        print("Discount:", discount)
        print("Final Amount:", final_amount)
c1 = ShoppingCart("Rahul", 2000)
c1.calculate_discount()

# 14 Hospital patient Management
class Patient:
    hospital_name = "City Hospital"
    def __init__(self, name, age, disease):
        self.patient_name = name
        self.patient_age = age
        self.disease = disease
    def display_patient(self):
        print("Hospital:", Patient.hospital_name)
        print("Patient Name:", self.patient_name)
        print("Age:", self.patient_age)
        print("Disease:", self.disease)
p1 = Patient("Rahul", 25, "Fever")
p2 = Patient("Priya", 30, "Cold")
p3 = Patient("Amit", 40, "Cough")
p1.display_patient()
p2.display_patient()
p3.display_patient()

# 15 Online Course management
class Course:
    institute_name = "ABC Institute"
    def __init__(self, course_name, course_fee):
        self.course_name = course_name
        self.course_fee = course_fee
    def calculate_fee(self):
        discount = 10
        final_fee = self.course_fee - (self.course_fee * discount / 100)
        print("Institute:", Course.institute_name)
        print("Course:", self.course_name)
        print("Original Fee:", self.course_fee)
        print("Discount:", discount, "%")
        print("Final Fee:", final_fee)
c1 = Course("Python", 10000)
c1.calculate_fee()

# 16 ATM Withdrawal System
class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def check_balance(self):
        print("Current Balance:", self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
a1 = ATM("Rahul", 10000)
a1.check_balance()
new_balance = a1.withdraw(2000)
print("Updated Balance:", new_balance)
a1.deposit(3000)
a1.check_balance()

# 17 Temperature converter

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def celsius_to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
t1 = Temperature(30)
print("Celsius to Fahrenheit:", t1.celsius_to_fahrenheit())
print("Fahrenheit to Celsius:", t1.fahrenheit_to_celsius(98.6))

# 18.Student Result Management
class StudentResult:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def calculate_total(self):
        return self.m1 + self.m2 + self.m3
    def calculate_percentage(self):
        total = self.calculate_total()
        percentage = total / 300 * 100
        return percentage
    def display_result(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.calculate_total())
        print("Percentage:", self.calculate_percentage(), "%")
s1 = StudentResult("Rahul", 80, 85, 90)
s1.display_result()

# 19. Food ordering system
class FoodOrder:
    def __init__(self, name, food_item, price, quantity):
        self.name = name
        self.food_item = food_item
        self.price = price
        self.quantity = quantity
    def calculate_bill(self):
        return self.price * self.quantity
    def apply_coupon(self, discount):
        total = self.calculate_bill()
        final_bill = total - discount
        return final_bill
    def display_order(self):
        print("Customer:", self.name)
        print("Food Item:", self.food_item)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Bill:", self.calculate_bill())
        print("Final Bill:", self.apply_coupon(50))
f1 = FoodOrder("Rahul", "Pizza", 200, 2)
f1.display_order()

# 20 Vehicle management system
class Vehicle:
    vehicle_count = 0
    def __init__(self, name, vehicle_type, price):
        self.vehicle_name = name
        self.vehicle_type = vehicle_type
        self.vehicle_price = price
        Vehicle.vehicle_count += 1
    def display_details(self):
        print("Vehicle Name:", self.vehicle_name)
        print("Vehicle Type:", self.vehicle_type)
        print("Vehicle Price:", self.vehicle_price)
        print("Total Vehicles:", Vehicle.vehicle_count)
    def calculate_insurance(self, rate):
        insurance = self.vehicle_price * rate / 100
        print("Insurance Amount:", insurance)
    def update_price(self, new_price):
        self.vehicle_price = new_price
        print("Updated Price:", self.vehicle_price)
v1 = Vehicle("Swift", "Car", 800000)
v2 = Vehicle("Honda", "Bike", 100000)
v3 = Vehicle("Tata", "Car", 1200000)
v1.display_details()
v1.calculate_insurance(5)
v1.update_price(850000)
print("Total Vehicles Created:", Vehicle.vehicle_count)