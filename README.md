SINA WEIBO Login Simulator      

A Python implementation of SINA WEIBO Login Simulator with RSA2 Encryption
使用Python模拟用户登录新浪微博，用户登录密码使用RSA2加密方式。    

## Prerequirement
    $ 安装python2.7 Firefox+HttpFox或类似调试工具    
## Configuration    
    $ 需要修正的参数可能有
        prelogin_url
        weibo_rsa_e
        weibo_rsa_n
        login_data
    $ 在火狐浏览器下打开http://weibo.com/进行微博登录 在HttpFox中找到method=get  url=`http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.   preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1397599558009`
    $ 根据请求prelogin_url链接地址：`http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1397592604677`
    修改 源代码中prelogin_url中的内容     
    $ 点击content 格式化后 看到提交所需要的参数 如下      
        sinaSSOController.preloginCallBack({
        "retcode": 0,
        "servertime": 1397621722,
        "pcid": "gz-36d09bc3b0d39641836cd121d2a132fd1317",
        "nonce": "3X1LV9",
        "pubkey": "EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443",
        "rsakv": "1330428213",
        "uid": "1998662112",
        "exectime": 2
        })      
    $  成功登录后在HttpFox中找到method =post url='http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.11)1 ​点击postdata 看到 登录时提交的参数如下   
        entry = weibo & gateway = 1 & from = &savestate = 7 & useticket = 1 & pagerefer = http % 3A % 2F % 2Flogin.sina.com.cn % 2Fsso % 2Flogout.php % 3Fentry % 3Dminiblog % 26r % 3Dhttp % 253A % 252F % 252Fweibo.com % 252Flogout.php % 253Fbackurl % 253D % 25252F & vsnf = 1 & su = ZWR3aW5fdWVzdGMlNDAxNjMuY29t & service = miniblog & servertime = 1397622469 & nonce = J4A5RE & pwencode = rsa2 & rsakv = 1330428213 & sp = 6a9d57682c7238e1a6ba7c76ccde277f784788c414d88fb7e09041f91030f0a239e8d2e25d26e2c581dcd37a7faae1f20d45f60735a1212eb0d7a6d4c7ae9042ecff3d7e24de504b1f9d8ff3c995a451811e963a38e8fd3c771b612c17f6e8561164c459369dd6ee3bb0713c5ed5a2dec352075cd29776a99350ed7b72d12429 & encoding = UTF - 8 & prelt = 525 & url = http % 3A % 2F % 2Fweibo.com % 2Fajaxlogin.php % 3Fframelogin % 3D1 % 26callback % 3Dparent.sinaSSOController.feedBackUrlCallBack & returntype = META     
        如有需要修改login_data
    $   点击content 在script中看到返回参数    
    <script>
    try {
        sinaSSOController.setCrossDomainUrlList({
            "retcode": 0,
            "arrURL": ["http:\/\/crosdom.weicaifu.com\/sso\/crosdom?action=login&savestate=1429158471"]
        });
    } catch(e) {}
    try {
        sinaSSOController.crossDomainAction('login',
        function() {
            location.replace('http://weibo.com/sso/login.php?ssosavestate=1429158471&url=http%3A%2F%2Fweibo.com%2Fajaxlogin.php%3Fframelogin%3D1%26callback%3Dparent.sinaSSOController.feedBackUrlCallBack%26sudaref%3Dweibo.com&ticket=ST-MTk5ODY2MjExMg==-1397622471-gz-F088A1D0AE5D39DEE23B506AC311C5A8&retcode=0');
        });
    } catch(e) {}    
    根据此内容修改源程序中`p = re.compile('location\.replace\(\“(.*?)\"\)')` 由于sina自身的变化 原来的双引号变成了现在的单引号 故将此正则修改为`p = re.compile('location\.replace\(\'(.*?)\'\)') 说明：stackoverflow上说单引号无需转义 但经测试是需要用\转义的 否则是无法获取变量的
    $   代理设置 由于公司网络 只需在源程序中添加如下代码
    ##公司代理设置
    enable_proxy = True
    proxy_handler = urllib2.ProxyHandler({"http" : 'http://10.1.2.188:80'})
    null_proxy_handler = urllib2.ProxyHandler({})

    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)

    urllib2.install_opener(opener)
    print 'sucessfully set the proxy!'
`
## Usage
1. 替换main方法中的username 和password
2. `python weibo_login.py`
3. success  

#References
* 具体参数的获取请参考[[方便查看] 新浪微博爬虫系列之模拟登录](http://blog.csdn.net/yonglaixiazaide/article/details/7923468)
* 关于re模块中对于单引号的转义的问题请[参考](http://stackoverflow.com/questions/14378998/javascript-regular-expression-single-quotes)  

#Contributor
yoyzhou    [找我](iamyoyozhou@gmail.com)  
wanghaisheng    [找我](edwin_uestc@163.com)    

#LICENSING
Copyright(C) 2013 Yoyo Zhou. Distributed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).  See the `LICENSE` file for details.


