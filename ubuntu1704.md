 apt install net-tools
    4  apt-get install net-tools
    5  ps -aux
    6  sudo kill 4320 4321
    7  ps -aux|grep apt
    8  sudo kill 4314
    9  ps -aux|grep apt
   10  apt-get install net-tools
   11  ifconfig
   12  python -V
   13  pip -V
   14  apt install python-pip
   15  pip -V
   16  clear
   17  df -h
   18  wget http://www.ubuntukylin.com/applications/showimg.php?lang=cn&id=23
   19  ls
   20  cat /etc/paswd
   21  cat /etc/shadow
   22  clear
   23  ls
   24  ip a
   25  apt-get docker
   26  apt-get docker.io
   27  apt-get install docker.io
   28  docker --version
   29  clearf
   30  clear
   31  git'
   32  git
   33  clear
   34  useradd labuser -u 544
   35  passwd labuser
   36  ls -ll
   37  cat /etc/network/interfaces
   38  vim /etc/network/interfaces
   39  apt install vim
   40  vim /etc/network/interfaces
   41  apt install ssh
   42  ssh-keygen -t rsa 
   43  ls
   44  cd softwareluke/
   45  ls
   46  cd .ssh
   47  cd ..
   48  ls
   49  cd ~
   50  ls
   51  pwd
   52  cd .ssh
   53  ls
   54  cat id_rsa.pub 
   55  cd /opt
   56  ls
   57  git clone git@gitlab.brandwisdom.cn:cloudwisdom/cw-hms-web.git
   58  ls
   59  cd cw-hms-web/
   60  git branch
   61  git branch -a
   62  ls -ll
   63  sudo add-apt-repository ppa:webupd8team/atom 
   64  sudo apt-get install atom
   65  sudo add-apt-repository ppa:webupd8team/atom
   66  uname -a
   67  uname -r
   68  clear
   69  uname -r
   70  reboot
   71  vim /etc/ssh/sshd_config 
   72  passwd root
   73  reboot
   74  ip a
   75  egrep -o '(vmx|svm)' /proc/cpuinfo
   76  docker --versiobn
   77  docker --version
   78  clear
   79  docker images
   80  docker ps -a
   81  apt install lrzsz
   82  rz
   83  cat /proc/cpuinfo
   84  startx
   85  clear
   86  node -v
   87  apt install nodejs
   88  node -v
   89  apt install nodejs-legacy
   90  node -v
   91  npm -v
   92  sudo n stable 
   93  n stable
   94  sudo npm install -g n 
   95  apt install npm
   96  sudo n stable
   97  sudo npm install npm -g
   98  npm -v
   99  java -version
  100  cat etc/profile
  101  cat /etc/profile
  102  clear
  103  apt
  104  apt list
  105  clear
  106  gedit /etc/apt/sources.list
  107  vim /etc/apt/sources.list
  108  apt install vnc-view
  109  apt install vnc
  110  apt-cache search vnc
  111  apt-cache search vnc-view
  112  apt-get install -y tigervnc-viewer
  113  clear
  114  netstat -ntlp
  115  CD /
  116  cd /
  117  ls
  118  cd dev/\
  119  clear
  120  sudo apt-get install filezilla
  121  sudo apt-get install unity-tweak-tool  
  122  sudo apt-get install gnome-tweak-tool 
  123  apt-get install qemu-kvm libvirt-bin virt-manager bridge-utils
  124  apt-get update --fix-missing
  125  cp /etc/apt/sources.list /etc/apt/sources.list_backup
  126  cd /etc/apt
  127  ls
  128  vim sources.list
  129  apt-get update
  130  apt-get update --fix-missing
  131  apt install libvirt-clients
  132  lsmod |grep kvm
  133  virsh -c qemu:///system list
  134  virt-manager
  135  apt install virt-manager
  136  virt-manager
  137  sudo add-apt-repository ppa:noobslab/macbuntu
  138  sudo apt-get update
  139  sudo apt-get install macbuntu-os-icons-lts-v7
  140  cd /root/桌面
  141  ls
  142  ls -ll
  143  chmod 777 VNC-Viewer-6.0.3-Linux-x64.deb 
  144  dpkg -i VNC-Viewer-6.0.3-Linux-x64.deb 
  145  cd .vnc
  146  cd ..
  147  cd .vnc
  148  sudo /etc/init.d/xrdp restart
  149  vncviewer localhost:1
  150  vncviewer
  151  apt install putty
  152  putty
  153  virt-manager
  154  clear
  155  apt install lrzsz
  156  wget
  157  apt install whois
  158  clear
  159  ls
  160  cd /
  161  ls
  162  df -H
  163  sudo add-apt-repository ppa:ubuntu-wine/ppa
  164  lvm
  165  lvdisplay
  166  pvscan
  167  lvm --version
  168  lvm -v
  169  clear
  170  docker --version
  171  docker images
  172  sudo add-apt-repository ppa:webupd8team/atom 
  173  sudo lsb_release -a 
  174  uname -r
  175  apt-get update
  176  sudo apt-get install atom
  177  cat /etc/network/interfaces
  178  cat /etc/selinux/config
  179  apt-get install usbmount
  180  fdisk -l /dev/sda
  181  clear
  182  fdisk -l /dev/sda
  183  mkdir -p /mnt/usb
  184  mount -t vfat  /media/softwareluke /mnt/usb
  185  mount -t msdos  /media/softwareluke /mnt/usb
  186  mount /media/softwareluke /mnt/usb
  187  clear
  188  ls
  189  virt-manager
  190  cd /home/softwareluke/桌面
  191  ls
  192  ls -ll
  193  chmod 777 CentOS-7-x86_64-Minimal-1611.iso 
  194  ls -ll
  195  clear
  196  ls -ll
  197  qemu-img create -f qcow2 centos7.img 5G
  198  ls
  199  chmod 777 centos7.img 
  200  ls -ll
  201  nmcli dev status
  202  virt-install --name=centos7vm --os-variant=cenos7 --ram 512 --vcpus=1 --disk path=/home/softwareluke/桌面/centos7.img,format=qcow2,size=12,bus=virtio --accelerate --cdrom /home/softwareluke/桌面/CentOS-7-x86_64-Minimal-1611.iso.iso --vnc --vncport=5910  --network bridge=virbr0 --noautoconsole
  203  nmcli dev status
  204  clear
  205  wget https://github.com/coreos/etcd/releases/download/v3.0.3/etcd-v3.0.3-linux-amd64.tar.gz
  206  docker search ubuntu
  207  clear
  208  docker images
  209  docker pull ubuntu
  210  curl -L https://github.com/docker/compose/releases/download/1.7.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
  211  docker-compose --vesion
  212  pip install docker-compose
  213  docker-compose --vesion
  214  ls
  215  vim docker-compose.yml 
  216  clear
  217  ansible
  218  ansible --version
  219  cd /opt
  220  ls
  221  vi docker-compose.yml
  222  docker-compose ls
  223  docker-compose ps
  224  touch docker-compose.yml
  225  docker-compose ps
  226  ls
  227  chmod 777 docker-compose.yml 
  228  vim docker-compose.yml 
  229  docker-compose ps
  230  ls
  231  git clone https://github.com/kasperisager/php-dockerized.git
  232  ls
  233  cd php-dockerized/
  234  docker-compose up
  235  cd ..
  236  ls
  237  cd cw-hms-web/
  238  git pull
  239  find . -name "*.java"|xargs cat|grep -v -e ^$ -e ^\s*\/\/.*$|wc -l    #Output:36064  
  240  find . -name "*.js" src|xargs cat|grep -v -e ^$ -e ^\s*\/\/.*$|wc -l  
  241  find . -name "*.js"|xargs cat|grep -v -e ^$ -e ^\s*\/\/.*$|wc -l  
  242  docker images
  243  docker ps -a
  244  docker ps
  245  clear
  246  ls
  247  cd /opt
  248  ls
  249  cd /home/softwareluke/
  250  ls
  251  cd 桌面
  252  ls
  253  chmod 777 ideaIC-2017.1.1.tar.gz 
  254  tar -zxvf ideaIC-2017.1.1.tar.gz 
  255  ls
  256  cd idea-IC-171.4073.35/
  257  ls
  258  clear
  259  ls
  260  cd bin
  261  ls
  262  ./idea.sh 
  263  clear
  264  sudo apt install openjdk-9-jre-headless
  265  java -version
  266  clear
  267  whereis java
  268  docker-compose ps
  269  docker-compose up
  270  gedit /etc/network/interfaces
  271  ls a
  272  lp a
  273  ifconfig -a
  274  virt-manager
  275  gedit /etc/network/interfaces
  276  /etc/init.d/networking restart
  277  gedit /etc/network/interfaces
  278  clear
  279  /etc/init.d/networking restart
  280  ip a
  281  gedit /etc/network/interfaces
  282  /etc/init.d/networking restart
  283  gedit /etc/network/interfaces
  284  /etc/init.d/networking restart
  285  clear
  286  ip a
  287  lspci |grep -i eth
  288  clear
  289  ip a
  290  gedit /etc/network/interfaces
  291  clear
  292  /etc/init.d/networking restart
  293  ip a
  294  /etc/init.d/networking restart
  295  ip a
  296  gedit /etc/network/interfaces
  297  clear
  298  /etc/init.d/networking restart
  299  ip a
  300  clear
  301  ifconfig
  302  nmcli con show
  303  nmtui
  304  clear
  305  nmcli con show
  306  ip a
  307  clear
  308  nmcli dev status
  309  nmcli dev show
  310  virt-manager
  311  ssh 192.168.13.1
  312  exit
  313  dpkg -i teamviewer_12.0.76279.deb 
  314  dpkg -i teamviewer_12.0.76279_i386.deb 
  315  sudo add-apt-repository ppa:noobslab/macbuntu
  316  sudo apt-get update
  317  sudo apt-get install macbuntu-os-icons-lts-v7
  318  apt-get install macbuntu-os-icons-lts-v7
  319  sudo apt-get install macbuntu-os-ithemes-lts-v7
  320  cd /
  321  cd /home/softwareluke
  322  cd 下载
  323  ls
  324  chmod 777 teamviewer_12.0.76279_i386.deb 
  325  dpkg -i teamviewer_12.0.76279_i386.deb 
  326  cd ..
  327  cd 桌面
  328  ls
  329  chmod 777 teamviewer_12.0.76279_i386.deb 
  330  dpkg -i teamviewer_12.0.76279_i386.deb 
  331  sudo apt-get install -f
  332  sudo apt-get install gdebi-core gdebi
  333  uname -a
  334  uname -r
  335  gdebi teamviewer_12.0.76279_i386.deb 
  336  cd /
  337  ls
  338  cd /home/softwareluke/
  339  cd 下载
  340  ls
  341  chmod 777 teamviewer_11.0.65280.dmg 
  342  ls
  343  pwd
  344  teamviewer
  345  cp /home/softwareluke/下载/teamviewer_11.0.65280.dmg .
  346  clear
  347  ls
  348  ls -l teamviewer_11.0.65280.dmg 
  349  rm -f teamviewer_11.0.65280.dmg 
  350  ls
  351  cp /home/softwareluke/下载/teamviewer_11.0.65280.dmg .
  352  ls -ll
  353  ls -ll teamviewer_11.0.65280.dmg 
  354  sudo /usr/bin/teamviewer start
  355  cd /
  356  ssh root@192.168.18.214
  357  apt-get install ksnapshot“
  358  apt-get install ksnapshot
  359  sudo add-apt-repository ppa:shutter/ppa
  360  apt-get update
  361  sudo apt-get install shutter
  362  cd /
  363  ssh root@192.168.18.214
  364  cd /
  365  apt-get install Xmind
  366  clear
  367  ls
  368  df -h
  369  vgdisplay
  370  lvdisplay
  371  fdisk -l
  372  cd /
  373  virt-manager
  374  virt list
  375  virsh list --all
  376  virsh start centos7.0 --console
  377  cd /home/softwareluke/
  378  cd 06-价格设置-DEMO.rar
  379  cd 下载
  380  ls
  381  chmod 777 06
  382  chmod 777 06-价格设置-DEMO.rar 
  383  tar -xf 06-价格设置-DEMO.rar 
  384  clear
  385  ssh root@192.168.18.217
  386  cd /
  387  ls
  388  cd ~
  389  git clone https://github.com/wg/wrk.git
  390  cd wrk/
  391  make
  392  apt install libssl-dev
  393  wrk
  394  apt install wrk
  395  wrk
  396  make install
  397  clear
  398  wrk -t12 -c100 -d30s http://192.168.18.214
  399  wrk -t12 -c100 -d30s http://192.168.18.214:3000
  400  wrk -t12 -c100 -d30s http://www.baidu.com
  401  wrk -t12 -c100 -d3s http://www.baidu.com
  402  wrk -t12 -c100 http://www.baidu.com
  403  wrk -t12 -c100 http://www.baidu.comclear
  404  wrk
  405  clear
  406  ls
  407  cd ..
  408  ls
  409  free -m
  410  clear
  411  df -h
  412  ip a
  413  cd /
  414  ls
  415  ssh root@192.168.18.214\
  416  ssh root@192.168.18.214
  417  cd /
  418  ls
  419  clear
  420  free -m
  421  ssh root@192.168.18.214
  422  ip a
  423  ssh root@192.168.18.217
  424  fo env
  425  go env
  426  ls
  427  vim main.go
  428  go run main.go 
  429  pwd
  430  export GOPATH=/
  431  go run main.go 
  432  vim foo.go
  433  go build -buildmode=plugin foo.go
  434  go run foo.go 
  435  cd /
  436  kls
  437  ls
  438  clear
  439  exit
  440  cd /
  441  virt-manager
  442  go
  443  ssh root@192.168.18.214
  444  apt install xrdp
  445  apt update
  446  ip a
  447  ifconfig
  448  cd /
  449  virt-manager
  450  apt install vnc4server
  451  apt install xubuntu-desktop
  452  echo xfce4-session >~/.xsession
  453  vim /etc/xrdp/startwm.sh 
  454  service xrdp restart
  455  add-apt-repository ppa:noobslab/macbuntu
  456  cd /home/softwareluke/下载
  457  dpkg -i code_1.13.1-1497464373_amd64.deb 
  458  dpkg -l
  459  dpkg -i code_1.13.1-1497464373_amd64.deb 
  460  pwd
  461  sudo add-apt-repository ppa:noobslab/icons
  462  apt update
  463  apt-get install ultra-flat-icons
  464  dpkg -i code_1.13.1-1497464373_amd64.deb 
  465  cd /etc/apt/
  466  sudo cp sources.list sources.list.bak
  467  ls
  468  vi sources.list
  469  apt update
  470  sudo add-apt-repository ppa:noobslab/macbuntu
  471  sudo apt-get install  macbuntu-os-ithemes-lts-v7
  472  sudo apt-get install  macbuntu-os-icons-lts-v7
  473  apt-get install  unity-tweak-tools
  474  unity-tweak-tools
  475  apt install unity-tweak-tools
  476  apt-get update
  477  apt install unity-tweak-tools
  478  ps -elf|grep apt
  479  kill -9 3316 
  480  ps -elf|grep apt
  481  apt install unity-tweak-tools
  482  apt install gedit vim
  483  apt autoremove
  484  apt install vim
  485  ip a
  486  df -h
  487  df -tH
  488  df -Th
  489  clear
  490  ls
  491  apt-get install macbuntu-os-icons-lts-v7
  492  apt-get install ubuntu-tweak
  493  java -version
  494  python -V
  495  pip -V
  496  go version
  497  npm -v
  498  node -v
  499  clear
  500  ls
  501  apt install openssh-server make gcc gdb g++
  502  wedded、
  503  lc
  504  wc
  505  dfedfsdfs
  506  clear
  507  netstat -ntlp
  508  apt-get install ubuntu-tweak
  509  apt install Unity Tweak Tool
  510  apt install unity-tweak-tool
  511  unity-tweak-tool
  512  apt-get install  macbuntu-os-ithemes-lts-v7 
  513  apt-get install  macbuntu-os-ithemes-lts
  514  apt-get install  macbuntu-os-ithemes
  515  unity-tweak-tool
  516  apt upgrade
  517  apt update
  518  clear
  519  docker info
  520  docker imagers
  521  docker images
  522  virt-manager
  523  clear
  524  unity-tweak-tool
  525  apt install Docky
  526  clear
  527  ls
  528  clea
  529  clear
  530  cd /
  531  ls
  532  cd mnt
  533  ls
  534  mkdir app
  535  ls
  536  mkdir devops
  537  ls
  538  mkdir web
  539  ls
  540  clear
  541  ls -ll
  542  mkdir log
  543  ls
  544  ls -ll
  545  fdisk -l
  546  add-apt-repository ppa:noobslab/macbuntu
  547  apt update
  548  apt-get install macbuntu-os-icons-lts-v7
  549  apt-get install albert
  550  apt-get install gnome-tweak-tool
  551  wget -O Ubuntu.po http://drive.noobslab.com/data/Mac/change-name-on-panel/ubuntu.po
  552  ld
  553  ls
  554  apt-get install plank
  555  whereis python
  556  which python
  557  whoami
  558  vim /etc/sudoers 
  559  usermod -g root softwareluke
  560  ls-ll
  561  ls -ll
  562  which java
  563  which golang
  564  which go
  565  which node
  566  clear
  567  go
  568  clear
  569  ls
  570  tar jvcf a.tar.bz2 app/*
  571  ls
  572  tar jvcf a.tar.bz2 /mnt/app/*
  573  clear
  574  ls
  575  sudo sh -c 'echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/dotnet/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list'
  576  sudo apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893
  577  apt-get update
  578  sudo apt-get install dotnet-dev-1.0.0-preview2-003121
  579  dotnet
  580  dotnet new
  581  ls
  582  dornet run
  583  clear
  584  dotnet --version
  585  pwd
  586  mkdir helloworld
  587  cd helloworld/
  588  dotnet new
  589  ls
  590  dotnet new
  591  cd /
  592  ls
  593  pip install tornado
  594  pip install flask
  595  pip install web.py
  596  clear
  597  ip a
  598  docker
  599  git
  600  clear
  601  cd ~
  602  cd .ssh
  603  ls
  604  cd ..
  605  ls
  606  ansible
  607  clear
  608  ls
  609  cleart
  610  clear
  611  apt-get install shutter rar
  612  nmtui
  613  nmcli con show
  614  clear
  615  nmcli dev show
  616  apt-get install zsh
  617  zsh
  618  cd ./
  619  cd /
  620  ;s
  621  ls
  622  clear
  623  ls
  624  apt install apache2
  625  which apache2
  626  cd /etc/apache2/
  627  ls
  628  clear
  629  ls
  630  netstat -ntl
  631  ls
  632  clear
  633  ls
  634  cd /opt
  635  ls
  636  ssh-keygen -t rsa
  637  cd ~
  638  cd .ssh
  639  ls
  640  cat id_rsa.pub 
  641  cd /
  642  ls
  643  cd home/
  644  ls
  645  cd softwareluke/
  646  ls
  647  cd /mnt
  648  ls
  649  mkdir pmscodes
  650  ls
  651  cd pmscodes/
  652  ls
  653  git clone -b develop git@gogs.jwops.cn:CW-NRD/cw-hms-source.git
  654  ls
  655  clear
  656  git clone -b base-dev git@gogs.jwops.cn:CW-NRD/jw-source.git
  657  ls
  658  git clone -b develop git@gogs.jwops.cn:CW-NRD/cw-hms-web.git
  659  git clone -b develop git@gogs.jwops.cn:CW-NRD/cw-pos-web.git
  660  ls
  661  clear
  662  ls
  663  pip install pyyaml 
  664  clear
  665  ls
  666  var http = require("http");  
  667  http.createServer(function(request, response) {  
  668  }).listen(8080);  
  669  console.log("Server running at http://localhost:8080/");  
  670  clear
  671  ls
  672  cd jw-source/
  673  git pull
  674  cd ..
  675  ls
  676  cd cw-hms-web/
  677  git pull
  678  clear
  679  ls
  680  cd ..
  681  ls
  682  git clone git@github.com:ibmcuijunluke/cw-datatest.git
  683  pwd
  684  cd ~
  685  cd .ssh
  686  ls
  687  cat id_rsa.pub 
  688  cd /mnt/pmscodes/
  689  ls
  690  clear
  691  git clone git@github.com:ibmcuijunluke/cw-datatest.git
  692  ls
  693  cd cw-datatest/
  694  ls
  695  ls -ll
  696  cd ..
  697  ls
  698  ls -ll
  699  pwd
  700  cd cw-datatest/
  701  pwd
  702  cd /home/softwareluke/桌面
  703  ls
  704  cd cw-datatest/
  705  ls
  706  cp -rf * /mnt/pmscodes/cw-datatest/
  707  ls
  708  cd /mnt/pmscodes/cw-datatest
  709  ls
  710  cd /
  711  cd mnt/
  712  ls
  713  cd pm
  714  cd pmscodes/
  715  ls
  716  cd cw-datatest/
  717  ls
  718  git add -A
  719  git commit -am "modify some changes"
  720  git push
  721  clear
  722  history

