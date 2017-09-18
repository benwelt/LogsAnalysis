# Logs Analysis
Udacity full stack web developer Logs Analysis project.
___

## Prerequisites
1. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant](https://www.vagrantup.com/)
3. [A terminal, such as Git Bash](https://git-scm.com/downloads)
4. [Udacity VM Configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
5. [Project Starter Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

##### VM Installation
1. Install VirtualBox then Vagrant
2. Unzip the VM configuation and `cd` into the `vagrant` folder
3. Start the VM by typing the command `vagrant up` (it may take a few minutes to run)
4. When the VM is running type `vagrant ssh` in the terminal to log in

##### Database Setup
1. Unzip the project starter data into the `vagrant` directory
2. Login to the VM and use the command `psql -d news -f newsdata.sql` to create and connect to the database
___
## Analyze the Log

The project requires 3 questions to be answered by using SQL to query the `news` database and print their outputs.
* What are the 3 most popular articles of all time?
* Who are the most popular authors of all time?
* On which days did more than 1% of requests lead to errors?

##### Create a View
This view will need to be created in the database before running the `logs.py` script to generate the query results.
```sql
CREATE VIEW Percent AS SELECT DATE(time), ROUND(100.00 * SUM(CASE status
WHEN '200 OK' THEN 0 ELSE 1 END)/COUNT(status),2) AS percent FROM log GROUP BY
DATE(time) ORDER BY percent DESC;
```
The view contains the error percentages of each day in the `log` table.

##### Running the Script
* Exit the database view in the terminal
* Run the command `python3 logs.py`

The output should look like this:
```
What are the 3 most popular articles of all time?
        Candidate is jerk, alleges rival - 338647 views.
        Bears love berries, alleges bear - 253801 views.
        Bad things gone, say good people - 170098 views.


Who are the most popular authors of all time?
        Ursula La Multa - 507594 views.
        Rudolf von Treppenwitz - 423457 views.
        Anonymous Contributor - 170098 views.


On which days did more than 1% of requests lead to errors?
        2016-07-17 - 2.26% Error Rate.
```
