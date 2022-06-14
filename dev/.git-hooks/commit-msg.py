#!/usr/bin/env python
# -*- coding: utf-8 -*-
# © 2021 bloopark systems (<http://bloopark.de>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import sys
import re


def main():
    with open(sys.argv[1], 'r') as fc:
        lines = fc.readlines()
        for seq, line in enumerate(lines):
            if line[0] == '#':
                continue
            if not line_valid(seq, line):
                commit_rules()
                sys.exit(1)
    sys.exit(0)


def line_valid(seq, line):
    if seq == 0:
        return re.match(
            "^PROJECT_CODE-[0-9]*\s+\[((FIX)|(REF)|(REM)|(REL)|(MERGE)|(ADD)|(IMP)"
            "|(I18N)|(PEP8))\]\s[\w&.\-!@,#$%^&*()]*:\s[\w\s&.\-!@#$%^&*()]*",
            line
        )
    elif seq == 1:
        return len(line.strip()) == 0
    else:
        return len(line.strip()) <= 72


def commit_rules():
    print("""
Rules for the commit messages
* Subject must start with the ticket number ex: PROJECT_CODE-123
* Followed by the commit type 
    - [ADD]: for adding new modules;
    - [FIX]: for bug fixes;
    - [IMP]: for improvements;
    - [REF]: for refactoring;
    - [REM]: for removing resources;
    - [REL]: for release commits;
    - [MERGE]: for merge commits;
    - [I18N]: for changes in translation files;
    - [PEP8]: for changes due to code style guidelines;
* Followed by the module name and ':'
* Followed with the subject of the commit 
* Separate subject from the body with a blank line
* Capitalize the subject line
* Wrap the body at 72 characters
* Use the body to explain what and why vs. how
 EXAMPLE: 

 PROJECT_CODE-123 [ADD] Module_name: Subject of the commit

 Body of the commit explaining the changes    
""")


if __name__ == '__main__':
    main()
