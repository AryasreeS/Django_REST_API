echo "create migrations"
python manage.py makemigrations todos

echo "migrate"
python manage.py migrate


echo "run server"
python manage.py runserver 0.0.0.0:8000