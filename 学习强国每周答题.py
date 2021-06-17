from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options
import random

def get_tip(web):
    time.sleep(random.randrange(1,3))
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span').click()
    time.sleep(random.randrange(1,3))
    try:
        tips = web.find_elements_by_xpath('//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font')
    except:
        return []
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span').click()
    tip=[]
    for i in tips:
        tip.append(i.text)
    return tip

def get_kind(web):
    return web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[1]').text

def solve_tkt(web,tip):
    emps=web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input')
    t=0
    for i in emps:
        i.send_keys(tip[t])
        t+=1
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    time.sleep(random.randrange(1,3))
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[3]/div/div[1]')
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    except:
        pass




def solve_danxt(web,tip):
    op = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[4]/div')
    for i in op:
        if i.text[3:] in tip:
            i.click()
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    time.sleep(random.randrange(1,4))
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[3]/div/div[1]')
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    except:
        pass

def solve_duoxt(web,tip):
    op=web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[4]/div')
    ans=''.join(tip)
    for i in op:
        if i.text[3:] in ans:
            i.click()
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    time.sleep(random.randrange(1,3))
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[3]/div/div[1]')
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    except:
        pass

def solve_vedio(web):
    emps = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input')
    t = 0
    for i in emps:
        i.send_keys('123')
        t += 1
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    time.sleep(random.randrange(1,4))
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[3]/div/div[1]')
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    except:pass



def solve(web,tip,kind):
    if tip==[]:
        solve_vedio()
    elif kind=='填空题':
        solve_tkt(web,tip)
    elif kind=='单选题':
        solve_danxt(web,tip)
    elif kind=='多选题':
        solve_duoxt(web,tip)

def get_all_issue_name(web):
    d=[[],[]]
    names=web.find_elements_by_xpath('//div[@class="week"]')
    t=0
    for i in names:
        d[0].append(i.text)
        d[1].append(i.find_element_by_xpath('./button'))
        t+=1
    return d
def main():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.get('https://pc.xuexi.cn/points/exam-weekly-list.html')
    time.sleep(10)#请务必在10秒内进行扫码登录，否则程序将报错
    l=len(get_all_issue_name(web)[0])

    for j in range(l):
        entrance=get_all_issue_name(web)
        if '重新答题' in entrance[0][j]:
            continue

        entrance[1][j].click()
        for i in range(5):
            tip = get_tip(web)
            kind = get_kind(web)
            solve(web, tip, kind)
            time.sleep(random.randrange(2,6))
        print(entrance[0][j].split('/')[0]+'解决了！！！')
        web.back()

        time.sleep(random.randrange(2,5))






if __name__ == '__main__':
    main()
