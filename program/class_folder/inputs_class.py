import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#get use inputs and parse for the nutrition info
class Inputs():
    def __init__(self,web_url, driver, session, database_tables):
        self.driver = driver
        self.web_url = web_url
        self.session = session
        self.database_tables = database_tables
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
    def get_key_word(self):
        self.driver.get(self.web_url)
        print('Recoridng your eating history...')
        time.sleep(3)
        search_terms = input('Please enter a brand.\t')
        print(f'search for the terms: \t{search_terms}')
        # search the key words
        search_field = self.driver.find_element_by_id('keywords')
        search_field.send_keys(search_terms)
        search_field.send_keys(Keys.RETURN)
        # get search terms results
        brands = self.driver.find_elements_by_class_name('jss5')
        result_lst = [ i.find_element_by_class_name('MuiTypography-root').text for i in brands]
        if 'iOS'in str(result_lst):
            print('Please try another search tearms for brand.')
            self.get_key_word()
        self.result_lst = result_lst
    
    #check the restarutnat name with user
    def get_brand(self):
        def check_brand(self):
            for i in self.result_lst:
                yield(i)
        brands = check_brand(self)
        correct = 'F'
        while correct == 'F':
            try:
                brand_candidate = next(brands)
                correct = input(f'If {brand_candidate} the brand you are looking for? T/F:\t').upper()
                if correct =='T':
                    target_brand = str(brand_candidate)
                    self.target_brand = target_brand
                    return target_brand
                elif correct !="F":
                    print('Please enter T or F. Try Again.')
                    self.get_brand()
            except: 
                print('Please try another search tearms for brand.')
                self.get_key_word()
                target_brand = self.get_brand()
                self.target_brand = target_brand
                return target_brand

    #get meal name    
    def get_key_word_checked(self):
        self.driver.get(self.web_url)
        time.sleep(3)
        meal_terms = input('Please enter the main meal ingrediant.\t').upper()
        search_terms = str(self.target_brand) + ' ' + meal_terms
        print(f'search for the terms: {search_terms}')
        # search the key words
        search_field = self.driver.find_element_by_id('keywords')
        search_field.send_keys(search_terms)
        search_field.send_keys(Keys.RETURN)
        # get search terms results
        foods = self.driver.find_elements_by_class_name('jss374')
        food_lst = [ i.text for i in foods]
        # check if contains wrong message
        if 'Food' in str(food_lst[0]):
            print('Please try another search tearms for meal.')
            self.get_key_word_checked()
        self.food_lst = food_lst
        self.meal_terms = meal_terms
        
    #check meal name with user
    def get_food(self):
        count = 0
        def check_food(self):
            for i in self.food_lst:
                yield(i)
        foods = check_food(self)
        correct = 'F'
        while correct == 'F':
            try:
                food_candidate = next(foods)
                correct = input(f'If {food_candidate} the meal you are looking for? T/F:\t').upper()
                
                if correct =='T':
                    target_food = str(food_candidate)
                    url = self.driver.find_elements_by_class_name('MuiListItem-button')[count].get_attribute('href')
                    target_food_url = (url)
                    self.target_food_url = target_food_url
                    self.target_food = target_food
                    return target_food_url, target_food
                elif correct =='F':
                    count=count+1
                    if count == 5:
                        print('Please try another search tearms for meal.')
                        self.get_key_word_checked()
                        self.get_food()
                        return self.target_food_url, self.target_food
                else:
                    print('Please enter T or F. Try again.')
                    self.get_food()
            except: 
                print('Please try another search tearms for meal.')
                self.get_key_word_checked()
                self.get_food()
                return self.target_food_url, self.target_food
    
    #parse the food nutrition info
    def get_food_info(self):
        self.driver.get(self.target_food_url)
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
    
    #get the meal time
    def get_time(self):
        date = input('Please enter the date. mm/dd/yyyy.\t')
        print('Please enter the meal time.')
        meal_time = input('B---Breakfast\nL---Lunch\nD---Dinner\nO---Others\t').upper()
        meal_translator = {'B':'Breakfast','L':"Lunch",'D':'Dinner','O':"Others"}
        if meal_time in ['B','L','D','O']:
            meal_time_transfered = meal_translator[meal_time]
        else:
            print('Please enter the meal time again.')
            self.get_time()
        self.date = date
        self.meal_time_transfered = meal_time_transfered
    
    #return the meal nutrition and time info
    def get_inputs(self):
        self.get_key_word()
        self.get_brand()
        self.get_key_word_checked()
        self.get_food()
        self.get_food_info()
        self.get_time()
        return self.date, self.meal_time_transfered, self.target_brand, self.target_food, self.calories, self.fat, self.carbs, self.fiber, self.protein
    