# Documentation
1. Basic requirements for running backend locally
	- python3
	- python3-venv
	- pip 
2. Running it
	- create a virtual environment with:
		`python3 -m venv venv` in /backend/django folder, which will generate a couple of files
	- run your virtual env with `source venv/bin/activate`
	- Once inside venv, install all dependencies with:
  `pip install -r ./backend/django/requirements.txt`
	- download wordnet database with: `python manage.py download_wordnet` command