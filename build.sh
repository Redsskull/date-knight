set -o errexit
pip install -r requirements.txt
cd theme/static_src/
npm install
npm run build
cd ../..
python manage.py collectstatic --noinput
python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser --no-input