from selenium.webdriver import Chrome
import time

def gettip(web):
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span').click()
    time.sleep(2)
    tips = web.find_elements_by_xpath('//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font')
    tip=[]
    for i in tips:
        tip.append(i.text)
    return tip



def main():
    web=Chrome()
    web.get('https://pc.xuexi.cn/points/exam-practice.html')
    time.sleep(10)#请务必在10秒内进行扫码登录，否则程序将报错
    # web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span').click()
    # time.sleep(2)
    # tip=web.find_element_by_xpath('//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div').text
    print(gettip(web))

if __name__ == '__main__':
    main()