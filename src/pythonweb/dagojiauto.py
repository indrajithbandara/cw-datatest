while read line;do
    echo'kill '$line;
    kill $line;
done < /tmp/celeryd.pid

while read line;do
    echo'kill '$line;
    kill $line;
done < /tmp/runserver.pid
ps -ef | grep runserver | awk '{print $2;}' | xargs -i -t kill {}

git pull

pip install -r requirements.txt -i http://pypi.douban.com/simple

cur_time=$(date +%Y%m%d%H%M%s)
db_name=/tmp/db/dkhs_${cur_time}.json
echo ${db_name}

if [ -d /tmp/db ]
then 
    echo '/tmp/db exists'
else
    mkdir /tmp/db 
    echo '/tmp/db create success'
fi

# backup database dkhs
python coresite/manage.py dumpdata --format=json accounts conference socialgraph portfolio statuses > ${db_name}

# drop all table except finace table
mysql -h 192.168.107.253 -udkhs_data -pdkhs_data -e "use dkhs; show tables;" | egrep -v "finance|Tables_in_dkhs" | xargs -i -t mysql -h 192.168.107.253 -udkhs_data -pdkhs_data -e "use dkhs;SET foreign_key_checks = 0;drop table if exists {}"

# syncdb without init data
python coresite/manage.py syncdb --noinput --migrate --no-initial-data 

# syncdb with init data
#python coresite/manage.py syncdb --noinput --migrate

# use backupdata recover database
python coresite/manage.py loaddata ${db_name}

# insert local client id
python coresite/manage.py loaddata coresite/coresite/fixtures/initial_data.json


##mysql -uroot -proot -e "drop database if exists dkhs ;create database dkhs character set utf8;"
##python coresite/manage.py syncdb --noinput --migrate
##mysql -uroot -proot dkhs < ~/init_stock.sql
##echo "from accounts.models import User; User.objects.create_superuser('dkhs', 'dkhs@dkhs.com', 'dkhs')" | coresite/manage.py shell


export C_FORCE_ROOT="1"
python coresite/manage.py celeryd -l info -f /tmp/celeryd.log --pidfile=/tmp/celeryd.pid &


python coresite/manage.py runserver 0.0.0.0:8000 &
echo $! > /tmp/runserver.pid