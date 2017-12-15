#!/usr/bin/env python

import psycopg2

DBNAME = 'news'


def execute_query(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        db.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def top_three_stories():
    """Fetching results that display the most popular 3 articles of all time"""
    query = """SELECT title, COUNT(title) AS views
                 FROM articles, log
                WHERE concat('/article/', articles.slug) = log.path
             GROUP BY title
             ORDER BY views desc limit 3;"""
    results = execute_query(query)
    for title, views in results:
        print(' {} - {} views '.format(title, views))


def top_authors():
    """Fetching results that display the top 3 authors of all time"""
    query = """SELECT name, COUNT(path) AS views
                 FROM authors, articles, log
                WHERE authors.id = articles.author
                  AND concat('/article/', articles.slug) = log.path
             GROUP BY name
             ORDER BY views desc;"""
    results = execute_query(query)
    for name, views in results:
        print(' {} - {} views '.format(name, views))


def high_errors():
    """Fetching results to display which days had more than 1% of requests
        leading to errors"""
    query = """SELECT *
                 FROM errorlog where "%" > 1;"""
    results = execute_query(query)
    for result in results:
        print(" {} - {}% errors".format(result[0], result[1]))


def main():
    """Running queries and printing all results in reader-friendly format"""
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
