# cau_auth
cau 中国农业大学 校园网认证  
```
pip install cau
```
🎉[golang版本已发布](https://github.com/NingYuanLin/cau_go)
## 功能 & 用途
在没有图形化界面的电脑上（例如Linux和WSL），登录校园网是非常困难的，此程序可以通过命令行的方式来登录校园网  
当然，在macos和windows上也是支持的，并且可能比手动在浏览器上操作要快一些
## 系统支持
Linux（包括WSL）、MacOS，Windows
## 使用方法
> 可在SHELL终端中使用`cau -h`或`cau --help`命令查看简略的使用帮助
### 1.查看当前登录状态
```
cau -s 或 cau --check_status
```
返回结果：
```
账号已经登录，当前登录的用户为:XXX
```
或
```
当前未登录
```
### 2.登录
#### 2.1 以手动指定账号密码的方式进行登录
```
cau -i -u 你的用户名 -p 你的密码
```  
此方法较为繁琐  
#### 2.2 使用配置文件执行登录操作
##### 2.2.1 生成配置文件
```
cau -c 或 cau --create_config
```
根据引导，输入校园网的用户名和密码  
> 配置文件生成在当前登录用户根目录下的.cau_auth_config文件中，如需修改配置文件，可直接`rm ~/.cau_auth_config`再重新运行`cau -c`
##### 2.2.2 执行登录
```
cau -i 或 cau --login
```
即可
### 3.注销
```
cau -o 或 cau --logout
```
## 常见问题
1. 使用虚拟环境执行`pip install cau`，退出虚拟环境后，发现无法执行`cau`命令？  
先在虚拟环境下，执行`which cau(macos & linux) or where(cmd in windows)`找到文件路径，再建立软链接到在环境变量里的目录  

**👏🏻欢迎提交Issue**
