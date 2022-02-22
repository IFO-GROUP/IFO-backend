IFO-GROUP backend

Commands

python3 -m venv env 
source env/bin/activate

pip install -r requirements.txt

./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver




<!-- second time -->

source env/bin/activate

./manage.py makemigrations
./manage.py migrate
./manage.py runserver