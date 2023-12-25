Investment Ledger
==========
App to display ledger for a customer 

### Tech Stack
- `django` version 1.9.6 - [documentation](https://docs.djangoproject.com/en)
- `python` version 2.7.5
- 
### Maintaining requirements
- requirements.txt

Local setup
===========
```bash
# Clone repository
git clone git@github.com:tanay1298/investment_ledger.git
# set `DEBUG=True` if not set, for all loggings on console
# keep `PRODUCTION_MODE=False` if not set

# install virtual environment
pip install --user virtualenv
# Now need to create virtual environment 
virtualenv -p /usr/bin/python venv
# now first activate virtual environment
# make sure venv folder is in current folder
source venv/bin/activate
# Now whenever you install any package will be insalled in venv folder

# Now install all the dependencies
pip install -r requirements.txt

# Now you can start server
# replace 3000 for desired port
python manage.py runserver 0.0.0.0:3000
```

```bash
# Some commands for debugging
# make sure virtualenv is activated

# Open django shell
python manage.py shell

# While development, when any model is modified
python manage.py makemigrations
# reflect changes to database
python manage.py migrate

# To deactivate virtualenv
deactivate
