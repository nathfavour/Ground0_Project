# Ground0_Project

      INTRODUCTION
This is a simple django project.

It consist of the main project (Ground0_Nathaniel) 
and the simgle site (Nathaniel) folders.

The settings for this prpject are in
Ground0_Nathaniel/settings.py.

The database codes can be found on db.sqlite3

NB: sqlite3 is a lightweight database server that
comes bundled with Django. So it was more convinent.
       OVERVIEW
This site is very simple; when you put your details
in the register page, you are stored as a user.
Then the admin can convert that user to an employee, or manager.
       DATABASE

The codes responsible for the database implementations
are found in Nathaniel/models.py.
The actual site does not implement all of the
database, in terms of the views.

For example, even though there is an Employee database
column for "comment", there is no comment page,
because the codes quickly became complex and I
had to abandon some implement.

It became complex because in my Nathaniel/views.py,
you can see that i am using a mixture of class based views and views
themselves.

I'm still figuring how to properly implement the two.


      WEBSITE
the website for this project has been hosted on
https://ingeniath03.pythonanywhere.com

i was planning extra pages like /login, /comment
but at the last minute, i had to move all the
core functionality to the admin page:
https://ingeniath03.pythonanywhere.com/admin/

Logging into the admin page will give you complete
insight on how the enire site works.

       SECURITY

I didn't take any security measures (apart from the
usual csrf_tokens etc) because this site is 
a practice project.
Although, some functionality is in hidden files 
(__pycache__) that are invisible in the project
     
            LAST WORDS
This project is far from perfect. Revisions, commits
and suggestions will be warmly accepted.
