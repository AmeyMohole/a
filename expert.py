from random import choice


class ExpertSystem:
    def __init__(self, symptoms, diseases):
        self.symptoms = symptoms
        self.diseases = diseases
        self.current_symptom = None
        self.current_disease = None
    
    def start(self):
        self.current_symptom = choice(self.symptoms)
        severity = int(input(f"On a scale of 0 to 10, how severe is your {self.current_symptom}? "))
        self.current_disease = self.diseases.get(self.current_symptom)
        if severity > 5:
            print(f"You may have {self.current_disease}")
        else:
            print(f"You probably don't have {self.current_disease}")
            
        self.askNextQuestion()
    
    def askNextQuestion(self):
        if self.current_disease is not None:
            answer = input("Do you have any other symptoms (yes/no)? ")
            if answer.lower() == "yes":
                self.start()
            else:
                print("Thank you for using our Expert System!")
        else:
            print("Sorry, I can't help you with disease diagnosis.")

if __name__ == '__main__':
    symptoms = ["fever", "cough", "sore throat", "runny nose", "headache"]
    diseases = {
        "fever": "flu",
        "cough": "cold",
        "sore throat": "strep throat",
        "runny nose": "allergies",
        "headache": "migraine"
    }
            
    es = ExpertSystem(symptoms, diseases)
    es.start()
