# -*- coding: utf-8 -*-
import uuid
import secrets
import string
import clipboard
from wox import Wox

class PasswdGenClass(Wox):

    def query(self,query):
        plen = 20
        if query=="uuid":
            password=str(uuid.uuid4()).upper()
        else:
            if 's' in query:
                query = query.replace('s', '')
                alphabet = string.ascii_letters + string.digits + string.punctuation
            else:
                alphabet = string.ascii_letters + string.digits
            if not query:
                plen = 20
            else:
                plen = int(query)
            password = ''.join(secrets.choice(alphabet) for i in range(plen))
        results = [{
            "Title": password,
            "SubTitle": "Click to copy to clipboard.",
            "IcoPath":"Images/walle.png",
            "JsonRPCAction":{
            #You can invoke both your python functions and Wox public APIs .
            #If you want to invoke Wox public API, you should invoke as following format: Wox.xxxx
            #you can get the public name from https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs,
            #just replace xxx with the name provided in this url
            "method": "copyToClipboard",
            #you MUST pass parater as array
            "parameters":[password],
            #hide the query wox or not
            "dontHideAfterAction":True
            }
        }]
        return results

    def copyToClipboard(self,password):
        clipboard.copy(password)

if __name__ == "__main__":
    PasswdGenClass()
