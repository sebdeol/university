# README

## Description

This is my implementation for Assignment 1: Part 3.
For this assignement, we have a MySQL database with two different tables, EMP and DEPT. EMP stores employee data and DEPT stores departments information.

The EMP table contains the `EMPNO`, `ENAME`, `JOB`, `MGR`, `HIREDATE`, `SAL`, `COMM`, and `DEPTNO` attributes.
The DEPT table contains `DEPTNO`, `DNAME`, and `LOC` attributes.

I have implemented five different SQL queries to retrieve data from the `EMP` and `DEPT` tables.
The implemented queries perform different operations such as counting, filtering, joining, and aggregating the data directly from the database.

## Implemented Queries

### Query 1
List all employees whose salary is between 1,000 AND 2,000. Show the Employee Name, Department and Salary
I have joined the `EMP` and `DEPT` tables on their common column `DEPTNO` and filtered the results using the `WHERE` clause to only show the employees within the desired salary range.

### Query 2
Count the number of people in department 30 who receive a salary and the number of people who receive a commission.
I have used the `COUNT` function along with a `CASE` statement to count the number of rows that meet the specific conditions (`SAL` or `COMM` not being `NULL`).
I then filtered the results using the `WHERE` clause for department 30.

### Query 3
Find the name and salary of employees in the Dallas office.
I have joined the `EMP` and `DEPT` tables on their common column (`DEPTNO`) and filtered the results using the `WHERE` clause to only show the employees working in the Dallas office.

### Query 4
List all departments that do not have any employees.
I have used a subquery with the `NOT IN` operator to find `DEPTNO` values that are not in the set of `DEPTNO` values in the `EMP` table.
I then filtered the results based on this condition in the `WHERE` clause.

### Query 5
List the department number and average salary of each department.
I have used the `AVG` function to calculate the average salary for each department and the `GROUP BY` clause to group the results by `DEPTNO`.


## Alternative Approaches

Query 1 - Instead of using the `BETWEEN` operator, the first query could also use >= and <= operators to filter the salary range.

Query 2 - The second query could have been implemented using the `COUNT()` function with a `GROUP BY` clause to group the results by `DEPTNO` and then filter the results by `DEPTNO` = 30.

Query 3 - The third query could have been implemented using the `LIKE` operator to filter the locations containing 'Dallas'.

Query 4 - The fourth query could have been implemented using the `LEFT JOIN` and `IS NULL` to join the `EMP` and `DEPT` tables and filter the results where the `EMPNO` is null.

Query 5 - The fifth query could have been implemented using the SUM() and `COUNT()` functions with a `GROUP BY` clause to get the total salary and total number of employees in each department and then divide the total salary by the total number of employees to get the average salary.