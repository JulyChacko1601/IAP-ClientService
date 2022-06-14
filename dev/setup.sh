#!/bin/bash
git clone -b 15.0 --depth 1 git@github.com:blooparksystems/enterprise.git ./addons_enterprise
git clone -b 15.0 --depth 1 git@github.com:blooparksystems/design-themes.git ./addons_themes
pip3 install --upgrade pip
pip3 install -r dev/requirements.txt
git submodule update --init
git update-index --assume-unchanged config/* dev/*
chmod +x ../dev.sh
chmod +x debug.sh
set -o allexport
source .env
set +o allexport
cd .git/hooks
rm -f commit-msg    
rm -f pre-push
sed -i'.original' -e "s/PROJECT_CODE/$PROJECT_CODE/" ../../dev/.git-hooks/commit-msg.py
chmod +x ../../dev/.git-hooks/commit-msg.py
ln -s ../../dev/.git-hooks/commit-msg.py ./commit-msg
sed -i'.original' -e "s/PROJECT_CODE/$PROJECT_CODE/" ../../dev/.git-hooks/pre-push.py
chmod +x ../../dev/.git-hooks/pre-push.py
ln -s ../../dev/.git-hooks/pre-push.py ./pre-push
