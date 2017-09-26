import re
import math
from datetime import *

class DataValidator():
    def validate(self, data):
        add_to = []
        feedback = ""
        for person in data:
            feedback += "Feedback for data at: " + str(data.index(person) + 1) + "\n"

            self.valid = True
            print(person)
            # check the format is a letter and 3 digit e.g A002 or a002
            if re.match(r'[a-z][0-9]{3}', (person[0]).lower()):
                # Kris
                if len(str(person[0])) >= 5:
                    self.valid = False
            else:
                # Kris
                feedback += "ID is incorrect; must contain a letter and 3 digits e.g. a001.\n"
                self.valid = False

            # check the format is either M/F/Male/Female

            if person[1].upper() == "M" or (person[1]).upper() == "F":
                print(person[1])
            else:
                # Kris
                feedback += "Incorect Gender; must be M or F.\n"
                self.valid = False

            # CHECK DATE, THEN CHECK AGE..
            # Kris
            date_correct = True
            try:
                datetime.strptime(person[6], "%d-%m-%Y")
            except ValueError:
                date_correct = False
                feedback += "Date is not corrent format! " + str(person[6])
                self.valid = False

            if date_correct:
                the_date = datetime.strptime(person[6], "%d-%m-%Y")
                test_age = math.floor(((datetime.today() - the_date).days/365))
                if test_age == int(person[2]):
                    pass
                else:
                    self.valid = False
                    feedback += "Age and birthday does not match. " + str(test_age) + ":" + str(int(person[2]))

            # check sales is 3 interger value
            if re.match(r'[0-9]{3}', person[3]):
                print(person[3])
            else:
                feedback += "Incorrect sales number; must be a 3 digit whole number. \n"
                self.valid = False

            # check BMI is either Normal / Overweight / Obesity or Underweight
            if re.match(r'\b(NORMAL|OVERWEIGHT|OBESITY|UNDERWEIGHT)\b', (person[4]).upper()):
                print(person[4])
            else:
                feedback += "Incorrect BMI value; Choose from Normal, Overweight, Obesity or Underweight. \n"
                self.valid = False

            # check Income is float
            try:
                if int(person[5]):
                    if len(str(int(person[5]))) > 3:
                        feedback += "Income is too large."
                        self.valid = False
                    else:
                        pass
                else:
                    feedback += "Incorrect income; must be an integer number. \n" + str(person[5])
                    self.valid = False
            except ValueError:
                self.valid = False

            if self.valid:
                add_to.append(person)
                feedback += "Passed and added to database.\n"
            else:
                feedback += '\n\n'

        print(feedback)
        return add_to