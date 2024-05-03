## How to start the app?
---

### Prerequisite
- Python

- First time starting
```bash
python -m venv venv
.\venv\Scripts\activate

python -m spacy download en_core_web_sm

python ./manage.py makemigrations
python ./manage.py migrate

python ./manage.py runserver
```

- Starting later on
```bash
python ./manage.py runserver
```