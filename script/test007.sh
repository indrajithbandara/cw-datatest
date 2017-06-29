#/bin/bash
#7.如果/export/um_lpp_source下有文件，那么将其文件系统大小改为3G
while line=`ls /export/um_lpp_source`
do
        if test $line=""
        then  echo "NULL"
             sleep 1
    else echo $line
                chfs -a size=3G /export/um_lpp_source
                 exit 0
        fi
done
