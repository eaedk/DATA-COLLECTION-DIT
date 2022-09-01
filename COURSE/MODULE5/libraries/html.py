import json
from .utils import Utils
from bs4 import BeautifulSoup
import pandas as pd


BASE_URL = 'COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'


class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
        return data

    

    @classmethod
    def main(cls):
        souper = cls.openFile()

        table = souper.find(id='box-data').find('table')
        df =  pd.read_html(table.prettify( formatter="html" ))[0]
        df.columns = map(str.lower, df.columns)

        data = df.to_dict('records') 
        return data
