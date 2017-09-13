#!/usr/bin/env python3

import psycopg2
import json

DBNAME = "news"

questions = [
            "What are the 3 most popular articles of all time?",
            "Who are the most popular authors of all time?",
            "On which days did more than 1% of requests lead to errors?"
            ]
q1 = ""

# Who are the most popular authors of all time?
q2 = ""

# On which days did more than 1% of requests lead to errors?
q3 = ""

# Holds the result of the query
query_result = {}

# Execute query
def query_log(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    result = c.execute(query)
    return result
    db.close()
