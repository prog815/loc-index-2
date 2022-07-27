#/bin/sh

date

find ./static/files/ -type f | awk '{print substr($0,16)}' | python update.py

echo OK

