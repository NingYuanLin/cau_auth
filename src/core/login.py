import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)
import requests
import json
from src.core import real_auth_ip
from src.core import check_status


def _login(username, password, auth_ip):
    base_url = "http://{auth_ip}/drcom/login?callback=dr1003&DDDDD={username}&upass={password}&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&v=6817"
    url = base_url.format(auth_ip=auth_ip, username=username, password=password)

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://10.3.38.7/a79.htm?isReback=1',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=mve8c7kvtso03dqcknjsu22bv1'
    }

    response = requests.request("GET", url, headers=headers)

    response_text = response.text.strip()
    response_dict = response_text[response_text.find('{'):-1]
    response_dict = json.loads(response_dict)
    is_success = response_dict['result']
    if is_success == 0:
        msg = response_dict['msga']
    else:
        msg = ''
    return is_success, msg


def login(username, password):
    """

    :param username:
    :param password:
    :return: dr1003({"result":1,"aolno":20554,"m46":0,"v46ip":"10.2.246.167","myv6ip":"","sms":0,"ufee":0,"NID":"宁远霖","olno":1,"udate":"","olmac":"000000000000","ollm":0,"olm1":"00000000","olm2":"0000","olm3":0,"olmm":2,"olm5":0,"gid":24,"olno":1,"olip":"10.6.56.59","oaf":101847,"oat":17707,"mac1":"","mac2":"","mac3":"","mac4":"","mac5":"","mac6":"","ac0":"czIwMjEzMDgxNTIw","oltime":4294967295,"olflow":16147456,"lip":"10.2.246.167","stime":"2021-09-11 13:08:50","etime":"2021-09-11 13:11:38","uid":"用户名","UL":"http://wdl1.cache.wps.cn/per-plugin/dl/addons/list/win-i386/3.7.0.5929/wpsoffice/index.ini","sv":0})
    """
    # 先验证账号是否登录，如果已经登录了，还进行登录操作，回导致接口阻塞无法获取返回值，并且原登录态会退出
    status_info_dict = check_status.check_status()
    is_login = status_info_dict['login']
    if is_login == 1:
        login_username = status_info_dict['username']
        msg = f'账号已经登陆，当前登陆的用户为:{login_username}'
        return 0, msg

    auth_ip = real_auth_ip.get_real_auth_ip()

    # print(auth_ip)

    is_success, msg = _login(username, password, auth_ip)

    if is_success == 0:
        # 在部分网关下，需要在username后加上 @ cau才能正确登录
        is_success, msg = _login(username + '@cau', password, auth_ip)

    return is_success, msg

    pass


def main():
    username = '用户名'
    password = '密码'
    print(login(username, password))


if __name__ == '__main__':
    main()
