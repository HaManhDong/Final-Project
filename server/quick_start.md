
### **Quick start**

Create tables in database:

```sh
$ python manage.py migrate
```

Create pas (Persons Authentication System) app:

```sh
$ python manage.py startapp pas
```

Add ***database models*** in file ***models.py***, and then make migration for pas app:

```sh
$ python manage.py makemigrations pas
```
To check SQL command to migrate file **initial.py**, run command:

```sh
python manage.py sqlmigrate pas initial.py
```

If you’re interested, you can also run [`python  manage.py  check`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-check) this checks for any problems in your project without making migrations or touching the database.

Now, run **migrate** again to create those model tables in your database:

```sh
$ python manage.py migrate
```
