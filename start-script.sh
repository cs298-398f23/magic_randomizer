# Doesn't work rn, running mongosh gives error
# echo "[mongodb-org-7.0]
# name=MongoDB Repository
# baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/7.0/x86_64/
# gpgcheck=1
# enabled=1
# gpgkey=https://www.mongodb.org/static/pgp/server-7.0.asc
# " > /etc/yum.repos.d/mongodb-org-7.0.repo
#
# sudo yum install -y mongodb-org

# Other idea for mongo, doesn't work rn because can't find package, maybe use that repo page?
# dnf install -qy mongodb-mongosh-shared-openssl3

# python3 -m venv .venv
# source .venv/bin/activate
# pip3 install -r requirements.txt 