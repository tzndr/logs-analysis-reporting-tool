#Query for 1st problem
select title, count(title) from articles, log where concat('/article/', articles.slug)
= log.path group by title order by count desc limit 3;
