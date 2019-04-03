#!/bin/sh
while :
do
  read -p "Hit enter: "
  ptex2pdf -l -u $1
done
