#!/bin/bash

for url in $(cat company-links.txt)
do
  echo $url
  company_name=$(echo $url | cut -d'/' -f5)
  echo $company_name

  wget $url -O "company/${company_name}.html"

done
