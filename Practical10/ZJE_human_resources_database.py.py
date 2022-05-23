class Staff: # to "combine" all the information including name, location. role
    fn= ""
    ln = ""
    lo= ""
    ro = ""
    def __init__(self,fn,ln,lo,ro):
        self.firstname = fn
        self.lastname = ln
        self.location=lo
        self.role=ro
    def attributes(self):
        print('First Name:%s. lastname:%s. Location:%s. Role:%s.'%(self.firstname, self.lastname,self.location,self.role))
p= Staff('Maizi','Fang','International Campus','Student')
p.attributes()
