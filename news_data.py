#Query for 1st problem
   SELECT title, COUNT(title) AS views
     FROM articles, log
    WHERE concat('/article/', articles.slug) = log.path
 GROUP BY title
 ORDER views desc limit 3;

#Query for 2nd problem
  SELECT name, COUNT(path) AS views
    FROM authors, articles, log where authors.id = articles.author
         AND concat('/article/', articles.slug) = log.path
GROUP BY name
ORDER BY views desc;

#Query for 3rd problem
SELECT *
  FROM errorlog where "%" > 1;
