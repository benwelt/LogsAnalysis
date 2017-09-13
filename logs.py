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

# Who are the most popular authors of all time?
q2 = """SELECT authors.name,COUNT(*) FROM articles,authors,log WHERE
    articles.author = authors.id AND log.path like concat('%' ,articles.slug)
    group by authors.name order by count desc"""

# On which days did more than 1% of requests lead to errors?
#q3 = """SELECT DATE(time),COUNT(*) FROM log WHERE
#    status LIKE '4%' OR status LIKE '5%' group by DATE(time)"""

# Holds the result of the query
query_result = {}

# Execute query
def query_log(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    result = c.execute(query)
    return result
    db.close()
