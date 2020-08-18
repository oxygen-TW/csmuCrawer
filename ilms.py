from commonTools import LoginILms

class ILms(LoginILms):
    def __init__(self, user, password):
        self.username = user
        self.password = password
        self.session = ""

    def CheckAccount(self):
        if(not(super().login(self.user, self.password))):
            return False
        else:
            return True

    def GetSession(self):
        res = super().login(self.user, self.password)

        if(not(res)):
            return False
        else:
            self.session = res["PHPSESSID"]
            return res["PHPSESSID"]

if __name__ == "__main__":
    l = ILms()
