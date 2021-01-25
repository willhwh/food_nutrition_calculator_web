from function_folder.functions_file import static, back_to_menu
from class_folder.parse_class import Parse
from class_folder.user_class import User
from class_folder.inputs_class import Inputs
from class_folder.food_class import Food


#main menu lists
class main_function():
    def __init__(self):
        self.web_url = None
        self.driver = None
        self.user_info = None
        self.food_tb = None
        self.record_tb = None
        self.user_tb = None
        self.session = None
        self.database_tables = None
    
    #static for start record and star visulize function
    def __start__(self):
        web_url, driver, session, database_tables = static()
        parse_tool = Parse(web_url, driver, session, database_tables)
        food_tb, record_tb, user_tb = parse_tool.db_session()
        user_info = User(food_tb, record_tb, user_tb, session)
        user_info.create_user()
        self.web_url = web_url
        self.driver = driver
        self.user_info = user_info
        self.food_tb = food_tb
        self.record_tb = record_tb
        self.user_tb = user_tb
        self.session = session
        self.database_tables = database_tables
    
    #show user's target intake
    def user_information(self):
        user_info = self.session.query(self.user_tb)
        for user in user_info:
            target_calories = user.Target_Calories
            target_protein = user.Target_Protein
            target_carbs = user.Target_Carbs
            target_fat = user.Target_Fat
        print(f'Your daily target intake nutritions are below:\nTarget Calories:\t{target_calories}\nTarget Protein:\t{target_protein}\nTarget Carbs:\t{target_carbs}\nTarget Fat:\t{target_fat}')

    #start the recording function
    def start_record(self):
        user_input = Inputs(self.web_url, self.driver, self.session, self.database_tables)
        date, meal_time_transfered, target_brand, target_food, calories, fat, carbs, fiber, protein = user_input.get_inputs()
        food_nutrition = Food(date, meal_time_transfered, target_brand, target_food, calories, fat, carbs, fiber, protein, self.session)
        food_nutrition.show_info()
        food_nutrition.save_result(self.food_tb,self.record_tb)
        back_to_menu()
 
    #start the visualizing functino   
    def start_visualize(self):
        self.user_info.start_visualize()
        back_to_menu()