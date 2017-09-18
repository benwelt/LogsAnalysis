#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

q1 = "What are the 3 most popular articles of all time?"
query_1 = """SELECT articles.title,COUNT(*) FROM articles,log WHERE log.path
    LIKE concat('%' ,articles.slug) GROUP BY articles.title
    ORDER BY count DESC LIMIT 3"""

q2 = "Who are the most popular authors of all time?"
query_2 = """SELECT authors.name,COUNT(*) FROM articles,authors,log WHERE
    articles.author = authors.id AND log.path LIKE concat('%' ,articles.slug)
    GROUP BY authors.name ORDER BY count DESC LIMIT 3"""

q3 = "On which days did more than 1% of requests lead to errors?"
query_3 = """SELECT * FROM Percent WHERE Percent > 1"""


# Execute query
def query_log(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()


def print_result(results):
    print(results[0])
    for result in results[1]:
        print("\t" + str(result[0]) + ' - ' + str(result[1]) + ' views.')
    print("\n")


def print_error_result(results):
    print(results[0])
    for result in results[1]:
        print("\t" + str(result[0]) + " - " + str(result[1]) + "% Error Rate.")
    print("\n")


if __name__ == '__main__':
    query_1_result = q1, query_log(query_1)
    query_2_result = q2, query_log(query_2)
    query_3_result = q3, query_log(query_3)

    print_result(query_1_result)
    print_result(query_2_result)
    print_error_result(query_3_result)
