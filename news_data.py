#!usr/bin/env python

import psycopg2

DBNAME = 'news'


# Fetching results that display the most popular 3 articles of all time
def top_three_stories():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("""SELECT title, COUNT(title) AS views
                        FROM articles, log
                       WHERE concat('/article/', articles.slug) = log.path
                    GROUP BY title
                    ORDER BY views desc limit 3;"""
                   )
    row_1 = cursor.fetchone()
    row_2 = cursor.fetchone()
    row_3 = cursor.fetchone()
    print(' {} - {} views '.format(row_1[0], row_1[1]))
    print(' {} - {} views '.format(row_2[0], row_2[1]))
    print(' {} - {} views '.format(row_3[0], row_3[1]))
    db.close()


# Fetching results that display the top 3 authors of all time
def top_authors():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("""SELECT name, COUNT(path) AS views
                        FROM authors, articles, log
                       WHERE authors.id = articles.author
                         AND concat('/article/', articles.slug) = log.path
                    GROUP BY name
                    ORDER BY views desc;"""
                   )
    row = cursor.fetchone()
    while row is not None:
        print(' {} - {} views '.format(row[0], row[1]))
        row = cursor.fetchone()
    db.close()


# Fetching results to display which days had more than 1% of requests
# leading to errors
def high_errors():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("""SELECT *
                        FROM errorlog where "%" > 1;"""
                   )
    row = cursor.fetchone()
    while row is not None:
        print(" {} - {}% errors".format(row[0], row[1]))
        row = cursor.fetchone()
    db.close()

# Printing all results in reader-friendly format
print('\n''\n'' The Top 3 Articles of All Time are:''\n')
top_three_stories()
print('\n''\n''\n'' The Most Popular Authors of All Time are:''\n')
top_authors()
print('\n''\n''\n'' The Days in which More than 1% of Requests Led '
      'to Errors:''\n')
high_errors()
print('\n''\n'' End of Report''\n')
