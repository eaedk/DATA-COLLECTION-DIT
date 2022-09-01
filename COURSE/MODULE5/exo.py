from COURSE.MODULE5.libraries.utils import Utils
from COURSE.MODULE5.libraries.csv import CsvFactory
from COURSE.MODULE5.libraries.json import JsonFactory
from COURSE.MODULE5.libraries.html import HtmlFactory
import pandas as pd
import numpy as np
import requests, bs4, re
from pymongo import MongoClient

def concat_data(list_of_data=[]):
    """concat data from providers _Factory"""
    concat = []

    for d in list_of_data:
        concat.extend(d)

    return concat

def httpFetcher(URL: str,
                params=None,
                headers=None):
    result = requests.get(URL,
                          params=params,
                          headers=headers)
    return result

def get_database():
    
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
    CONNECTION_STRING = "mongodb://koupoh:EokHCuHGjKRJCByl@cluster0-shard-00-00.vlhcs.mongodb.net:27017,cluster0-shard-00-01.vlhcs.mongodb.net:27017,cluster0-shard-00-02.vlhcs.mongodb.net:27017/?ssl=true&replicaSet=atlas-4vjb7f-shard-0&authSource=admin&retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['data_collection']

def add_random_currencies(data:list):

    URL = "https://www.bceao.int/fr/cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts"
    result = httpFetcher(URL).text
    souper = bs4.BeautifulSoup(result,'html.parser')

    #table of devise
    table = souper.select_one("#box_cours > table") 
    # change comma to have correct float
    findcomma = table.find_all(text = re.compile(','))
    for comment in findcomma:
        fixed_text = comment.replace(',', '.')
        comment.replace_with(fixed_text)
    
    df =  pd.read_html(table.prettify( formatter="html" ))[0]
    df.columns = map(str.lower, df.columns)

    currency_indexes = np.random.randint(df.shape[0], size=len(data))

    df_data = pd.DataFrame(data)
    df_data['currency'] = [ df.loc[i,"devise"] for i in currency_indexes] # add random devise
    df_data['conv_to_xof'] = [ df.loc[i,"vente"] for i in currency_indexes]
    
    return df_data.fillna('').to_dict('records')

def add_random_countries(data:list):

    URL = "https://restcountries.com/v3.1/region/africa"
    result = httpFetcher(URL).json()
    
    country_indexes = np.random.randint(len(result), size=len(data))
    
    df_data = pd.DataFrame(data)
    df_data['country'] = [ result[i]["name"]['common'] for i in country_indexes] # add random country
    df_data['flag'] = [ result[i]['flags']['png'] for i in country_indexes]

    return df_data.fillna('').to_dict('records')


if __name__ == '__main__':
    """"""
    print("PROCESSING STARTED")
    # concat data from the 3 sources
    all_data = concat_data(list_of_data=[JsonFactory.main(),HtmlFactory.main(),CsvFactory.main() ])
    print(pd.DataFrame(all_data).head(3))
    print("PROCESSING IN PROGRESS...")

    # BCEAO
    all_data_with_currencies = add_random_currencies(data=all_data)
    print(pd.DataFrame(all_data_with_currencies).head(3))
    print("PROCESSING IN PROGRESS...")

    # Country
    all_data_with_countries = add_random_countries(data=all_data_with_currencies)
    print(pd.DataFrame(all_data_with_countries).head(3))
    print("PROCESSING IN PROGRESS...")

    # MongoDB
    # Get the database
    dbname = get_database()
    # get collection and insert all
    collection_name = dbname["contacts_items"]
    print(Utils.divider())
    collection_name.delete_many({}) # clean the collection before adding contact
    print(f"Number of element in the collection BEFORE insertion: {collection_name.count_documents({})}")
    result = collection_name.insert_many(all_data_with_countries)
    print(Utils.divider())
    print(f"Number of element in the collection AFTER insertion: {collection_name.count_documents({})}")
    # result.inserted_ids # => [ObjectId('54f113fffba522406c9cc20e'), ObjectId('54f113fffba522406c9cc20f'), ...]
    print("PROCESSING DONE!!!")
