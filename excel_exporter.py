import pandas as pd
from pandas import ExcelWriter
import os.path

def export(reviews):
    counter = 1
    fname = 'mining/reviews_1.xlsx'
    while os.path.isfile(fname):
        counter += 1
        fname = 'mining/reviews_' + counter + '.xlsx'

    df = pd.DataFrame(reviews)
    writer = ExcelWriter(fname)
    df.to_excel(writer, 'zomato',index=False)
    writer.save()