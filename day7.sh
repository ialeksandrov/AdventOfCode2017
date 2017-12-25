#!/bin/bash

for i in `cat day7.txt | cut -d' ' -f1`; do
    grep $i day7.txt | wc -l | sed "s/$/ $i/";
done | grep ^1
