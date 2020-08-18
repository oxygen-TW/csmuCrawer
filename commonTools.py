import requests
from requests.exceptions import Timeout
from CSMUCException import *
import logging
import json

class LoginILms():
    def __init__(self):
        pass

    def login(self, user, password):
        LoginUrl = "http://lms.csmu.edu.tw/sys/lib/ajax/login_submit.php?account={username}&password={password}&ssl=1"
        LoginUrl = LoginUrl.format(username=user, password=password)
        r = ""

        try:
            r = requests.get(LoginUrl, timeout=3)
        except Exception as identifier:
            logging.critical(str(identifier))

        #確認 HTTP Code
        if(r.status_code != 200):
            raise HTTPCodeError

        #確認是否登入成功 
        response = json.loads(r.text.replace("(","").replace(")",""))
        status = response["ret"]["status"]
        
        if(status == "false"):
            return False

        #若成功則回傳 Cookies
        logging.debug(r.cookies.get_dict())
        return r.cookies.get_dict()

if __name__ == "__main__":
    l = LoginILms()
    print(l.login("0770012", "csmu234830"))