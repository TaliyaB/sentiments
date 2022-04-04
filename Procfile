web: gunicorn sentsys.wsgi --log-file -
web: python sentsys/manage.py collectstatic
web: gunicorn sentsys.wsgi
web: python sentsys/manage.py runserver