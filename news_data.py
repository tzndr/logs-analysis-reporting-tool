import psychopg2

DBNAME = 'newsdata.sql'

#Fetching results that display the most popular 3 articles of all time
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

#Fetching results that display the top 3 authors of all time
def top_authors():
    db = psychopg2.Connect(database = DBNAME)
    cursor = db.cursor()
    cursor.execute( "  SELECT name, COUNT(path) AS views
                         FROM authors, articles, log where authors.id = articles.author
                          AND concat('/article/', articles.slug) = log.path
                     GROUP BY name
                     ORDER BY views desc;"
                   )
    print(cursor.fetchall())
    db.close()

#Fetching results to display which days had more than 1% of requests leading to errors
def high_errors():
    db = psychopg2.Connect(database = DBNAME)
    cursor = db.cursor()
    cursor.execute( "  SELECT *
                       FROM errorlog where "%" > 1;"
                   )
    print(cursor.fetchall())
    db.close()
