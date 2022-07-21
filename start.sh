#!/bin/bash
/train.py

if [ -s details.txt ]; then
  echo "not empty"
else
  echo "empty"
fi

export var=$(cat details.txt)
