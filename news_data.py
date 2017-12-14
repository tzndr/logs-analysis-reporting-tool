#Query for 1st problem
select title, count(title) as views from articles, log where concat('/article/', articles.slug)
= log.path group by title order by views desc limit 3;

#Query for 2nd problem
select name, count(path) from authors, articles, log where authors.id = articles.author
and concat('/article/', articles.slug) = log.path group by name order by count desc;

#Query for 3rd problem
select * from errorlog where "%" > 1.0;
