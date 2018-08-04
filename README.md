# 习讯云签到自动化

这是一个使用django编写的一个习讯云自动签到网站


###如何使用?
```shell
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

运行好后访问网址

 ::url/start

 ::url 为你的部署域名  访问上面网站后开启自动签到

##网站有什么功能


* 可以根据学校代码编辑可以使用在支持全部学校
* 无限循环判断，只在日常时间进行打卡(可以在代码内修改)
* 访问后台 admin/ 可以管理已添加账户


##有问题反馈
在使用中有任何问题，欢迎反馈给我，可以用以下联系方式跟我交流

* 邮件(abigeater#163.com, 把#换成@)



##关于作者

```Python
  Class Me():
    nickName: "abigeater",
    site: "http://abigeater.com"
```
