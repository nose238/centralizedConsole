# Creating directories;
cd /;
mkdir centralConsole
# Creating SSH key
ssh-keygen -b 2048 -t rsa -f /root/.ssh/id_rsa -q -N '' ; echo '' ;
# Terminal utilities 
yum install python -y;
yum install sshpass -y;
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm -f get-pip.py
mkdir keys;
mkdir /root/.ssh/temp;
# Python modules
pip install daemon-runner;
pip install lxml;
pip install selenium;

