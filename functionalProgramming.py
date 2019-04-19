# CSE-3342 Spring 2019
# PA07: Functional Programming
# Instructor: Naseer Jan
# Name: Eric Miao

import functools

#employees is a set of list that contains employement infomation
employees = [
  { "empno": 7369, "name": "Smith",  "job": "clerk", 		"manager": 7902, "hiredate": "17-DEC-1980", "sale": 800,  "comm": 0, 		"deptname": "RESEARCH"},
  { "empno": 7499, "name": "Allen",  "job": "salesman", 	"manager": 7698, "hiredate": "20-FEB-1981", "sale": 1600, "comm": 300, 		"deptname": "SALES"},
  { "empno": 7521, "name": "Ward",   "job": "salesman", 	"manager": 7698, "hiredate": "22-FEB-1981", "sale": 1250, "comm": 500, 		"deptname": "SALES"},
  { "empno": 7566, "name": "Jones",  "job": "manager", 	    "manager": 7839, "hiredate": "02-APR-1981", "sale": 2975, "comm": 0, 		"deptname": "RESEARCH"},
  { "empno": 7698, "name": "Blake",  "job": "manager", 	    "manager": 7839, "hiredate": "01-MAY-1981", "sale": 2850, "comm": 0, 		"deptname": "SALES"},
  { "empno": 7782, "name": "Clark",  "job": "manager", 	    "manager": 7839, "hiredate": "09-JUN-1981", "sale": 2450, "comm": 0, 		"deptname": "ACCOUNTING"},
  { "empno": 7788, "name": "Scott",  "job": "analyst", 		"manager": 7566, "hiredate": "19-APR-1987", "sale": 3000, "comm": 0, 		"deptname": "RESEARCH"},
  { "empno": 7839, "name": "King",   "job": "president", 	"manager": 0,    "hiredate": "17-NOV-1981", "sale": 5000, "comm": 0, 		"deptname": "ACCOUNTING"},
  { "empno": 7844, "name": "Turner", "job": "salesman", 	"manager": 7698, "hiredate": "08-SEP-1981", "sale": 1500, "comm": 0, 		"deptname": "SALES"},
  { "empno": 7876, "name": "Adams",  "job": "clerk", 		"manager": 7788, "hiredate": "23-MAY-1987", "sale": 1100, "comm": 0, 		"deptname": "RESEARCH"},
  { "empno": 7900, "name": "James",  "job": "clerk", 		"manager": 7698, "hiredate": "03-DEC-1981", "sale": 950,  "comm": 0, 		"deptname": "RESEARCH"},
  { "empno": 7934, "name": "Miller", "job": "clerk", 		"manager": 7782, "hiredate": "23-JAN-1982", "sale": 1300, "comm": 0, 		"deptname": "ACCOUNTING"},
  { "empno": 7902, "name": "Ford",   "job": "analyst", 		"manager": 7566, "hiredate": "03-DEC-1981", "sale": 3000, "comm": 0, 		"deptname": "RESEARCH"},
  { "empno": 7654, "name": "Martin", "job": "salesman", 	"manager": 7698, "hiredate": "28-SEP-1981", "sale": 1250, "comm": 1400, 	"deptname": "SALES"}
];

# This function will get "sale" number from each row/set from the employees list
def get_sale(x):
    temp = dict(x)
    return temp.get("sale")

print("Step I: Using map to get all sale number")
j = map(get_sale, employees)
for i in j:
    print(i)
print()



# Each of the GETTER below will translate the input parameter (x) into dictionary and get particular row from the employees list

def get_managers(x):
    temp = dict(x)
    if temp.get("job") == "manager":
        return temp.get("sale")


def get_salesmen(x):
    temp = dict(x)
    if temp.get("job") == "salesman":
        return temp.get("sale")


def get_analysts(x):
    temp = dict(x)
    if temp.get("job") == "analyst":
        return temp.get("sale")


def get_clerks(x):
    temp = dict(x)
    if temp.get("job") == "clerk":
        return temp.get("sale")


def get_president(x):
    temp = dict(x)
    if temp.get("job") == "president":
        return temp.get("sale")


#The fileter function below will get paticular rows and store them into a list
print("Step II: Using filter function to sort all employees by job title")
all_manager = list(filter(get_managers, employees))
all_clerk = list(filter(get_clerks, employees))
all_analyst = list(filter(get_analysts, employees))
all_salesman = list(filter(get_salesmen, employees))
all_president = list(filter(get_president, employees))
print("Managers: ")
for i in all_manager:
    print(i)
print()

print("Clerks: ")
for i in all_clerk:
    print(i)
print()

print("Analysts: ")
for i in all_analyst:
    print(i)
print()

print("Salesmen: ")
for i in all_salesman:
    print(i)
print()

print("President: ")
for i in all_president:
    print(i)
print()


print("Step III: Using reduce function to ")
import functools
j = list (map(get_sale, employees))








