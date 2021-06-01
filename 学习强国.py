from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options

def get_tip(web):
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span').click()
    time.sleep(2)
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
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()




def solve_danxt(web,tip):
    op = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[4]/div')
    for i in op:
        if i.text[3:] in tip:
            i.click()
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()

def solve_duoxt(web,tip):
    op=web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[4]/div')
    for i in op:
        if i.text[3:] in tip:
            i.click()
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()

def solve_vedio(web):
    emps = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input')
    t = 0
    for i in emps:
        i.send_keys('123')
        t += 1
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()



def solve(web,tip,kind):
    if len(tip)==0:
        solve_vedio()
    elif kind=='填空题':
        solve_tkt(web,tip)
    elif kind=='单选题':
        solve_danxt(web,tip)
    elif kind=='多选题':
        solve_duoxt(web,tip)


def main():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.get('https://pc.xuexi.cn/points/exam-practice.html')
    time.sleep(10)#请务必在10秒内进行扫码登录，否则程序将报错
    # web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span').click()
    # time.sleep(2)
    # tip=web.find_element_by_xpath('//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div').text
    for i in range(5):
        tip=get_tip(web)
        kind=get_kind(web)
        print(tip)
        print(kind)
        print('=======')
        solve(web,tip,kind)
        time.sleep(2)



if __name__ == '__main__':
    main()