# What is this?

A simple Django 1.8.2 app with Python Social Auth that demonstrates the following issue.

https://github.com/omab/python-social-auth/issues/644

You need your own client id and secret.

https://console.developers.google.com/

```
$ export SOCIAL_AUTH_GOOGLE_OPENIDCONNECT_KEY='(Client ID Here).apps.googleusercontent.com'
$ export export SOCIAL_AUTH_GOOGLE_OPENIDCONNECT_SECRET='(Your Client Secrete here)'
$ ./manage.py runserver 8080
```
