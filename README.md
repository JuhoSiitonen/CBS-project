# Cyber security base course project 

Repository for 2024 Cyber security base course project.

This project is made with Python using Django framework to showcase 5 security flaws and the ways to fix them in a web application. 

The web application itself is a basic forum where users can post topics and comment on them. It is possible to give upvotes for topics. 

Vulnerabilities demonstrated in app are according to OWASP 2017 listing.

## Installation
To run the app you need to navigate to CBS-PROJECT/CBSproject folder and run the following command in:
bash appsetup.sh

This will run a shell script which will create a database with two default users. The usernames and their passwords are:
username: Juho   password: badpassword1234
username: Pertsa password: badpassword1234

## Vulnerabilities

1. A1:2017-Injection
[Vulnerable code segment](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/pages/views.py#L23)

Injection vulnerabilities are on the top of the 2017 OWASP list and for good reason. This specific vulnerability can have a malicious actor send in data (which in fact is usually raw SQL with escape characters) which can cause data loss, corruption or leaking of sensitive data. Without proper preventative measures (being the sanitization of the user sent data) all the data within a services databases are at risk. 

For my application the injection is in the form an SQL injection vulnerability. The injection can happen because the user input is not properly sanitized. Within the code segment link provided you can see that the code uses a user input "text" directly and proceeds to even use the Django ORM model in a very bad way. The bad way being a raw SQL statement which inserts the unsanitized input to the database. This way of interacting with the user data can cause malicious actors to inject SQL code directly into the HTML text box. 
The raw query which is run is not the easiest to inject as was with the course materials (e.g via a SELECT query with LIKE) but this is nevertheless a very careless way to interact with the users input and puts the services data in a precarious situation.

Below the vulnerable section is a commented out section with a better way of interacting with the user input. This utilizes the use of the ORM model Django provides. This in conjunction with the Django forms sanitizes the user input of escape characters and thus renders the most obvious injection methods useless. 


2. A2:2017-Broken Authentication
[Vulnerable session management](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/CBSproject/settings.py#L15)
[Custom session manager code](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/CBSproject/sessionmanager.py#L1)

Broken authentication is as the number 2 in the OWASP 2017 list. According tp the OWASP list Broken authentication presents itself usually in session management which is fundamental in stateful applications. By gaining access to the session management the attacker can compromise the whole system very quickly.

In my project broken authentication presents itself in the way of a very bad session management function. To make this work I had to add my own sessionmanager function to the backend settings and of course create the said function within the project. The bad sessionmanager makes it so that the session cookie is just a running counter integer starting from 0. This makes it so that a malicious actor can basically guess the sessioncookie system and then proceed to capture other users sessions and act on their behalf on the service. 

To fix this problem the recommended and easiest solution would be to remove the vulnerable sessionmanager from backend settings and instead use the Django default sessionmanagement. This would create an encrypted session cookie which would be very difficult to brute force. Another solution would be to make a more robust custom sessionmanager function which would utilize encryption and a much longer unique sessioncookie which could not be "guessed" by a malicious user. 


3. A5:2017-Broken Access Control
[Missing access control](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/pages/views.py#L73)

Broken access control stands as the fifth entry in the OWASP 2017 list. According to OWASP broken access control presens itself usually as a lack of automated detection of access credentials. This can lead to attackers modifying data in ways which compromise the system. 

Within my project broken authentication presents itself as the lack of a check for a logged in user within the /like endpoint. Within the project this does not make for a huge loophole for malicious users but it opens the gate for using something like Postman to make POST reguests to the /like endpoint and thus make repeated upvotes for a posting within the app. 

To fix this vulnerability one would only need to uncomment the line to which the link point to within the code. Meaning the decorator which invokes the Django default login check middleware functionality. This could also be implemented with a custom middleware which checks the users privileges. 

4. A7:2017-Cross-Site Scripting (XSS)
[Direct use of user input]()

Cross-site scripting stands as the number seven on the OWASP 2017 list. According to OWASP it is the second most prevalent issue on the list. The vulnerability means that there is a way for an attacker to store unsanitized input which will be executed as a part of a victims HTML output.  

Within my project the cross-site scripting vulnerability presents itself as a vulnerability within the HTML code when a user is posting comments. This vulnerability makes it possible for a user to add a comment which is not sanitized in when presented to the user and thus the user commenting is able to post something like HTML script tags and run malicious javascript code on another users browser.

To fix this vulnerability it is recommended not to use the "|safe" in conjunction with showing the comments in the HTML code. Without the |safe added to the template Django would automatically sanitize inputs like script tags and just showcase them as plain text. With the addition of telling Django it is safe to print out whatever the user came up with it is possible to use script tags as you are basically telling Django not to intervene. 
The Django forms (within the forms.py) also sanitize the user input for escape characters and other unsafe inputs which could embed for example javascript code into the database and thus present it through the application to other unsuspecting users within the HTML output (if |safe is used).

5. CSRF
[Missing CSRF middleware](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/CBSproject/settings.py#L52)
[Missing CSRF Token](https://github.com/JuhoSiitonen/CBS-project/blob/8681984f882e1c74e884756496c19ffa59ca5a23/CBSproject/pages/templates/pages/posting.html#L19)

CSRF vulnerability isn't a part of the OWASP lists but due to its profound impact on web development it is allowed on the course to use as an example of a vulnerability. CSRF stands for cross-site request forgery and what it means is that if a service uses POST forms without a CSRF Token an attacker can force the end user to execute unwanted actions within the service. This can be accomplished in many ways but one instance of it is with a malicious email attachment which when downloaded can use the users logged in credentials (session cookies etc) within the browser to execute unwanted actions via a POST request. 

In the project CSRF vulnerability presents itself in two portions of the codebase. Because Django has a default middleware setting to check for CSRF Token it is required to comment it out in the backend settings to be able to make this specific vulnerability. This accompanied with a form which does not use a CSRF Token (the comment form within a specific postings page) created the chance to exploit the CSRF vulnerability witin the POST request. 

To fix this vulnerability the first thing would be to uncomment the Django default project setting for the CSRF middleware. This middleware checks for the CSRF token and if it is present and correct the user is able to post information to the backend. 