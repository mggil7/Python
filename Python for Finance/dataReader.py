import pandas_datareader.data as web

import datetime

start = datetime.datetime(2015, 1, 1)

end = datetime.datetime(2017, 1, 1)

df = web.get_data_yahoo('GE','yahoo',start, end)

print('rodando')