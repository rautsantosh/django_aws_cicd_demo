#!/usr/bin/bash 

sed -i 's/\[]/\["54.144.250.113"]/' /home/ubuntu/django_aws_cicd_demo/notspam/settings.py

python manage.py migrate 
python manage.py makemigrations     
sudo python manage.py collectstatic
sudo chown ubuntu:ubuntu /home/ubuntu/django_aws_cicd_demo
sudo chown ubuntu:ubuntu /home/ubuntu/django_aws_cicd_demo/public
sudo service gunicorn restart
sudo service nginx restart
#sudo tail -f /var/log/nginx/error.log
#sudo systemctl reload nginx
#sudo tail -f /var/log/nginx/error.log
#sudo nginx -t
#sudo systemctl restart gunicorn
#sudo systemctl status gunicorn
#sudo systemctl status nginx
# Check the status
#systemctl status gunicorn
# Restart:
#systemctl restart gunicorn
#sudo systemctl status nginx
