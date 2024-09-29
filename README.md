# Cyber security base course project 

Repository for 2024 Cyber security base course project.

This project is made with Python using Django framework to showcase 5 security flaws and the ways to fix them in a web application. 

The web application itself is a basic forum where users can post topics and comment on them. It is possible to give upvotes for topics. 

Vulnerabilities demonstrated in app are according to OWASP 2017 listing.

1. A1:2017-Injection

Injection vulnerabilities are on the top of the 2017 OWASP list and for good reason. This specific vulnerability can have a malicious actor send in data which can cause data loss, corruption or leaking of sensitive data. Without proper preventative measures all the data within a services databases are at risk. 
For my application the injection is in the form an SQL injection. 
[https://vscode.dev/github/JuhoSiitonen/CBS-project/blob/main/CBSproject/pages/views.py#L23](Vulnerable code)



2. A2:2017-Broken Authentication

3. A5:2017-Broken Access Control

4. A7:2017-Cross-Site Scripting (XSS)

5. CSRF