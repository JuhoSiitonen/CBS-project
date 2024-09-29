# Cyber security base course project 

Repository for 2024 Cyber security base course project.

This project is made with Python using Django framework to showcase 5 security flaws and the ways to fix them in a web application. 

The web application itself is a basic forum where users can post topics and comment on them. It is possible to give upvotes for topics. 

Vulnerabilities demonstrated in app are according to OWASP 2017 listing.

1. A1:2017-Injection
[Vulnerable code segment](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/pages/views.py#L23)

Injection vulnerabilities are on the top of the 2017 OWASP list and for good reason. This specific vulnerability can have a malicious actor send in data which can cause data loss, corruption or leaking of sensitive data. Without proper preventative measures all the data within a services databases are at risk. 
For my application the injection is in the form an SQL injection. The injection can happen because the user input is not properly sanitized. Within the code segment link provided you can see that the code uses a user input "text" directly and proceeds to even use the Django ORM model in a very bad way. The bad way being a raw SQL statement which inserts the unsanitized input to the database. This way of interacting with the user data can cause malicious actors to inject SQL code directly into the HTML text box. 
The raw query which is run is not the easiest to inject as was with the course materials (e.g via a SELECT query with LIKE) but this is nevertheless a very careless way to interact with the users input and puts the services data in precarious situation.

Below the vulnerable section is a commented out section with a better way of interacting with the user input. This utilizes the use of the ORM model Django provides. This in conjunction with the Django forms sanitizes the user input of escape characters and thus renders the most obvious injection methods useless. 


2. A2:2017-Broken Authentication
[Vulnerable session management](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/CBSproject/settings.py#L15)
[Custom session manager code](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/CBSproject/sessionmanager.py#L1)



3. A5:2017-Broken Access Control
[Missing access control](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/pages/views.py#L73)

4. A7:2017-Cross-Site Scripting (XSS)
[Direct use of user input](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/pages/views.py#L23)

5. CSRF
[Missing CSRF middleware](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/CBSproject/settings.py#L52)
[Missing CSRF Token](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/pages/templates/pages/posting.html#L19)