1. make virtual env
    mkdir ~/work/db_server_env
    virtualenv --no-site-packages --distribute --python=/usr/bin/python3.5 .

2. install required packages in virtual env
    source ~/work/db_server_env/bin/activate
    pip3.5 freeze
    (should be nothing here....)
    pip3.5 install -r ~/work/db_server/pip-requirements.txt
    pip3.5 freeze
    (check installed packages...)
    deactivate

3. run django
    ~/work/db_server_env/bin/python manage.py makemigrations
    ~/work/db_server_env/bin/python manage.py migrate
    ~/work/db_server_env/bin/python manage.py createsuperuser
    ~/work/db_server_env/bin/python manage.py runserver
