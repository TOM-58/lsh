##4##



class ref:
    def __init__(self,NameRef,Occupation,CompanyOrganization,ContactNo,Email,Relationship):
        self.NameRef = NameRef
        self.Occupation = Occupation
        self.CompanyOrganization = CompanyOrganization
        self.ContactNo = ContactNo
        self.Email = Email
        self.Relationship = Relationship
    
    def print_info(self):
        print("NameRef:",self.NameRef)
        print("Occupation:",self.Occupation)
        print("CompanyOrganization:",self.CompanyOrganization)
        print("ContactNo:",self.ContactNo)
        print("Email:",self.Email)
        print("Relationship:",self.Relationship)


def fourth_input():
    while True:
        NameRef = input("NameRef:")
        Occupation = input("Occupation:")
        CompanyOrganization = input("CompanyOrganization:")
        ContactNo = input("ContactNo:")
        Email = input("Email:")
        Relationship = input("Relationship:")
        ref2 = input("Do you want to write down the second ref?(Y/N)")
        if ref2 == ('Y','y'):
            continue
        elif ref2 == ('N','n'):
            break
        else:
            pass
            

    


def run():

    fourth_input()

if __name__ == "__main__":
    run()


























