#!/bin/bash

egrep -hro '"/company/.{1,}" ' | uniq | sort | tr -d '"' | sed -e 's/^/https:\/\/www.value.today/'
