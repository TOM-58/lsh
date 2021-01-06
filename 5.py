
##5##


class Working_Experiences_optional:
    def __init__(self,Company,Industry,PositionWe,From,to,Level,MonthlySalary):
        self.Company = Company
        self.Industry = Industry
        self.PositionWe = PositionWe
        self.From = From
        self.to = to       
        self.Level = Level
        self.MonthlySalary = MonthlySalary

    def print_info(self):
        print('Company:')
        print('Industry:')
        print('Position:')
        print('From:')
        print('to:')
        print('Level')
        print('MonthlySalary')


def we():
        Company = input('Company:')
        Industry = input('Industry:')
        PositionWe = input('Position:')
        From = input('From:')
        to = input('to:')
        Level = input('Level:')
        MonthlySalary = input('MonthlySalary:')



def fifth_input():
    option = input("Do you want to fill in the working experience?(Y/N)")
    while True:
        if option.upper ==('Y'):
            we()
        elif option.upper == ('N'):
            break
        else:
            continue
                

print("Done")


def run():

    fifth_input()

if __name__ == "__main__":
    run()



       
 



        







print("Your application has been completed.")

