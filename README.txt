1. make virtual env
    mkdir ~/work/db_server_env
    cd ~/work/db_server_env
    virtualenv --no-site-packages --distribute --python=/usr/bin/python3.5 .

2. install required packages in virtual env
    source ~/work/db_server_env/bin/activate
    pip3.5 freeze
    (should be nothing here....)
    pip3.5 install -r ~/work/db_server/pip-requirements.txt
    pip3.5 freeze
    (check installed packages...)
    deactivate

2.1 insatll mysqlclient-1.3.9
  a. download whl file from http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
  (if python35 32bit : mysqlclient-1.3.9-cp35-cp35m-win32.whl)
    python -m pip install mysqlclient-1.3.9-cp35-cp35m-win32.whl

  b. enter mysql console
    mysql -u root -p

  c. create database (data_app is database name)
    drop database data_app;
    create database data_app default character set utf8;

  d. ubuntu mysql installation
    sudo apt-get install mysql-server
    sudo apt-get install libmysqlclient-dev
    sudo apt-get install libpython3.5-dev (try it when installing mysqlclient-1.3.9 is failed)

3. django command example.
  a. use own shell
    cd ~/work/db_server
    ~/work/db_server_env/bin/python manage.py makemigrations data_app
    ~/work/db_server_env/bin/python manage.py migrate
    ~/work/db_server_env/bin/python manage.py createsuperuser
    ~/work/db_server_env/bin/python manage.py runserver
  b. django extension
    a. Werkzeug should be installed, then we can use below command.
        python manage.py runserver_plus
    python manage.py graph_models -a -g -o data_app_visualized.png
  c. OR use virtualenv
    source ~/work/db_server_env/bin/activate
    cd ~/work/db_server
    python manage.py makemigrations data_app
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

4. distribute
  a. nginx
    sudo apt-get install nginx-full
    change app path /home/work/shko/db_server in data_app
    sudo cp data_app /etc/nginx/sites-available/.
    sudo ln -s /etc/nginx/sites-available/data_app /etc/nginx/sites-enabled
    sudo service nginx restart

  b. uwsgi
    sudo pip3.5 install uWSGI==2.0.15
    change path variables (chdir, home) in uwsgi.ini
    change ExecStart, emperor in uwsgi.service file
    sudo cp uwsgi.service /etc/systemd/system/.
    sudo service uwsgi start
    sudo systemctl enable uwsgi (only once)
    sudo systemctl status uwsgi (check)

  c. uwsgi test
    sudo uwsgi uwsgi.ini  (just for test)
    uwsgi --http :8888 --home /home/shko/work/db_server_env/ --chdir /home/shko/work/db_server/ --module data_server.wsgi


