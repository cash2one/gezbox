#__author__ quxl
#项目运行步骤
#cd /path/to/gezbox/
#mkdir env
#virtualenv env
#source env/bin/active
#pip install -r requirements.txt
#将lib下的piston 目录拷贝到 env/lib/site-packages  piston 最新版本有bug。所以只能用这个版本，项目内的piston 为老版本
#python manage.py syncdb
#python manage.py runserver 8080
#本机浏览器内输入  http://localhost:8080
#只有走注册接口 注册的用户 才会产生 储蓄账户信息，syncdb 时 产生的超级管理员 是不具备这方面信息，实在经理和时间不够，否则改造syncdb
#命令也可完成

如果是本地 则 将 {{host}} 替换为  localhost:8080

如果用过postman  则可以导入如下地址
https://www.getpostman.com/collections/6b103a4fe19759d608f7

接口地址:
注册      http://{{host}}/api/accounts/login/
           参数:username 用户名
               password  密码

登录      http://{{host}}/api/accounts/login/
           参数:username 用户名
               password  密码

注销      http://{{host}}/api/accounts/logout/

创建订单   http://{{host}}/api/feng/orders/
            参数: descr 描述
                  price 价格

获取我的订单 http://{{host}}/api/feng/orders/

接受订单    http://{{host}}/api/orders/(?P<order_id>\d+)/accept/


在生产环境中主要通过uwsgi  和 nginx 进行连接
启动命令  uwsgi --ini gezbox.com.ini

在nginx 里配置了 负载均衡的机器。可以根据机器能里配置nginx 工作进程数

如果mysql 的的读写操作成为 接口瓶颈，可以考虑采用 redis 内存数据库 作为主数据库的方式，提高相应速度。
但是这得等到具有一定业务量之后再考虑实施。


supervisor 没怎么用过，初步了解，是用来守护进程用的，防止进程挂掉。如果有需要可以深入了解研究

