#!/bin/bash
pylint addons_bp/* ./**/*.py *.py --rcfile ./dev/pylint.cfg --load-plugins pylint_odoo --fail-under 10 --ignore-patterns=commit-msg.py,dev.sh,addons_repos_ext,addons_ext,addons_enterprise,addons_themes,dev
