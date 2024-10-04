#!/bin/bash -ilex
python3 -V
echo $PATH
pip3 install -r requirements.txt
python3 -m pytest --alluredir report --clean-alluredir
