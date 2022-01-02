import json
import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)
import requests
from src.core import real_auth_ip


def _check_status():
    """
    :return: 未登录：{"result":0,"m46":0,"v46ip":"10.2.246.167","myv6ip":"","sv":0,"domain":"[::]","v6":"http://[::]:9002/v6","ss5":"10.2.246.167","ss6":"10.3.38.7","vid":0,"ss1":"000d48448ce8","ss4":"000000000000","cvid":0,"pvid":0,"hotel":0,"aolno":20056,"eport":-1,"eclass":1,"zxopt":1,"AC":"","wopt":0,"v4serip":"10.3.38.7","hidm":0,"hidn":-5}
        已登录：{"result":1,"time":7376,"flow":4946277,"fsele":1,"fee":0,"m46":0,"v46ip":"10.2.246.167","myv6ip":"","oltime":4294967295,"olflow":16034816,"lip":"10.2.246.167","stime":"2021-09-11 13:40:37","etime":"2021-09-11 13:41:30","uid":"用户名","v6af":0,"v6df":0,"v46m":0,"v4ip":"10.2.246.167","v6ip":"::","AC":"用户名","ss5":"10.2.246.167","ss6":"10.3.38.7","vid":0,"ss1":"000d48448ce8","ss4":"000000000000","cvid":0,"pvid":0,"hotel":0,"aolno":19756,"eport":-1,"eclass":1,"zxopt":1,"NID":"宁远霖","olno":0,"udate":"","olmac":"000000000000","ollm":0,"olm1":"00000000","olm2":"0000","olm3":0,"olmm":1,"olm5":0,"gid":24,"actM":1,"actt":192,"actdf":10056,"actuf":0,"act6df":0,"act6uf":0,"allfm":1,"d1":0,"u1":0,"d2":0,"u2":0,"o1":0,"nd1":40224,"nu1":3116,"nd2":0,"nu2":0,"no1":0}
    """
    auth_ip = real_auth_ip.get_real_auth_ip()
    url = f"http://{auth_ip}/drcom/chkstatus?callback=dr1002&v=10311"

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://10.3.38.7/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=mve8c7kvtso03dqcknjsu22bv1'
    }

    response = requests.request("GET", url, headers=headers)

    response_text = response.text.strip()
    start_index = response_text.find('(') + 1
    response_json_text = response_text[start_index:-1]

    response_json_dict = json.loads(response_json_text)

    return response_json_dict


def check_status():
    """

    :return: is login:{'login':1,'username':'...'} else {'login':0,'username':''}
    """
    status_info_dict = _check_status()
    result = status_info_dict['result']
    if result == 1:
        username = status_info_dict['NID']
        ac = status_info_dict['AC']  # 用户名
    else:  # result == 0
        username = ''
        ac = ''

    res = {
        'login': result,
        'username': username,
        'AC': ac
    }

    return res


def main():
    print(check_status())


if __name__ == '__main__':
    main()
