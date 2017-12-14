# logs_analysis
A Python program using PostgreSQL to query a news site database for specific results
<br>
<h1>About</h1>
<p>The Logs Analysis project is the 3rd project of the Full Stack Nanodegree program from Udacity. 
   It is a program written in Python 3 that sends three specific PostgreSQL queries to a large news website database 
   (containing over a million rows of data through 3 multicolumned tables) and returns the results in 
   a reader-friendly format. Each query is dynamic in that they require the joining of tables or the 
   use of views to return complex answers from many different units of data within the database.</p>
   
   <h1>Running the Program</h1>
   <ol>
   <li>Download and install <a href='https://www.virtualbox.org/'>Virtual Box</a>
   <li>Downlaod and install <a href='https://www.vagrantup.com/downloads.html'>Vagrant</a>
   <li>Clone this repository and place <code>news_data.py</code> inside your vagrant directory
   <li>Download the <a href='https://goo.gl/6h4bJE'>Newsdata Database</a> and place newsdata.sql inside your Vagrant directory
   <li>Navigate <code>cd</code> to your Vagrant directory within your terminal 
   <li>Execute the command <code>vagrant up</code>
   <li>Follow up with the command <code>vagrant ssh</code>
   <li>Import the news database by running <code>psql -d news -f newsdata.sql</code>
   <li>Access the database with <code>psql news</code> and create the required SQL views (see below)
   <li>Run the program <code>python news_data.py</code>
   </ol>
   
<h1>Required Views</h1>
