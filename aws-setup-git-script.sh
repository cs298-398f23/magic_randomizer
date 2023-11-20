#!/bin/bash
# installs git, clones the repo, and runs the real setup script
# This is so that I have to copy paste less when I'm testing

sudo yum install -y git
git clone https://github.com/cs298-398f23/magic_randomizer.git /home/ec2-user/magic_randomizer

chmod +x /home/ec2-user/magic_randomizer/start-script.sh
source /home/ec2-user/magic_randomizer/start-script.sh