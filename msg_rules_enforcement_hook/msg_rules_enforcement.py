#!/usr/bin/env python3

import argparse
import sys
import re

def get_match(message):
    matches = re.findall('(merge|(((feat|fix): ([\w\-]+)|docs|test): ))', message)
    if len(matches) > 0:
        return matches[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("commit_msg_filepath")
    args = parser.parse_args()
    commit_msg_filepath = args.commit_msg_filepath

    with open(commit_msg_filepath, "r+") as f:
        content = f.read()
        if not get_match(content):
            exit("Commit message should contain type (feat,fix) and task reference. Examples: 'feat: 123123: my commit message'; 'fix: ABC-2323: some fix here'")

if __name__ == "__main__":
    exit(main())
