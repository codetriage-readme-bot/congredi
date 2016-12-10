#!/bin/bash
# Corrective regexes
find congredi/ -type f -exec sed -i "s/    /\t/g" {} \; -print
find congredi/ -type f -exec sed -i "s/,[^\s]/p" {} \; -print
