安装nginx

首先添加nginx_signing.key(必须，否则出错)
$ wget http://nginx.org/keys/nginx_signing.key

$ sudo apt-key add nginx_signing.key
添加]Nginx](http://nginx.org/)官方提供的源
$ echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" 

$ echo "deb-src http://nginx.org/packages/ubuntu/ trusty nginx" 
更新源并安装Nginx
$ sudo apt-get update

$ sudo apt-get install nginx
安装Nginx完成后可查看版本号，输入

$ /usr/sbin/nginx -v
安装mysql

$ sudo apt-get install mysql-server-5.7 mysql-client-5.7
途中会提示设置MySQL的密码，安装好后：

$ mysql -uroot -p
 
然后输入刚刚设置的密码，能成功进入即成功安装。
安装nodejs

apt install nodejs
apt install npm

npm install -g n

# 安装最新版本
n latest

# 如果安装失败，有可能是被墙了，比如安装失败的版本是 7.7.3
# 先删除
n - 7.73
 
然后再执行 
n latest

# 如果安装不成功，或者运行失败（Segmentation Fault），反复先删除版本，再次安装，网上的帖子说，安装过程中可能出了问题，所以需要重新安装。。。
部署node程序

# 切换源
npm config set registry https://registry.npm.taobao.org 

# 上传文件
# -r 表示上传整个目录，否则就是上传文件
scp -r  mac路径地址 ubuntu@118.89.106.201: 服务端路径

# 安装 pm2
sudo npm install pm2 -g

# 切换到代码库下，
npm install 
sudo pm2 index.js
linux指令

# 登陆
ssh ubuntu@118.89.106.201

# 查看当前目录 全路径
pwd

# 删除目录
rm -rf dist  

# 移动目录
sudo mv server ../server

# 备份文件
sudo cp nginx.conf nginx.conf.bak

# 重启nginx
sudo service nginx reload

# 开放8080端口
sudo ufw allow  8080
mysql操作

# 先开放mysql端口
sudo ufw allow  3306
mac下载Sequel Pro通过ssh连接mysql，创建表结构等数据即可。