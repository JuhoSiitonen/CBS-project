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

Broken authentication is as the number 2 in the OWASP 2017 list. According tp the OWASP list Broken authentication means 

In my project broken authentication presents itself in the way of a very bad session management function. To make this work I had to add my own sessionmanager function to the backend settings and of course create the said function within the project. The bad sessionmanager makes it so that the session cookie is just a running counter integer starting from 0. This makes it so that the 

To fix this problem the recommended and easiest solution would be to remove the vulnerable sessionmanager from backend settings and instead use the Django default sessionmanagement. This would create an encrypted session cookie which would be very difficult to brute force. Another solution would be to make a more robust custom sessionmanager function which would utilize encryption and a much longer unique sessioncookie which could not be "guessed" by a malicious user. 


3. A5:2017-Broken Access Control
[Missing access control](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/pages/views.py#L73)

Broken access control stands as the fifth entry in the OWASP 2017 list. According to OWASP broken access control means

Within my project broken authentication presents itself as the lack of a check for a logged in user within the /like endpoint. Within the project this does not make for a huge loophole for malicious users but it opens the gate for using something like Postman to make POST reguests to the /like endpoint and thus make repeated upvotes for a posting within the app. 

To fix this vulnerability one would only need to uncomment the line to which the link point to within the code. Meaning the decorator which invokes the Django default login check middleware functionality. This could also be implemented with a custom middleware which checks the users privileges. 

4. A7:2017-Cross-Site Scripting (XSS)
[Direct use of user input](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/pages/views.py#L23)

Cross-site scripting stands as 

Within my project the cross-site scripting vulnerability presents itself as a another vulnerability within the injection vulnerable code. This vulnerability makes it possible for a user to add a posting which is not sanitized and thus the user is able to post something like HTML script tags and run malicious javascript code on another users browser.

To fix this vulnerability it is recommended to use Django forms to sanitize user input. Within my project the version of the form with Django forms is commented out. This also applies to the views function code for the index endpoint where code changes are required to use the Django forms. The Django forms sanitize the user input for escape characters and other unsafe inputs which could embed for example javascript code into the database and thus present it through the application to other unsuspecting users.

5. CSRF
[Missing CSRF middleware](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/CBSproject/settings.py#L52)
[Missing CSRF Token](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/pages/templates/pages/posting.html#L19)

CSRF vulnerability isn't a part of the OWASP lists but due to its profound impact on web development it is allowed on the course to use as an example of a vulnerability. CSRF stands for cross-site request forgery and 

In the project CSRF vulnerability presents itself in two portions of the codebase. Because Django has a default middleware setting to check for CSRF Token it is required to comment it out in the backend settings to be able to make this specific vulnerability. This accompanied with a form which does not use a CSRF Token (the comment form within a specific postings page) created the chance to exploit the CSRF vulnerability. 

To fix this vulnerability the first thing would be to uncomment the Django default project setting for the CSRF middleware. This middleware checks for the CSRF token and if it is present and correct the user is able to post information to the backend. 