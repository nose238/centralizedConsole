# Creating user
useradd adminConsole;
echo "W@rri0rs" | passwd --stdin adminConsole;
usermod -a -G root adminConsole;
# Creating directories
cd /;
mkdir centralConsole;
# Terminal utilities 
yum install python -y;
yum install sshpass -y;
yum install net-tools -y;
curl -O https://bootstrap.pypa.io/get-pip.py;
python get-pip.py;
rm -f get-pip.py;
mkdir keys;
mkdir /root/.ssh/temp;
mkdir /var/www/html/centralizedConsole/web/clients;
# Python modules
pip install daemon-runner;
pip install lxml;
pip install selenium;
# Permises
chmod 774 -R /var/www/html/centralizedConsole;
chmod 774 -R /centralConsole;
chmod 777 -R /var/www/html/centralizedConsole/web/clients; # This is not the best option
# Changnig user
su adminConsole;
# Creating SSH key
ssh-keygen -b 2048 -t rsa -f /home/adminConsole/.ssh/id_rsa -q -N '' ;
mkdir /home/adminConsole/.ssh/temp/
echo "COMPLETED";