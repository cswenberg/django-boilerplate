# A Boilerplate for Django Applications
## Installation
Stack
- python3
- virtualenv
- react
- postgres

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Development

Highly encouraged to use [autoenv](https://github.com/kennethreitz/autoenv). Set up environment by:

```bash
cp env.template .env
```

To run django locally:

```bash
python manage.py runserver
```

## Setting up the Postgres Server (macos)

Guide provided by [Robin weiruch](https://www.robinwieruch.de/postgres-sql-macos-setup/)

### First time setup
Installation with homebrew

```bash
brew install postgres
```

Initialize physical space on hard drive for databases (should be done automatically)

```bash
initdb /urs/local/var/postgres
```

Start our PostgreSQL database

```bash
pg_ctl -D /usr/local/var/postgres start
```

### Database setup
Create our database

```bash
createdb db_name
```

Connect to our database to begin setup

```bash
psql db_name
```

This should have brought you into the psql shell, noted by a `psql=#`

Create our database user (same name as the DB_USER environment variable)

```bash
CREATE USER db_user
```

Note: You can give the db_user a password by adding ```PASSWORD db_password``` at the end of the previous command

We have now initialized our postrgres database with our user and can now begin running our django app

Leave the psql shell with

```bash
\q
```

## Making changes to models

When making changes to your models, you will need to let django migrate them with:

```bash
python manage.py makemigrations
python manage.py migrate
```

The first command will create the migrations for your changes and the second will apply them to your database

## Adding and admin user

```bash
python manage.py createsuperuser
```

Follow the prompt to create your username, email, and password
