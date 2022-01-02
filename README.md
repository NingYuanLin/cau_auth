# cau_auth
cau 中国农业大学 校园网认证
## 功能 & 用途
在没有图形化界面的电脑上（例如Linux和WSL），登录校园网是非常困难的，此程序可以通过SHELL命令的方式来登录校园网
## 系统支持
Linux（包括WSL）、MacOS，暂不支持Windows
## 环境要求
python3，并需要安装requests包：
`pip install requests`
## 准备
### 1.知道自己使用的python解释器文件目录
一般来说，系统默认的python解释器所在目录为`/usr/bin/python3`,但这往往不是我们平时使用的，如果你平时使用anaconda工具管理python环境，可首先执行  
`conda activate 你的环境名`  
进入到你平时使用的环境，然后使用  
`which python3`  
命令获得你所使用的解释器的目录
```
(base) [root@iZj6c58ihjgkfwd8gnh3inZ ~]# which python3
/root/ning/soft/anaconda/bin/python3
```
## 配置
### 1.下载项目
可使用git或者github网页的Download ZIP
### 2.进入项目目录
`cd cau_auth`
### 3.设置你使用的python解释器
`vim src/cau.py`  
将文件第一行的内容设置为：
`#!解释器路径`  
例如我的解释器为`/root/ning/soft/anaconda/bin/python3`，我就将第一行修改为`#!/root/ning/soft/anaconda/bin/python3`
### 4.为文件增加可执行权限
`chmod +x src/cau.py`或`chmod u+x src/cau.py`
### 5.建立软链接
```
ln -s {你项目所在路径}/src/cau.py /usr/local/bin/cau
```
* 建立软链接一定要用绝对路径，不可使用相对路径
* 软链接地址可以指定到其他位置，只要在用户的环境变量里即可
## 使用方法
* 可在SHELL终端中使用`cau -h`或`cau --help`命令查看简略的使用帮助
### 1.查看当前登陆状态
```
cau -s 或 cau --check_status
```
返回结果：
```
账号已经登陆，当前登陆的用户为:XXX
```
或
```
当前未登录
```
### 2.登陆
#### 2.1 以手动指定账号密码的方式进行登录
`cau -i -u 你的用户名 -p 你的密码`  
#### 2.2 使用配置文件执行登录操作
##### 2.2.1 生成配置文件
```
cau -c 或 cau --create_config
```
根据引导，输入校园网的用户名和密码  
* 配置文件生成在当前登录用户根目录下的.cau_auth_config文件中，如需修改配置文件，可直接`rm ~/.cau_auth_config`再重新运行`cau -c`
##### 2.2.2 执行登录
```
cau -i 或 cau --login
```
即可
### 3.注销
```
cau -o 或 cau --logout
```

**👏🏻欢迎提交Issue**
