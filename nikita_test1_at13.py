''' ------->PYTHON------------>
1.What is decorator , write a decorator?
a->Decorater is a function
which can take a function as argument and extend its functionality
and return modified function with extend functionality.
example:-

def decore(cal):
    def inner(a,b):
        mul = a*b
        div = a/b
        cal(a, b)
        print('mul:-',mul,'div:-',div)
    return inner

@decore
def cal(a,b):
    sum = a+b
    sub = a-b
    print('sum is:-',sum,'sub is:-',sub)

cal(30,50)

2.Whatis lambda expression, write a lambda expression?
a->
syntex->
var = lambda argument/parameter list:body/expression
example->
sum = lambda a,b:a+b
print(sum(10,20))

3.WAF, S=‘Helloeveryone’, count the occurrence of each char, return those
 repetitive character , without using any inbuilt function.
 a->
s= "Helloeveryone"
freq = {}
for ele in s:
    if ele in freq:
        freq[ele] += 1
    else:
        freq[ele] = 1
print ("Occurrence  is:- "+ str(freq))
4. WAF,Reverse a string words.
 > Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function?
a->
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "hello world"

print("original string is : ", end="")
print(s)

print(" reversed string is : ", end="")
print(reverse(s))

5.WAF, input= ‘aaabbaacd’ output= ‘3a2b2a1c1d’
a->
a = input()
l = int(len(a))
c = int()
b = str()
i = 0
while c <l:
    if a[i] == a[c]:
        c += 1
    else:
        b += (a[i] + str(c-i))
        i = c
b += (a[i] + str(c-i))
print(b)


6.Sort a list integer element without using inbuilt function?
a->
number = [1,9,8,90,6]
for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]
print (number)

7.Li = [1,2,3], Li2 = [10,20,30]
 Result = {1:10,2:20,3:30}
 Take a two list a parameter, return dictionary, look like above result.

li1= [1,2,3]
li2= [10,20,30]

dict1 = dict(zip(li1, li2))
print(dict1)

8. Handel a csv file, write first_name , email, phn_no, insert 5 data in this csv, then read
 the csv and print in console bar?
a->
import csv
print(dir(csv))


with open('pathname_url','w',newline='') as var:
 w = csv.writer(var)
     w.writerow(['FNAME','EMAIL','PHONE'])
     n = int(input('Enter number of DATA'))
     for i in range(n):
         FNAME= input('Enter fNAMEr:-')
         EMAIL = input('Enter EMAIL:-')
         PHONE = int(input('Enter PHONE_NO:-'))

         w.writerow([FNAME,EMAIL,PHONE])
TO READ-->
import csv
with open('PATHNAMEOF_CSV','r') as var:
    data = csv.reader(var)
    sort_data = list(data)
    # print(sort_data)
    for i in sort_data:
        for j in i:
            print(j)

9.Whatis exception handling , how handel the exception in python , explain with each
 block?
a->
-An unwanted and unexcepted event that distrubs normal flow of program is called  Exception.
ex:-ZeroDivisionError,TypeError,ValueError,FileNotFoundError
-The main objective of exception handeling grecful Termination of the program.
-Exception Handeling is only applicable for runtime Errors not for syntax errors.
-the code which may raise exception is called risky code
and we have to take risky code inside try block.
The corresponding handeling code we have to take inside except block.
syntax:-
try:
	Risky code
except NameOfException:
	Handeliing code/Alternative Code
finally:
The finally block is used to execute code whether an exception was raised or not.

10. Difference between Moudle and Packages (3 diff)
a->
Modules:- 1)A group of functions, variables and classes saved a file,
which is nothing but a module and it's in build.
2)ex:- math, os, sys, functools, unittest etc.
3)module is a single file containing Python code.
Packages :- 1)It is an encapsulation mechanism to group related modules in a single unit,
it's a package of module. It's look like a folder and it’s contain several python files(.py)
and __init__.py(imp)
2)Ex:- pandas, numpy, pytest, tenserflow etc
3)a package is a collection of modules that are organized in a directory hierarchy.

11. Difference between List vs tuple vs set vs dictionary?
List:-
[1,2,"a"]
1)it is  Mutable (modifiable).
2)Allows duplicates
3)A list can be created using the list() function or simple assignment to [].
tuple:-
(1,2,3)
1)it is Immutable (non-modifiable)
2)Allows duplicates
3)Tuple can be created using the tuple() function.
set:-
{"a","b"}
1)Mutable, but elements inside must be immutable
2)Allows Only unique elements
3)A set can be created using the set() function.
dictionary:-
{key:value,key:value}
1)it is Mutable, keys are immutable, but values can change
2)Unique keys, values can be duplicated.
3)A dictionary can be created using the dict() function.

12. What is Garbage Collection?
-The process of automatic deletion of unwanted or unused objects to free the memory
is called garbage collection in Python.
-A garbage collection in Python manages the memory automatically and
heap allocation.

13. What is list comprehension , write code in list comprehension?
List comprehension is a concise way to create a new list based on the values
of an existing list.
ex-numbers = [1, 2, 3, 4]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

14. Difference between Shallow copy vs Deep Copy?
shallow copy-
Shallow Copy stores the references of objects to the original memory address.
Shallow Copy reflects changes made to the new object in the original object.
Shallow Copy stores the copy of the original object and points the references to the objects.
A shallow copy is faster.
deep copy-
Deep copy stores copies of the object’s value.
Deep copy doesn’t reflect changes made to the new/copied object in the original object.
Deep copy stores the copy of the original object and recursively copies the objects as well.
Deep copy is slower.

15. Explain break, continue, pass with code?
break:-The break statement in Python terminates the current loop and resumes execution
at the next statement.
count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1
continue:-The continue statement in Python returns the control to the beginning of the while loop.
The continue statement rejects all the remaining statements in the current iteration of the loop
 and moves the control back to the top of the loop.
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue
    print(count)
pass:-The pass statement in Python is used when a statement is required syntactically but do
not want any command or code to execute
def function_placeholder():
    pass

'''

