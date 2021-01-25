import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#get use inputs and parse for the nutrition info
class Inputs():
    def __init__(self,web_url, driver): #, session, database_tables):
        self.driver = driver
        self.web_url = web_url
        # self.session = session
        # self.database_tables = database_tables
        self.result_lst = []
        self.target_brand = None
        self.food_lst = []
        self.meal_terms = None
        self.target_food_url = None
        self.target_food = None
        self.calories = 0
        self.fat = 0
        self.carbs = 0
        self.fiber = 0 
        self.protein = 0
        self.date = None
        self.meal_time_transfered = None
    
    #get the restaurant name
    def get_key_word(self,user_input_restaurant_name):
        self.driver.get(self.web_url)
        print('Recoridng your eating history...')
        time.sleep(5)
        search_terms = user_input_restaurant_name
        print(f'search for the terms: \t{search_terms}')
        # search the key words
        search_field = self.driver.find_element_by_id('keywords')
        search_field.send_keys(search_terms)
        search_field.send_keys(Keys.RETURN)
        # get search terms results
        brands = self.driver.find_elements_by_class_name('jss5')
        result_lst = [ i.find_element_by_class_name('MuiTypography-root').text for i in brands]
        self.target_brand = result_lst[0]
    
    def get_restaurant_name(self,user_input_restaurant_name):
        self.get_key_word(user_input_restaurant_name)
        return self.target_brand
    
    def get_key_word_checked(self,user_input_meal_name):
        self.driver.get(self.web_url)
        time.sleep(5)
        meal_terms = user_input_meal_name
        search_terms = str(self.target_brand) + ' ' + meal_terms
        print(f'search for the terms: {search_terms}')
        # search the key words
        search_field = self.driver.find_element_by_id('keywords')
        search_field.send_keys(search_terms)
        search_field.send_keys(Keys.RETURN)
        # get search terms results
        foods = self.driver.find_elements_by_class_name('jss374')
        food_lst = [ i.text for i in foods]
        self.food_lst = food_lst
        self.meal_terms = meal_terms
        
  

    def get_meal_name(self,user_input_meal_name):
        self.get_key_word_checked(user_input_meal_name)
        foods = self.food_lst
        return foods

    def get_meal_info(self, user_input_restaurant_name, user_input_meal_name):
        search_terms = user_input_restaurant_name + ' ' + user_input_meal_name
        print(f'search for the terms: {search_terms}')
        search_field = self.driver.find_element_by_id('keywords')
        search_field.send_keys(search_terms)
        search_field.send_keys(Keys.RETURN)
        url = self.driver.find_elements_by_class_name('MuiListItem-button')[0].get_attribute('href')
        self.driver.get(url)
        infos = self.driver.find_element_by_class_name('jss374')
        infos = infos.text.split('\n')
        
        calories = infos[0].split(' ')[0]
        fat = infos[6].split(' ')[0]
        carbs = infos[8].split(' ')[0]
        fiber = infos[10].split(' ')[0]
        protein = infos[12].split(' ')[0]
        
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.fiber = fiber
        self.protein = protein

        return self.calories, self.fat, self.carbs, self.protein
    

    # #return the meal nutrition and time info
    # def get_inputs(self):
    #     self.get_key_word()
    #     self.get_brand()
    #     self.get_key_word_checked()
    #     self.get_food()
    #     self.get_food_info()
    #     self.get_time()
    #     return self.target_brand, self.target_food, self.calories, self.fat, self.carbs, self.fiber, self.protein
    
    #     #return self.date, self.meal_time_transfered, self.target_brand, self.target_food, self.calories, self.fat, self.carbs, self.fiber, self.protein
    