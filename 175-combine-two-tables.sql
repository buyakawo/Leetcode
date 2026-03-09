-- Write your PostgreSQL query statement below

SELECT p.firstName, p.lastName, Address.city, Address.state,
From Person p,
LEFT JOIN Address a,
ON a.personId=p.personId