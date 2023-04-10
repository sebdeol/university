mysql;
USE COMPANY1;

-- 1
-- This query lists all employees with a salary between 1,000 and 2,000 (included).
-- It displays the Employee Name, Department, and Salary.
SELECT ENAME AS "Employee Name", DEPT.DNAME AS "Department", EMP.SAL AS "Salary"
FROM EMP
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO
WHERE EMP.SAL BETWEEN 1000 AND 2000;
-- End of 1

-- 2
-- This query counts the number of people in department 30
-- who receive a salary and the number of people who receive a commission.
SELECT COUNT(CASE WHEN SAL IS NOT NULL THEN 1 END) AS "Salary Count",
       COUNT(CASE WHEN COMM IS NOT NULL THEN 1 END) AS "Commission Count"
FROM EMP
WHERE DEPTNO = 30;
-- End of 2

-- 3
-- This query extracts the name and salary of employees working from the Dallas location.
SELECT ENAME AS "Employee Name", SAL AS "Salary"
FROM EMP
JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO
WHERE LOC = 'Dallas';
-- End of 3

-- 4
-- This query lists all the departments that do not have any employees.
SELECT DNAME AS "Department"
FROM DEPT
WHERE DEPTNO NOT IN (SELECT DISTINCT DEPTNO FROM EMP);
-- End of 4

-- 5
-- This query lists the department number and the average salary of each department.
SELECT DEPTNO AS "Department Number", AVG(SAL) AS "Average Salary"
FROM EMP
GROUP BY DEPTNO;
-- End of 5