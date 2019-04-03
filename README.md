# pythonWebsitePixelTracking

### server
CentOS 7

### ip address log
Database import functionality has not been added, the IP address is written into `/home/vestaCentral/mnt/pythonWebsite/pt.out`


### DNS 
Unfortunately, the DNS nameservers still forwarding the domain, we may only can use ip address as domain currently.

### uwsgi
server run log is `uwsgi.log`
uwsgi setting file is `uwsgi.ini`

start uwsgi `uwsgi --ini uwsgi.ini` this command would use 8000 port

### nginx 
setting file `pt_nginx.conf` which is link to `/etc/nginx/conf.d`
start nginx `service nginx start` it listen 443 port

### system environment
Django==2.1.7
pbr==5.1.3
pytz==2018.9
six==1.12.0
stevedore==1.30.1
uWSGI==2.0.18
virtualenv==16.4.3
virtualenv-clone==0.5.1
virtualenvwrapper==4.8.4



