RHCSA考试：
破解root密码
# e
# console=tty0 rd.break
# ctrl + x
# mount -o remount,rw /sysroot
#chroot /sysroot/
#passwd root
#touch /.autorelable
#exit 两次
 
设置主机名、ip地址、子网掩码、DNS服务器
~]#vim /etc/hostname
~]#hostname HOSTNAME
~]#bash
方法一：~]# nmtui
方法二：# vim  /etc/sysconfig/network-scripts/ifcfg-.en0
BOOTPROTO=static
ONBOOT=yes
IPADDR0=
GATEWAY0=
DNS1=
~]#systemctl restart network
检查;
~]#ip addr show      172.25.0.10/24
~]#ip route
~]#cat /etc/resolve.conf            172.25.254.254
~]#ping
 
 
1.Selinux设置在Enforcing
~]# vim /etc/selinux/config
SELINUX=disabled
SELINUXTYPE=targeted
~]# reboot  重启让SElinux重新配置生效 
或者  setenforce 1 设置为强制
 
 
2.配置yum源
~]# vim /etc/yum.repos.d/xxx.repo
[BASE]
name=
baseurl=
enable=1
gpgchck=0
 
 
3.调整逻辑卷
~]# cat /etc/fstab   # 看其分区文件格式
~]#lvextend /dev/vg/xxxxx -L 300M
重读文件系统：
XFS：  ~]# xfs_growfs   挂载点
EXT4：  ]# resize2fs  分区
 
 
4.创建用户和组
~]#groupadd adminuser
~]#useradd -G adminuser natasha
~]#useradd -G adminuser harry
~]#useradd -s /sbin/nologin sarah
~]#echo "RedHat" | passwd --stdin natasha
~]#echo "redhat" | passwd --stdin harry
~]#echo "redhat" | passwd --stdin sarah
 
 
5.复制并配置权限
~]#cp  /etc/fstab /var/tmp/fstab
~]#chown root.root /var/tmp/fstab
~]#chown a-x /var/tmp/fstab
~]#setfacl -m u:natasha:rw /var/tmp/fstab
~]#setfacl -m u:natasha:--- /var/tmp/fstab
 
 
6.cron job
~]#crontab -e -u natasha
23 14 * * *    /bin/echo hjya
 
 
7.创建目录更改权限
~]#mkdir -pv /home/admins
~]#chown .adminuser /home/adminuser
~]#chmod g+w  /home/adminuser
~]#  chmod o-rx  /home/adminuser
~]#chmod g+s /home/adminuser
~]#ll -d /home/admins
drwxrws---
 
8.YUM升级内核
~]#vim vim /etc/yum.repos.d/xxx.repo
[kernel]
name=
baseurl=http://server.domain11.example.com/pub/updates
enable=
gpgcheck=
~]#uname -r
~]#yum install kernel
~]#reboot
 
 
9.LDAP服务
~]# id ldapuser1  # 此时会下那是为空用户
~]# yum install  sssd authconfig-gtk -y  # sssd服务、认证图形化界面
~]# authconfig-gtk &  图形化配置
      复制相关内容
wKiom1cbki7yRs0eAACE5-fW12Y886.png

10.NTP服务
~]#yum install chrony -y
~]#yum install -y  system-config-date
~]#system-config-date &
wKiom1cbki6RPYXaAABy9ZdMuoY977.png
~]# chronyc sources -v
 
 
11.autofs自动挂载LDAP
~]#yum install -y autofs
~]# systemctl enable autofs  # 开机启动
~]# getent passwd ldapuser1 # 查看用户的信息，关键是看其挂载位置
~]#vim /etc/auto.master
增加：/home/guests    /etc/auto.ldap
说明：/home/guests服务目录，该目录不需要创建，由autofs自动创建
~]#vim  /etc/auto.ldap
ldapuser1      172.25.254.254:/home/guests/ldapuser1
或者：*      172.25.254.254:/home/guests/&
~]#systemctl restart autofs
~]#su -ldapuser1
 
 
12.创建用户修改密码
~]#useradd -u 3400 alex
~]#echo "redhat" | passwd --stdin alex
 
 
13.创建交换分区
~]# fdisk /dev/vda      此处一定要创建为扩展分区，方便下面的题目；新建逻辑分区修改为
~]#partprobe /dev/vda
~]#makeswap  /dev/vda5
~]#vim /fstab
UUID=        swap swap 0 0
~]#reboot
~]# fdisk -l  # 验证swap分区大小
 
 
14.find应用
~]#mkdir -pv /root/findresults
~]#find / -user ira -exec  cp -rfp {}  /root/findresults/  \;
 
 
15.复制行：cat + 管道重定向
~]# cat  /usr/share/dict/words | grep seismic > /root/lines
 
 
16.tar压缩
~]# tar jvcf /root/backup.tar.bz2 /etc/*
 
 
17.创建逻辑卷
卷组：datastore      16M 默认4M
逻辑卷组：database    10个PE
挂载点：/mnt/database
文件系统格式：ext4
~]#fdisk /dev/vda
8e
~]#pvcreate /dev/vda6
~]#vgcreate  datastore  -s 16M  /dev/vda6
~]# vgdisplay datastore  # 查看
~]#lvcreate -n database -l 10  datestore
~]#lvdisplay /dev/dastore/database
~]#mkfs.ext4 /dev/dastore/database
~]#mkdir /database
~]#blkid /dev/datastore/database
~]#vim  /fstab
~]#mount -a
~]# df -hT
重启下看下