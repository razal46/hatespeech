# Hatespeech Final Project
---

## How to start the app?

### Prerequisite
- Python

### First time starting
- Download ML model (sentimental_model.joblib) from [here](https://drive.google.com/file/d/13_B1qK7pK3MZOjzZfb7hb7u0hqVPCFXP/view?usp=drive_link)
- Copy that file into the ```detect``` folder
- Run these commands in the terminal
```bash
python -m venv venv
.\venv\Scripts\activate

python -m spacy download en_core_web_sm

python ./manage.py makemigrations
python ./manage.py migrate

python ./manage.py runserver
```

### Starting later on
- Run these commands in the terminal
```bash
.\venv\Scripts\activate
python ./manage.py runserver
```