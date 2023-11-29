#!/bin/bash
# installs git, clones the repo, and runs the real setup script
# This is so that I have to copy paste less when I'm testing

sudo yum install -y git
git clone https://github.com/cs298-398f23/magic_randomizer.git /home/ec2-user/magic_randomizer

# changes the owner of the repo to ec2-user so sudo doesn't have to be used
sudo chown ec2-user:ec2-user /home/ec2-user/magic_randomizer -R

# install and start docker
sudo yum install docker -y
sudo service docker start

# install docker-compose and give ec2-user permission to run it, it's separate from docker for some reason
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

cd /home/ec2-user/magic_randomizer
sudo docker-compose up -d --build