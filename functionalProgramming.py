# CSE-3342 Spring 2019
# PA07: Functional Programming
# Instructor: Naseer Jan
# Name: Eric Miao

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

for x in employees:
    temp = dict(x)
    print(temp.get("job"))

#print(employees)
def ifSamePosition(x):
    if x == "manager":
        return True
    else:
        return False

result = filter(ifSamePosition,employees)

for x in result:
  print(x)
