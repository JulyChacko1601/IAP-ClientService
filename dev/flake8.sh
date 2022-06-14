#!/bin/bash
flake8 . --exclude=addons_repos_ext,addons_ext,addons_enterprise,addons_themes,commit-msg.py,__init__.py,*.sh,dev --max-line-length=80 --statistics
