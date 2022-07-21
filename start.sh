#!/bin/bash
/train.py

if [ -s details.txt ]; then
  echo "not empty"
  export var=$(cat d.txt)
else
  echo "empty"
fi


