import psychopg2

DBNAME = 'newsdata.sql'

#Fetching results for question 1
def top_three_stories():
    db = psychopg2.Connect(database = DBNAME)
    cursor = db.cursor()
    cursor.execute( "SELECT title, COUNT(title) AS views
                       FROM articles, log
                      WHERE concat('/article/', articles.slug) = log.path
                   GROUP BY title
                   ORDER BY views desc limit 3;"
                   )
    print(cursor.fetchall())
    db.close()


#Query for 2nd problem
  SELECT name, COUNT(path) AS views
    FROM authors, articles, log where authors.id = articles.author
         AND concat('/article/', articles.slug) = log.path
GROUP BY name
ORDER BY views desc;

#Query for 3rd problem
SELECT *
  FROM errorlog where "%" > 1;
