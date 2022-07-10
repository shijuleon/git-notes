#!/bin/env bash
# rm -rf .git notes.index notes
git init
cp hooks/{notelib.py,commit-msg,prepare-commit-msg} .git/hooks
chmod +x note .git/hooks/{commit-msg,prepare-commit-msg}
cp note ~/.local/bin
