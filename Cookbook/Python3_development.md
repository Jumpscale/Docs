## Ubuntu 15.10 Python3 in development

manual prepare your machine for development purposes on ubuntu 15.10
best to copy following script in /tmp/install.sh & execute

'''
#!/bin/bash
set -ex

cd /tmp
rm -rf get-pip.py
wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate

apt-get install libpython3.5-dev python3.5-dev libffi-dev gcc build-essential autoconf libtool pkg-config libpq-dev -y
apt-get install libsqlite3-dev -y
apt-get install net-tools sudo -y

rm -f /usr/bin/python
rm -f /usr/bin/python3
ln -s /usr/bin/python3.5 /usr/bin/python
ln -s /usr/bin/python3.5 /usr/bin/python3

python get-pip.py

pip install 'cython>=0.23.4' git+git://github.com/gevent/gevent.git#egg=gevent

pip install msgpack-python
pip install redis
pip install bcrypt
pip install blosc
pip install bson
pip install certifi
pip install docker-py

pip install gitlab3
pip install gitpython
pip install html2text

#is this std now??? in python3.x
#pip install multiprocessing
##NOT WORKING TO BE CHECKED
#pip install email
# pip install pysqlite


pip install influxdb
pip install ipdb
pip install ipython --upgrade
pip install jinja2
pip install netaddr

#pip install numpy

pip install reparted
pip install pytoml
pip install pystache
pip install pymongo
pip install psycopg2
pip install pathtools
pip install psutil

pip install pytz
pip install requests
pip install sqlalchemy
pip install urllib3 
pip install zmq
pip install pyyaml
pip install websocket
pip install marisa-trie
pip install pylzma
pip install ujson

export SANDBOX=0
export JSBRANCH='python3_unstable'
export AYSBRANCH='python3_unstable'
cd /tmp;rm -f install.sh;curl -k https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/python3_unstable/install/install3.sh > install.sh;bash install.sh

'''
