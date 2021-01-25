import csv

#store nurtrition info to RMDB
class Food:
    def __init__(self, date, meal_time_transfered, target_brand, target_food,
                 calories, fat, carbs, fiber, protein, session):
        self.date = date
        self.meal_time_transfered = meal_time_transfered
        self.target_brand = target_brand 
        self.target_food = target_food
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.fiber = fiber
        self.protein = protein
        self.session = session
    
    #show the recording meal info
    def show_info(self): 
        meal_info = f'The meal {self.target_brand} {self.target_food} contains \n{self.calories} kcal calories,\n{self.fat} g fat,\n{self.carbs} g carbs,\n{self.fiber} g fiber,\n{self.protein} g protein'
        print(meal_info)
    
    #save the record to RMDB
    def save_result(self, food_tb, record_tb):
        #User
        user_id = 1
        
        #food
        food_id = self.session.query(food_tb).count()+1
        search_history = self.session.query(food_tb).filter(food_tb.Brand == self.target_brand
                                                          ).filter(food_tb.Meal == self.target_food)
        if search_history.count()>0:
            for history_data in search_history:
                food_id = history_data.Food_ID
                
        else:
            food_data = food_tb(Food_ID = food_id, Brand = self.target_brand,
                                            Meal= self.target_food,
                                            Calories = self.calories,Fat = self.fat,
                                            Carbs = self.carbs, Fiber = self.fiber, Protein = self.protein)
            self.session.add(food_data)
            self.session.commit()

        #record 
        record_id = self.session.query(record_tb).count()+1
        record_data = record_tb(Record_ID = record_id, Time = self.date, 
                                                Meal_Time = self.meal_time_transfered,
                                                Food_ID = food_id, User_ID = user_id)
        self.session.add(record_data)
        self.session.commit() 