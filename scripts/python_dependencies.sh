#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip3 install -r /home/ubuntu/django_aws_cicd_demo/requirements.txt