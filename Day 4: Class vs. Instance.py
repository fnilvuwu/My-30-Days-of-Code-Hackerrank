class Person:
    initialAge = 0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if (initialAge > 0):
            self.initialAge = initialAge
        else:
            print("Age is not valid, setting age to 0.")
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if (self.initialAge >= 13 and self.initialAge < 18) :
            print("You are a teenager.")
        elif (self.initialAge < 13):
            print("You are young.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge += 1

        
