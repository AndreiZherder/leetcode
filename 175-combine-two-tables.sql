SELECT Person.firstName, Person.LastName, Address.city, Address.state
FROM Person LEFT OUTER JOIN Address ON Person.personId = Address.personId