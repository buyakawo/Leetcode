-- Write your PostgreSQL query statement below
-- self join: e1 is table of employees and e2 is table of managers
SELECT e1.name AS Employee
FROM Employee e1
JOIN Employee e2
ON e1.managerId=e2.id
WHERE e1.salary>e2.salary;
