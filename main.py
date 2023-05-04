"""
Bunch of example functions and statements to demonstrate to primarily first and second year students.
Will add more as needed from assignments and such.
Uncomment functions as needed to see functionality.
"""
import math
import os
import random
import sqlite3
from sqlite3 import Error
import csv
import string

"""
Generate a random password for employees, then add the password
Onto a new spreadsheet (CSV File) that contains the following columns imported from an existing CSV File:
first name, last name, phone and email. Essentially, creating a new CSV with appended password column.
Note: writerows is used over writerow.
"""


def passwordGen(length):
    all = string.ascii_letters+string.digits+'!@#$%^&*(){}?'
    password = "".join(random.sample(all,length))
    return password


def csvPassword():
    with open('employees.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        passlength = 16
        for i in range(len(rows)):
            if i == 0:
                rows[0].append("Password")
                continue
            newpass = passwordGen(passlength)
            rows[i].append(newpass)
    with open('empnew.csv', 'w', newline="") as fi:
        writer = csv.writer(fi)
        writer.writerows(rows)


#Hot dog math for Prog & Problem Solving 129 stuff.
from employee import SalaryEmployee, HourlyEmployee, Employee


def test_129():
    packedDog = 10
    #note, always 10 hotdogs 8 buns.
    packedBun = 8
    people = 6
    hotdogPerson = 2
    a = int(input("Enter something"))

    bunPerson = hotdogPerson


    print(math.ceil(22/10))


    totaldog = people * hotdogPerson
    totalbun = people * bunPerson

    print(totaldog)
    leftoverDog = (packedDog - (totaldog % packedDog)) % packedDog
    minNumDog = (totaldog / packedDog) + (0 ^ (0 ^ leftoverDog))
    print(str(minNumDog) + " min left")
    leftoverBun = (packedBun - (totalbun % packedBun)) % packedBun
    print(str(leftoverDog) + " left over dogs and left over buns : "+ str(leftoverBun) + "?")
    return leftoverBun

#Class creation
class animal:
    #constructor sample no args
    def __init__(self):
        self.age = 0
        self.name = 0
    #constructor with args
    def __init__(self, ageArg, nameArg):
        self.age = ageArg
        self.name = nameArg

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def setName(self, stringtest):
        self.name = stringtest

    def setAge(self, valuetest):
        self.age = valuetest

    def functiontest(self):
        print("In a function - also changed values age and name")
        self.age = 22
        self.name = "stick"

#Sub-class of Animal.
class Dog(animal):
    breed = ""

    def setBreed(self, breed):
        self.breed = breed

    def getBreed(self):
        return self.breed

def words(n,words=[""]):
    nums = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r"],
        "8": ["s", "t", "u"],
        "9": ["v", "w", "x"],
    }
    if n == 0:
        return words
    new_words = [""]
    rem=n%10
    if rem == 0 or rem == 1:
        return []
    for i in nums.get(rem, []):
        for j in words:
            new_words.append(i+j)
    return words(n//10,new_words)

# Complicated but not complicated phone converting.
# Using a dictionary key "Number" values list of letters for the key.
def print_phone():
    num = int(input('Enter Phone Number'))
    for i in words(num):
        print(i)

# Press the green button in the gutter to run the script.
def typeTest():
    val2 = 0
    print(val2)
    val2 = float(input("Enter any number: "))
    print(val2)

#file IO
def grades():
    gradefile = open('grades.txt', 'w')
    # initialization phase
    total = 0  # sum of grades
    grade_counter = 0  # number of grades entered

    # processing phase
    grade = int(input('Enter grade, -1 to end: '))  # get one grade

    while grade != -1:
        grade_str = str(grade) + "\n"
        gradefile.write(grade_str)
        total += grade
        grade_counter += 1
        grade = int(input('Enter grade, -1 to end: '))

    # termination phase
    gradefile.close()
    if grade_counter != 0:
        average = total / grade_counter
        print(f'Class average is {average:.2f}')
    else:
        print('No grades were entered')


def collatz(n):
    if n % 2 == 0:
        print(n // 2)
        collatz(n // 2)
    if n % 2 == 1:
        if n == 1:
            return
        print (3*n + 1)
        collatz(3*n + 1)

def cointoss():
    numberOfStreaks = 0
    coinFlip = []
    streak =  0
    for experimentNumber in range(100):
        # Code that creates a list of 100 'heads' or 'tails' values.
        for i in range(100):
            coinFlip.append(random.randint(0, 1))
        # does not matter if it is 0 or 1, H or T, peas or lentils. I am going to check if there is multiple 0 or 1 in a row

        # Code that checks if there is a streak of 6 heads or tails in a row.
        for i in range(len(coinFlip)):
            if i == 0:
                pass
            elif coinFlip[i] == coinFlip[i - 1]:  # checks if current list item is the same as before
                streak += 1
            else:
                streak = 0

            if streak == 6:
                numberOfStreaks += 1



    print('Chance of streak: %s%%' % (numberOfStreaks / (100 * 10000)))

class NearEarthObject:
    """This class represents a near earth object"""
    def __init__(self, designation, name, diameter, hazardous, approaches):
        self.hazardous = hazardous
        self.diameter = diameter
        self.designation = designation
        self.name = name
        self.approaches = approaches
        self.fullname = designation + "(" + name + ")"
        if len(name) == 0:
            self.fullname = designation

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, designation):
        self._designation = designation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self,diameter):
        self._diameter = diameter

    @property
    def hazardous(self):
        return self._hazardous

    @hazardous.setter
    def hazardous(self, hazardous):
        self._hazardous = hazardous

    @property
    def approaches(self):
        return self._approaches

    @approaches.setter
    def approaches(self, approaches):
        self._approaches = approaches

    def __str__(self):
        return f'NEO {self.fullname} has a diameter of {self.diameter:.3f} ' \
            f'km and {"is" if self.hazardous == True else "is not"} potentially hazardous'

def sec_to_hours(seconds):
    hour=str(seconds//3600)
    min=str((seconds%3600)//60)
    sec=str((seconds%3600)%60)
    strformat=["{} hours {} mins {} seconds".format(hour, min, sec)]
    return strformat

def fantasyGame():
    #stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    displayInventory(inv)

    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)

def displayInventory(inventory):
        print("Inventory:")
        item_total = 0
        for k, v in inventory.items():
            print(f'{v} {k}')
            item_total += v

        print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
        for item in addedItems:
            inventory.setdefault(item, 0)
            inventory[item] += 1
        return inventory

def hanoi(n, src,dest,extra):
    if n == 1:
        print("Move disk 1 from source", src, "to destination", dest)
        return
    hanoi(n - 1, src, extra, dest)
    print("Move disk", n, "from source", src, "to destination", dest)
    hanoi(n - 1, extra, dest, src)

def sqlthings():
    cur = os.getcwd()
    conn = create_dbconnection(cur+'/test.db')
    #Creating a table - I only needed to do this once to generate it. Call it again if needed I guess.
    # sql_createtable = """CREATE TABLE IF NOT EXISTS books(
    # book_id integer,
    # author_full_name text,
    # publication_date text,
    # book_title text,
    # num_copies integer);
    # """
    bookID = input("Enter book ID:")
    author_name = input("Enter author name:")
    pubdate = input("Input publication date (mm/dd/yyyy):")
    book_title = input("Input book title:")
    num_copies = input("Input number of copies:")
    # Build the SQL Statement, then we can add on the variables in the execute function call.
    sql_insert = "insert into books(book_id, author_full_name, publication_date, book_title, num_copies) values (?,?,?,?,?)"

    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert, (bookID, author_name, pubdate, book_title, num_copies))
        # Always commit, if forgotten, database not updated.
        conn.commit()
    except Error as e:
        print(e)

def create_dbconnection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def printsql():
    cur = os.getcwd()
    conn = create_dbconnection(cur + '/test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    """
    CSV Employee Lab
    """
    csvPassword()

    """
    SQL stuff - building/inserting variables into table
    Also a lazy printing table method.
    Prog & Problem Solving II Final maybe?
    """
    #sqlthings()
    #printsql()

    """
    Object Explanation and example, Abstraction stuff as well.
    Demonstrating new object creation, printing a 'toString' but in Python, using __str__
    Dump of examples of objects in Python basically.
    """
    #no = NearEarthObject('testden', 'name', 45, 'yes', 'approaches')
    #no.hazardous = "yesss"
    #print(no.name)
    #print(no.__str__())

    #emp1 = SalaryEmployee("Jane", 555, 50000)
    #print(repr(emp1))
    #emp2 = HourlyEmployee("John", 120, 15, 14)
    #print(repr(emp2))
    #this is supposed to throw a type error.
    #emp3 = Employee("Bill frickin gates", 1)
    #print(repr(emp3))

    #animal1 = animal(5, "brick")
    #animal2 = animal(2,"reggie")
    #print(animal1.getName(), animal1.getAge())
    #print(animal2.getName(), animal2.getAge())
    #animal1.setName("brick Jr")
    #animal1.setAge(6)
    #print(animal1.getName(), animal1.getAge())
    #dog1 = Dog(3,"Shadow")
    #dog1.setBreed("Lab")
    #print(dog1.getName(),dog1.getAge(),dog1.getBreed())

    """
    Fantasy game, kill a dragon get loot, this is just merging a list into a dictionary.
    Uses addToInventory and displayInventory
    addToInvetory will add an item if it exists in the dictionary, first it checks by setting a default of 0.    
    """
    # fantasyGame()
    """
    Type explaining - input as float, adding to string.
    Object as variable.
    """
    #x = float(input("guythd?"))
    #print("my str " + str(x))

    # typeTest()
    # a = test_129()
    # print(a)

    """
    Very bare bones dictionary example and how it works calling prints of key-value pairs.
    """
    #mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
    #yourdict = mydict
    #yourdict["elephant"] = 999
    #print(mydict["elephant"])

    """
    Solution to the 'Tower of Hanoi' Puzzle.
    We want the solution on the third rod, C, so we change the order of rods in this call here.
    If we want solution on second rod, B, the order is A B C. 
    3 is the number of disks. Uses Recursion.
    """
    #hanoi(3, 'A','C','B')

    """
    Printing out all valid telephone numbers to words, such as 212-272-5263 becomes a-1-barb-lane
    """
    #print_phone()

    """
    File I/O - Open a file / blank file and fill it with stuff.
    """
    #grades()

    """
    Algorithm for Collatz Number, recursion stuff.
    """
    #n = int(input("Collatz #"))
    #collatz(n)

    """
    Seconds to hours, reinventing the wheel for use in projects Programming & Problem Solving (129/131). 
    """
    #ans = sec_to_hours(5765)
    #print(ans)

    """
    Generates a huge list of randomly tossed coins, checks for streaks of 6.
    """
    #cointoss()

