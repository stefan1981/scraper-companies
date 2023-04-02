#!/bin/bash

dl(){

i=0
while [ $i -ne 1067 ]
do
    url="https://www.value.today/?title=&field_company_category_primary_target_id&field_headquarters_of_company_target_id=All&field_company_website_uri=&field_market_value_jan072022_value=&page=$i"

    wget $url -O "dl/${i}.html"

    i=$(($i+1))
    echo $url
done

}

dl
