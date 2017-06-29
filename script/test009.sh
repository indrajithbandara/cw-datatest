#/bin/sh
a=2
while name="test.log"
do
        sleep 1
        b=$(ls -l $name | awk '{print $5}')
        if test $b -ge $a
        #then echo "OK"
    then `cp /opt/*.tar.gz .`
        exit 0
        fi
done