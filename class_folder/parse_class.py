import os
import csv


#pasring variables
class Parse():
    # meal_translator =  {'B':'Breakfast','L':"Lunch",'D':'Dinner','O':"Others"}
    
    def __init__(self, web_url, driver): #, session, database_tables):
        self.web_url = web_url
        self.driver = driver
        # self.session = session
        # self.database_tables = database_tables
    
    #db_session for all the tables in the RMDB
    # def db_session(self):
    #     food_tb = self.database_tables.Food
    #     record_tb = self.database_tables.Record
    #     user_tb = self.database_tables.User
    #     return food_tb, record_tb, user_tb
    