'''
-------------->SQL------------>

1. Explain about the DML,DDL,TCL,DQL commands?
DML:-
Data Manipulation Language 
DML is used for inserting, deleting, and updating data in a database. It is used to retrieve and 
manipulate data in a relational database. It includes INSERT, UPDATE, and DELETE.  
DDL:-
Data Definition Language
In SQL DDL commands are used to create and modify the structure of a database and database 
objects. These commands are CREATE, DROP, ALTER, TRUNCATE, and RENAME.                                                                                   
TCL:-
Transaction Control Language
TCL includes statements that are used to manage the changes that are made from DML statements. 
It enhances the transactional nature of SQL. The TCL commands in SQL are: commit, rollback, savepoint 
DQL:-
Data Query Language
DQL commands are used for fetching data from a relational database. They perform read-only queries of data. 
SELECT command selects the attribute based on the condition described by the WHERE clause and returns them.

 2. What is join, explain about the all joins?
 ans->
Join is an operation in DBMS(Database Management System) that combines the row of two or more tables 
based on related columns between them.
The main purpose of Join is to retrieve the data from multiple tables
Types of Join
1. Inner Join:-Inner Join is a join operation in DBMS that combines two or more tables based on related columns 
and returns only rows that have matching values among tables.
Inner join of two types. are Conditional join and Natural join
2. Outer Join:-Outer join is a type of join that retrieves matching as well as non-matching records from related tables.
There are three types of outer join
Left outer join
Right outer join
Full outer join
 
3. Difference between Joins vs Subquery?
a->
join-
A JOIN is a means for combining fields from two tables by using values common to each.
joins are faster then subquery.
subquery-
A subquery is a query nested inside another query and is used to return data that will be used in the main query as 
a condition to further restrict the data to be retrieved. 
subquery are slower then joins.

4. Find 3rd Highest Salary Of employee table ?
a->SELECT * FROM employee ORDER BY salary DESC LIMIT 1 OFFSET 2;

5. Find the top seller in this month, according to date in customer table?
a->SELECT TOP 5  item_id , items_sold  
FROM sales_details ORDER BY  items_sold DESC

6. Difference between Rank vs Dense_rank?
RANK() assigns the same rank to rows with equal values, leaving gaps.
DENSE_RANK() assigns the same rank to equal values without gaps, resulting in consecutive ranks.

'''

'''
----------->UNIX------->
 1. Copy a file one directory to another directory?
 a->cp dir1/file1.txt dir2
 
 2. How do you find the process IF(PID) of a running process.
 a->ps -e | grep process_name
 
 3. difference between chown vs chmod?
 a->chown is used to change the ownership of a file while chmod is for changing the file mode bits.  
 chmod allows you to set Read, Write, Execute Permissions, chown enables you to change who the owner of the file is.

 4. In adirectory a find a file name abc.txt?
 a->ls -d abc  #list all files containing --abc--
 
 5. Why we are using sed command?
 a->sed is a stream editor, and it can be used to edit text files, with its most common use being to replace occurrences
  of words in a files. This is extremely helpful in situations where a configuration file has a lot of instances of
   the same word that needs replacing throughout the file.
 
 6. How to list directories in Unix?
 a->ls
To list only directories, you can use the -d option in combination with a wildcard (*/)
ls -d */
 
'''

'''---------->SELENIUM-------->
 1. Whatis webdriver?
 A->webdriver intract with real web browser,it is connecting our code to browser
 
 2. Howtohandel selective dropdown, write a snippet for it?
 A->
 driver = webdriver.Chrome() 
 driver.get('URL')
 dropdown_element = driver.find_element(By.ID, 'dropdown-id')
 select = Select(dropdown_element)
 select.select_by_visible_text('Option 1') 
 
 3. Howtohandel auto suggestive dropdown, write a snippet for it.?
 A->
 
 4. Howtohandel multiple windows and back to current window?
 A->
 
 5. WhatStaleElementException?
 A->when the page is refreshed or navigated away and then returned to, the original element reference becomes invalid.
 ,Dynamic content
 
 6. Explain the wait mechanism, write syntax and snippet for it.
 A->
 Web pages sometime load elements asynchronously and elements might not be immediately available for interaction 
when a script is executed. To handle this  Selenium provides wait mechanisms
1)Implicit Wait
2)Explicit Wait
3)Fluent Wait

 
 7. Howtohandle dynamic web element, (write at least 3 point)
 A->
 
 8. Howmanylocators in selenium?
 A->There are 8 types of the locators in selenium
1. ID
2. NAME
3. CLASS NAME
4. TAG NAME
5. LINK TEXT
6. PARTIAL LINK TEXT
7. XPATH
10. Absolute xpath

 9. In webtable want to fetch 3rd Column , 3rd row data, write a xpath for it.
A->driver.find_element(By.XPATH, "//table[@id='example-table']//tr[4]/td[3]")

10. Write xpath
A->
TO NAVIGATE->


'''
















