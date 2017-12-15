#!/usr/bin/env python

import psycopg2

DBNAME = 'news'


def top_three_stories():
    """Fetching results that display the most popular 3 articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("""SELECT title, COUNT(title) AS views
                        FROM articles, log
                       WHERE concat('/article/', articles.slug) = log.path
                    GROUP BY title
                    ORDER BY views desc limit 3;"""
                   )
    results = cursor.fetchall()
    db.close()
    for row in results:
        print(' {} - {} views '.format(results[0], results[1]))



def top_authors():
    """Fetching results that display the top 3 authors of all time"""
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


def high_errors():
    """Fetching results to display which days had more than 1% of requests
        leading to errors"""
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


def main():
    """Printing all results in reader-friendly format"""
    print('\n''\n'' The Top 3 Articles of All Time are:''\n')
    top_three_stories()
    print('\n''\n''\n'' The Most Popular Authors of All Time are:''\n')
    top_authors()
    print('\n''\n''\n'' The Days in which More than 1% of Requests Led '
          'to Errors:''\n')
    high_errors()
    print('\n''\n'' End of Report''\n')

if __name__ == '__main__':
    main()
