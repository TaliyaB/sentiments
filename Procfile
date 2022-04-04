web: git clone https://github.com/TaliyaB/sentiments
web: pip install .
web: python sentsys/manage.py collectstatic
web: gunicorn sentsys.wsgi
web: python sentsys/manage.py runserver