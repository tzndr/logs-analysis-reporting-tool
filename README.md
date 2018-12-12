# Logs Analysis Internal Reporting Tool
A Python program using PostgreSQL to query a news site database for specific results
## About
The Logs Analysis project is the 3rd project of the Full Stack Nanodegree program from Udacity.
It is a program written in Python 3 that sends three specific PostgreSQL queries to a large news website database
(containing over a million rows of data through 3 multi-columned tables) and returns the results in
a reader-friendly format with sorted data. It answers "What are the three most popular articles of all time and how many views has each received?", Who are the most popular authors of all time and how many views has each received?", and "On which days did more than 1% of requests lead to errors and what was the percentage?". Each query is dynamic in that they require the joining of tables or the use of views to return complex answers from many different units of data within the database.</p>

## Running the Program
1. Download and install <a href='https://www.virtualbox.org/'>Virtual Box</a>
1. Download and install <a href='https://www.vagrantup.com/downloads.html'>Vagrant</a>
1. Clone this repository and place <code>news_data.py</code> inside your vagrant directory
1. Download the <a href='http://bit.ly/2y4PPQy'>Newsdata Database</a> and place newsdata.sql inside your Vagrant directory
1. Navigate <code>cd</code> to your Vagrant directory within your terminal
1. Execute the command <code>vagrant up</code>
1. Follow with the command <code>vagrant ssh</code>
1. Import the news database by running <code>psql -d news -f newsdata.sql</code>
1. Access the database with <code>psql news</code> and create the required SQL views (see below)
1. Exit the database with <code>\q</code>
1. Run the program <code>python news_data.py</code>

<h1>Required Views</h1>
<h4>errorview:</h4>
<p><code>CREATE VIEW errorview AS
         SELECT time::date AS day, COUNT(status) AS errors
         FROM log
         WHERE status != '200 OK'
         GROUP BY day
         ORDER BY day;
   </code>

<h4>totalview:</h4>
<p><code>CREATE VIEW totalview AS    
         SELECT time::date AS day, COUNT(status) AS total
         FROM log
         GROUP BY day
         ORDER BY day;
   </code>

<h4>errorlog:</h4>
<p><code>CREATE VIEW errorlog AS    
         SELECT (to_char(errorview.day, 'Mon DD, YYYY')), round(((errorview.errors*1.00)/(totalview.total)*100), 2)
         AS percent
         FROM errorview
         JOIN totalview
         ON errorview.day = totalview.day
         ORDER BY percent desc;
   </code>
