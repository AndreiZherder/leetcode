SELECT a.name as Employee
FROM Employee as a
INNER JOIN Employee as b ON a.managerId = b.id
WHERE a.salary > b.salary