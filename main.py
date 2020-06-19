 
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd 

if __name__ == '__main__':

    data = pd.read_csv('AB_NYC_2019.csv')

    data.to_csv('result.csv', columns=['id', 'host_id', 'price', 'number_of_reviews', 'last_review'], index=False)

