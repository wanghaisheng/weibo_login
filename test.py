import re
#coding:utf-8
#对应单引号在re模块中转义的使用 第二行代码是为了避免中文显示的问题而添加的
#参考材料 http://stackoverflow.com/questions/14378998/javascript-regular-expression-single-quotes

text = "location.replace('http://weibo.com/sso/login.php?ssosavestate=1429158471&url=http%3A%2F%2Fweibo.com%2Fajaxlogin.php%3Fframelogin%3D1%26callback%3Dparent.sinaSSOController.feedBackUrlCallBack%26sudaref%3Dweibo.com&ticket=ST-MTk5ODY2MjExMg==-1397622471-gz-F088A1D0AE5D39DEE23B506AC311C5A8&retcode=0'"
p1 = re.compile('location\.replace\(\'(.*?)\'\)')
#p2 = re.compile('location\.replace\('(.*?)'\)')
p3 = re.compile('location\.replace\(\"(.*?)\"\)')
print p1.search(text)   #使用\转义单引号
#print p2.findall(text)   #不使用\转义单引号
print p3.search(text)   #使用\转义双引号
 