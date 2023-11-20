#!/bin/bash
# installs git, clones the repo, and runs the real setup script
# This is so that I have to copy paste less when I'm testing

sudo yum install -y git
git clone https://github.com/cs298-398f23/magic_randomizer.git
cd magic_randomizer

chmod +x ./magic_randomizer/start-script.sh
source magic_randomizer/start-script.sh