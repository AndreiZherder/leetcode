SELECT email FROM
    (SELECT email, COUNT(email) as email_cnt
    FROM Person
    GROUP BY email) as a
    WHERE a.email_cnt > 1