#LeeSagnHyup-927UMF0L
import datetime
 ##1##


class job_application_form:
    def __init__(self,position,applied,salary,Availability):
        self.position = position
        self.applied = applied
        self.salary = salary
        self.Availability = Availability
    
    def print_info(self):
         print("position:"+self.position)
         print("applied:"+self.applied)
         print("expected salary:"+self.salary+"SGD")
         print("Availability:"+self.Availability+"month")


def first_input():
    position = input('Positiion Applied:')
    applied = date_entry =input('Date Applied ex)20210101:')
    salary = input('Expected Salary:')
    Availability = input('Availability(month):')
    print(position, applied, salary, Availability)

def run():
    first_input()

if __name__ == "__main__":
    run()