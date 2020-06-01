import requests
import json
from time import *
from collections import defaultdict
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://user:pass@db',echo=True)
class postman():
    def __init__(self):
        self.url=''
        self.payload={}
        self.headers={}
        self.response=None
        self.category=[]
        self.retrieved_category=[]
        self.page_no=1
        self.all_api=[]
        self.ind=0
    def get_auth(self):
        self.url="https://public-apis-api.herokuapp.com/api/v1/auth/token"
        self.response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
        self.headers['Authorization']='Bearer '+(json.loads(self.response.text.encode('utf8'))['token'])
    def get_all_categories(self):
        self.get_auth()
        while(True):
            self.url = "https://public-apis-api.herokuapp.com/api/v1/apis/categories?page="+str(self.page_no)
            self.response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
            self.retrieved_category=json.loads(self.response.text.encode('utf8'))['categories']
            
            if len(self.retrieved_category)==0:
                break
            self.category.extend(self.retrieved_category)
            self.page_no+=1
        print('Categories Retrieved:',len(self.category))
        print(self.category)
    def get_each_category(self):
        for page in range(self.ind,len(self.category)):
            category=self.category[page]
            print(category)
            self.page_no=1
            while(True):
                error=''
                try:
                    self.url = "https://public-apis-api.herokuapp.com/api/v1/apis/entry?page="+str(self.page_no)+"&category="+category
                    self.response=requests.request("GET",self.url, headers=self.headers, data = self.payload)
                    error=self.response.content
                    self.retrieved_apis=json.loads(self.response.text.encode('utf8'))
                    self.retrieved_apis=self.retrieved_apis['categories']
                    self.all_api.extend(self.retrieved_apis)
                    self.page_no+=1
                    if len(self.retrieved_apis)==0:
                        self.ind+=1
                        break
                except Exception as e:
                    if "error" in error.decode("utf-8"):
                        print('*'*50+'Token Expired'+'*'*50)
                        sleep(35)
                        self.get_auth()
                        print('*'*49+'Token Activated'+'*'*49)
                    else:
                        print('*'*50+'Slept'+'*'*50)
                        sleep(35)
                        print('*'*50+'Waked'+'*'*50)
        pd.DataFrame(self.all_api).to_sql('sudhan_postmanapi',
                                          con=engine,
                                          index=False
                                          )
crawler=postman()
crawler.get_all_categories()
crawler.get_each_category()
print(pd.DataFrame(engine.execute("select * from sudhan_postmanapi").fetchall(),
                   columns=['API','Description','Auth','HTTPS','Cors','Link','Category']).to_string())

