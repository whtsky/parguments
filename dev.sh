#!/bin/bash

echo 'Installing git hooks..'
mkdir .git/hooks > /dev/null
cp githooks/* .git/hooks > /dev/null
chmod +x .git/hooks > /dev/null
echo 'Done.'

echo 'Creating virtualenv..'
virtualenv .
source bin/activate

echo 'Install requirements..'
pip install -r dev-requirements.txt

python setup.py develop