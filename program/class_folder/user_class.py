import matplotlib.pyplot as plt
import numpy as np

#user relative class
class User():
    def __init__(self, food_tb, record_tb, user_tb, session):
        self.food_tb = food_tb
        self.record_tb = record_tb
        self.user_tb = user_tb
        self.session = session
    
    #craete a user
    def create_user(self):
        user_id = self.session.query(self.user_tb).count()+1
        if user_id ==1:
            print("Creating User File...")
            weight = int(input("Please enter your weight.\t"))
            print("Please pick your activity level from one of the options below:\t")
            print("A---Light\nB---Mediumn\nC---Heavy")
            act = str(input("A or B or C?\t")).upper()
            print("Please pick your purpose from one of the options below:\t")
            print("A---Gain Weight\nB---Keep Weight\nC---Loss Weight")
            purpose = str(input("A or B or C?\t")).upper()
            calories_dict = {'AA': 35, 'AB': 30, 'AC': 25,
                            'BA': 40, 'BB': 35, 'BC': 30,
                            'CA': 45, 'CB': 40, 'CC': 35}

            target_calories = calories_dict[act+purpose] * weight
            target_protein = target_calories * 0.3/4
            target_fat = target_calories * 0.2/9
            target_carbs = target_calories * 0.5/4

            user_input = self.user_tb(User_ID=1, Target_Calories = target_calories,
                                 Target_Protein = target_protein, Target_Carbs = target_carbs,
                                 Target_Fat = target_fat)
            self.session.add(user_input)
            self.session.commit()

    #return the intake nutrition for a user assigned date
    def start_visualize(self):
        search_date = input('Please enter the date you are looking at. mm/dd/yyyy.\t')
        records = self.session.query(self.food_tb).join(self.record_tb,self.food_tb.Food_ID == self.record_tb.Food_ID
                                               ).filter(self.record_tb.Time == search_date)
        intake_calories = 0
        intake_protein = 0
        intake_carbs = 0
        intake_fat = 0
        for intake in records:
            intake_calories += intake.Calories
            intake_protein += intake.Protein
            intake_carbs += intake.Carbs
            intake_fat += intake.Fat

        target = self.session.query(self.user_tb)
        for goal in target:
            target_calories = goal.Target_Calories
            target_protein = goal.Target_Protein
            target_carbs = goal.Target_Carbs
            target_fat = goal.Target_Fat


        plt.figure(figsize=(10,10))
        plt.title('Intaken Nutritions vs. Target Goals')
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5)
        ax1=plt.subplot(221)
        ax2=plt.subplot(222)
        ax3=plt.subplot(223)
        ax4=plt.subplot(224)

        axes = [ax1,ax2,ax3,ax4]
        intakes = [intake_calories,intake_protein,intake_carbs,intake_fat]
        targets = [target_calories,target_protein,target_carbs,target_fat]
        nutritions = ['Caloires','Protein','Carbs','Fat']


        print(f'You have intaken the nutrition belows:')
        for ax,intake,target,nutrition in zip(axes,intakes,targets,nutritions):
            print(f'{intake}g {nutrition} on {search_date}.')
            sizes = np.array([int(intake),int(target)])
            def absolute_value(val):
                a  = round(val/100*sizes.sum(), 0)
                return a
            ax.pie(sizes,
                   labels = [f'Intaken {nutrition}',f'Target {nutrition}'],
                    autopct = absolute_value,
                    pctdistance = 0.6,
                    textprops = {"fontsize" : 12})
        plt.show()