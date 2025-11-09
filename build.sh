pip cache purge
# Installer les dépendances
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# Collecter les fichiers statiques
python manage.py collectstatic --noinput


