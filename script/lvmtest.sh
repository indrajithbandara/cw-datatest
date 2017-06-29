############################################
fdisk /dev/vda      此处一定要创建为扩展分区，方便下面的题目；新建逻辑分区修改为
partprobe /dev/vda
~]#makeswap  /dev/vda5
~]#vim /fstab
UUID=        swap swap 0 0
~]#reboot
~]#fdisk -l  # 验证swap分区大小

##########################################
卷组：datastore      16M 默认4M
逻辑卷组：database    10个PE
挂载点：/mnt/database
文件系统格式：ext4
~]#fdisk /dev/vda
8e
~]#pvcreate /dev/vda6
~]#vgcreate  datastore  -s 16M  /dev/vda6
~]#vgdisplay datastore  # 查看
~]#lvcreate -n database -l 10  datestore
~]#lvdisplay /dev/dastore/database
~]#mkfs.ext4 /dev/dastore/database
~]#mkdir /database
~]#blkid /dev/datastore/database
~]#vim  /fstab
~]#mount -a
~]# df -hT
重启下看下