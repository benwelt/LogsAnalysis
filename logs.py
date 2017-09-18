#!/usr/bin/env python3

import psycopg2
import json

DBNAME = "news"

questions = [
            "What are the 3 most popular articles of all time?",
            "Who are the most popular authors of all time?",
            "On which days did more than 1% of requests lead to errors?"
            ]

q1 = """SELECT articles.title,COUNT(*) FROM articles,log WHERE log.path like
    concat('%' ,articles.slug) group by articles.title
    order by count desc limit 3"""

q2 = """SELECT authors.name,COUNT(*) FROM articles,authors,log WHERE
    articles.author = authors.id AND log.path like concat('%' ,articles.slug)
    group by authors.name order by count desc"""

q3 = """SELECT DATE(time), ROUND(100.00 * SUM(CASE status WHEN '200 OK'
    THEN 0 ELSE 1 END)/COUNT(status),2) AS Percent GROUP BY DATE(time)
    ORDER BY Percent DESC"""

# Holds the result of the query
query_result = {}

# Execute query
def query_log(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()
