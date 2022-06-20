#!/usr/bin/env python
# -*- coding: utf-8 -*-
# © 2021 bloopark systems (<http://bloopark.de>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import sys
import re


def main():
    for line in sys.stdin:
        local_ref, local_sha1, remote_ref, remote_sha1 = line.strip().split()
        branch_name = local_ref.replace('refs/heads/', '')
        if not line_branch(branch_name):
            print(
                "Branch ", branch_name,
                "Not follow the naming standard of the project"
            )
            branch_rules()
            sys.exit(1)
    sys.exit(0)


def line_branch(name):
    return re.match(
        "((feature)|(fix)|(hotfix)|(improve))[/](IAPC)-[0-9]*_[\w]*", name
    )


def branch_rules():
    print("""
Rules for Branch naming
* branch name should start with
** feature/
** hotfix/
** fix/
** improve/
* followed by ticket name 
** IAPC-123
* followed by _ and branch name
 EX: feature/IAPC-123_new_branch
""")


if __name__ == '__main__':
    main()
