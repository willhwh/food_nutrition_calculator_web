#for parsing food info
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#for connecting to RMDB
##user_name and passwrod
from config import username, password, host

from flask import Flask
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

#create varaibles for future usage
def static():
    web_url = 'https://www.calorieking.com/us/en/foods/'
    
    #chrome setting
    def start_program():
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        return driver
    
    #chrome driver
    driver = start_program()
    

    #connect to RMDB
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Prevent caching
    engine = create_engine(f"postgresql://{username}:{password}{host}")
    base = automap_base()
    base.prepare(engine, reflect=True)
    database_tables = base.classes
    
    #for editing RMDB
    session = Session(bind=engine)
    
    return web_url, driver, session, database_tables

#back to main menu
def back_to_menu():
    print('Back to Main Menu.')
    pass

#get user command
def get_command():
    '''
    Get command, upper-case it
    '''
    print("'A' => Add to Record")
    print("'U  => View Target Intake")
    print("'V' => View Daily Intake")
    print("'Q' => Quit")
    command = input("Enter command: ").upper()
    return command