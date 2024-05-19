## How to run this application on localhost

1. Clone the repo
1. Rename `.env.default` file to `.env`.
1. Run `npm run sass:build`
1. Create a virtual env and activate it.
1. Run `python manage.py migrate`
1. Run `python manage.py runserver`
1. Open http://localhost:8000 in your browser.

NOTE: By default this will use sqlite3 database, but you can modify `.env` file to use mysql.
