#coding:gbk
def main(config):
    print('Welcome to Web WHOIS test')
    print('============================')
    print('< Press enter to start program...>')
    input()
    print('Start...')
    import os
    os.system("del result.txt")
    import time
    time.sleep(1)
    print('loading resource',end='')
    import whois
    a = open(config,'r')
    url = str(a.read())
    data = url.split('\n')
    print(' -- Ok')
    print('began to test\n')
    print("======================")
    exp = {}
    times = 0

    for i in data:
        try:
            print("Detect: " + str(times) + ' Website'+ '\r',end='')
            times += 1
            try:
                inf = whois.whois(i)

                webDatePreTreat = inf['expiration_date']

                if type(webDatePreTreat) == list:
                    webPre = str(webDatePreTreat[0])
                else:
                    webPre = str(webDatePreTreat)

                exp[i] = webPre

            except whois.parser.PywhoisError:
                exp[i] = '<<<<< Have not been registered yet !!'
                continue
        except BaseException:
            exp[i] = '?????? Error'
            continue


    print('\nFinish detect !')
    print("======================\n")

    a = open('result.txt', 'a')
    web = list(exp.keys())
    date = list(exp.values())
    for i in range(1, len(web)):
        content = web[i] + "   :   " + date[i]
        a.write(content + '\n')

import sys
data = sys.argv

if len(data) != 2:
    print("Code Instruction: testweb [web config file]")
else:
    file = sys.argv[1]
    try:
        main(file)
    except BaseException:
        print('Program Error, Please Try again')