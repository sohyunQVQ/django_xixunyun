#coding=utf8
import requests
import json
import time
from datetime import datetime, date, timedelta
import random
import calendar
from xml.dom.minidom import parse
import xml.dom.minidom
from app.models import Users
import threading


class xixunyun():
    def __init__(self):
        self.session = requests.session()
        self.token = ""
        self.user_id = ""
    def login_xixun(self, classid, password, schoolid):
        post_data = {"app_version":"3.3.1",
                "registration_id":"170976fa8ab6f764b1d",
                "uuid":"02%3A00%3A00%3A00%3A00%3A00",
                "platform":"2",
                "request_source":"3",
                "password":password,
                "system":"6.0.1",
                "school_id":schoolid,
                "model":"IPHONE-X",
                "app_id":"cn.vanber.xixunyun.saas",
                "account":classid,
                "key":"y4HK8b3c3sQ0q6DqBwXgglx8NYMAXFW%2B",
        }
        try:
            data = self.session.post("https://api.xixunyun.com/login/api?platform=android&version=3.3.1&token=01c47ce30786a42cc4358c61ff02cf11&entrance_year=0&graduate_year=0",data=post_data,verify=True)
        except TimeoutError:
            data = False
        json_data = json.loads(data.text)
        try:
            self.token = json_data['data']['token']
            self.user_id = json_data['data']['user_id']
        except TypeError:
            return False
        else:
            return True

    def playcard(self, address, latitude, longitude):
        post_data={
            "address":address,
            "latitude":latitude,
            "sign_type":"0",
            "longitude":longitude
        }
        data = self.session.post("https://api.xixunyun.com/signin?platform=android&version=3.3.1&token=%s&entrance_year=0&graduate_year=0" % self.token,data=post_data,verify=True)
        json_data = json.loads(data.text)
        if json_data['code'] == 20000 or json_data['code'] == 64032:
            return True
        else:
            return False
    def write_month(self,strdate,alltext, gettext, questext):
        post_data={"end_date":strdate,
                  "business_type":"month",
                  "content":'[{"content":"%s","require":0,"sort":1,"title":"本月工作总结"},{"content":"%s","require":0,"sort":2,"title":"本月工作成果及收获"},{"content":"%s","require":0,"sort":3,"title":"下月计划安排"}]' % (alltext, gettext, questext),
                  "start_date":strdate}
        data = self.session.post("https://api.xixunyun.com/Reports/StudentOperator?platform=android&version=3.3.1&token=%s&entrance_year=0&graduate_year=0" % self.token,data=post_data, verify=True)
        json_data = json.loads(data.text)
        if json_data['code'] == 20000:
            return True
        else:
            return False
    def write_week(self,strdate, alltext, gettext,nexttext):
        post_data = {"end_date": strdate,
                     "business_type": "week",
                     "content": '[{"content":"%s","require":0,"sort":1,"title":"本周工作总结"},{"content":"%s","require":0,"sort":2,"title":"本周心得体会"},{"content":"%s","require":0,"sort":3,"title":"问题及困难反馈"}]' % (alltext, gettext, nexttext),
                     "start_date": strdate}
        data = self.session.post(
            "https://api.xixunyun.com/Reports/StudentOperator?platform=android&version=3.3.1&token=%s&entrance_year=0&graduate_year=0" % self.token,data=post_data, verify=True)
        json_data = json.loads(data.text)
        if json_data['code'] == 20000:
            return True
        else:
            return False
    def get_history(self):
        data = self.session.get("https://api.xixunyun.com/signin/student/%s?start_time=&graduate_year=0&entrance_year=0&end_time=&page_no=1&version=3.3.1&platform=android&page_size=10&token=%s" % (self.user_id, self.token))
        json_data = json.loads(data.text)
        need_data =  json_data['data']['data'][:3]
        html = ""
        for i in need_data:
            html += '<input type="radio" id="address_%s" name="address" value="%s" onclick="choose(\'%s\',\'%s\',\'%s\')" /><label for="address_%s">%s</label><br>\n' % (i['id'],i['id'],i['address'],i['latitude'],i['longitude'], i['id'], i['address'])
        return html
    def get_weekreport(self):
        self.collection = xml.dom.minidom.parse("app/static/file/report.xml").documentElement
        report_i = self.collection.getElementsByTagName("row")
        report = typeya = alltext = gettext = questext = ""
        while typeya != "week":
            report = report_i[random.randint(0,len(report_i))]
            typeya = report.getElementsByTagName('type')[0].childNodes[0].data

        alltext = report.getElementsByTagName('list1')[0].childNodes[0].data
        try:
            gettext = report.getElementsByTagName('list2')[0].childNodes[0].data
        except IndexError:
            gettext = "暂无～"

        try:
            questext = report.getElementsByTagName('list3')[0].childNodes[0].data
        except IndexError:
            questext = "暂无～"
        return (alltext,gettext,questext)

    def get_monthreport(self):
        self.collection = xml.dom.minidom.parse("app/static/file/report.xml").documentElement
        report_i = self.collection.getElementsByTagName("row")
        report = typeya = alltext = gettext = nexttext = ""
        while typeya != "month":
            report = report_i[random.randint(0,len(report_i))]
            typeya = report.getElementsByTagName('type')[0].childNodes[0].data

        alltext = report.getElementsByTagName('list1')[0].childNodes[0].data
        try:
            gettext = report.getElementsByTagName('list2')[0].childNodes[0].data
        except IndexError:
            gettext = "暂无～"

        try:
            nexttext = report.getElementsByTagName('list3')[0].childNodes[0].data
        except IndexError:
            nexttext = "暂无～"
        return (alltext, gettext, nexttext)


    def run(self,lock=False):
        def _start():
            while True:
                now = datetime.utcnow()
                while 15 < now.hour < 6:
                    print("now good time :%s" % str(now))
                    time.sleep(600)
                users = Users.objects.all()
                for user in users:
                    print("%s:login..." % user.studentid)
                    if self.login_xixun(user.studentid, user.password, user.schoolid) == False:
                        print("%s:password error" % user.studentid)
                        continue
                    else:
                        if self.playcard(address=user.address, latitude=user.latitude, longitude=user.longitude) == True:
                            print("%s:is ok" % (user.studentid))
                        else:
                            print("%s:error" % user.studentid)
                            continue
                    print("wait random time....")
                    time.sleep(random.randint(1,10))
                print("this is working is over....600s start next work")
                time.sleep(600)
        if lock:
            _start()
        else:
            getThread = threading.Thread(target=_start)
            getThread.setDaemon(True)
            getThread.start()
        
        
