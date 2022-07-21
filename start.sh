#!/bin/bash
/train.py

if [ -f /details.txt ]; then
  echo "not empty"
  export var=$(cat d.txt)
else
  echo "empty"
fi


