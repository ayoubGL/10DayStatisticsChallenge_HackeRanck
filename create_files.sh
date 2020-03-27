#!/bin/bash
Files="$@"
for f in $Files
do
	touch ./$f.py
done
