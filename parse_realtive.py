#for parsing food info
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#create varaibles for future usage
def static():
    web_url = 'https://www.calorieking.com/us/en/foods/'
    
    #chrome setting
    def start_program():
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome()
        return driver
    
    #chrome driver
    driver = start_program()
    

    # #connect to RMDB
    # app = Flask(__name__)
    # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Prevent caching
    # engine = create_engine(f"postgresql://{username}:{password}{host}")
    # base = automap_base()
    # base.prepare(engine, reflect=True)
    # database_tables = base.classes

    return web_url, driver #, session, database_tables