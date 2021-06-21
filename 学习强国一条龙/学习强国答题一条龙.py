from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import random
import math


def sleep():
    time.sleep(random.randrange(2, 5))


def get_tip(web):
    time.sleep(random.randrange(1, 3))
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span').click()
        time.sleep(random.randrange(1, 3))

        tips = web.find_elements_by_xpath('//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font')

        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span').click()
        tip = []
        for i in tips:
            tip.append(i.text)
        return tip
    except:
        return []


def get_kind(web):
    return web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[1]').text


def solve_tkt(web, tip):
    emps = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input')
    t = 0
    for i in emps:
        i.send_keys(tip[t])
        t += 1
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    time.sleep(random.randrange(1, 3))
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[3]/div/div[1]')
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    except:
        pass


def solve_danxt(web, tip):
    op = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[4]/div')

    for i in op:
        if i.text[3:] in tip:
            i.click()
            break
    else:
        i.click()

    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    time.sleep(random.randrange(1, 4))
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[3]/div/div[1]')
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    except:
        pass


def solve_duoxt(web, tip):
    op = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[4]/div')
    ans = ''.join(tip)
    for i in op:
        if i.text[3:] in ans:
            i.click()
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    time.sleep(random.randrange(1, 3))
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[3]/div/div[1]')
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    except:
        pass


def solve_vedio(web):
    emps = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/div/input')
    t = 0
    for i in emps:
        i.send_keys('123')
        t += 1
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    time.sleep(random.randrange(1, 4))
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[3]/div/div[1]')
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]/button').click()
    except:
        pass


def solve(web):
    tip = get_tip(web)
    if len(tip) == 0:
        solve_vedio(web)
    else:
        kind = get_kind(web)
        if kind == '填空题':
            solve_tkt(web, tip)
        elif kind == '单选题':
            solve_danxt(web, tip)
        elif kind == '多选题':
            solve_duoxt(web, tip)


def get_all_issue_name(web):
    d = [[], []]
    names = web.find_elements_by_xpath('//div[@class="week"]')
    t = 0
    for i in names:
        d[0].append(i.text)
        d[1].append(i.find_element_by_xpath('./button'))
        t += 1
    return d


def get_all_jifeng_but(web):
    # buts=web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div')
    buts = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div')

    useful_but = [[], [], [], []]#0是题型，1是按钮，2是积分情况，3是状态

    for i in buts:
        # if i.find_element_by_xpath("./div[2]/div[2]/div").text!='已完成':
        tmp_name = i.find_element_by_xpath("./p").text
        tmp = i.find_element_by_xpath('.//div[@class="buttonbox"]')
        tmp_s = i.find_element_by_xpath('.//div[@class="my-points-card-text"]').text
        # a = int(tmp_s[0])
        # b = int(tmp_s[1][:-1])
        useful_but[0].append(tmp_name)
        useful_but[1].append(tmp)
        useful_but[2].append(tmp_s)#积分情况
        useful_but[3].append(tmp.text)
        Save_point(useful_but)
    return useful_but


def question_num(web):
    tmp = web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]').text
    a, b = tmp.split('/')
    if a == b:
        return False
    else:
        return True


def solve_anyone(web):
    time.sleep(random.randrange(2, 5))
    while question_num(web):
        solve(web)
        time.sleep(random.randrange(2, 5))

    solve(web)
    time.sleep(random.randrange(2, 5))
    web.back()


def enter_weekly(web):
    l = len(get_all_issue_name(web)[0])

    for j in range(l):
        entrance = get_all_issue_name(web)
        if '重新答题' in entrance[0][j]:
            continue

        entrance[1][j].click()
        sleep()
        solve_anyone(web)
        break
    sleep()
    web.back()


def get_special_item(web):
    items = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div/div/div/div')
    return items

#专项答题的xpath比较特色，所用到的函数都需要特色处理
def enter_special(web):
    sleep()
    items = get_special_item(web)
    for i in items:
        left = i.find_element_by_xpath('./div[1]').text
        right = i.find_element_by_xpath('./div[@class="right"]/button')

        if (right.text == "开始答题") or (right.text =='继续答题'):
            right.click()
            sleep()
            special_solve_anyone(web)
            sleep()
            web.back()
            print("专项答题——", left, "完成了")
            break


def special_solve_anyone(web):
    time.sleep(random.randrange(2, 5))
    while special_question_num(web):
        special_solve(web)
        time.sleep(random.randrange(2, 5))

    special_solve(web)
    time.sleep(random.randrange(2, 5))

    web.back()


def special_question_num(web):
    tmp = web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[2]').text
    a, b = tmp.split('/')
    if a == b:
        return False
    else:
        return True


def special_solve(web):
    tip = special_get_tip(web)

    if tip == []:
        special_solve_vedio(web)
    else:
        kind = special_get_kind(web)
        print(kind)
        if '填空题' in kind:
            special_solve_tkt(web, tip)
        elif '单选题' in kind:
            special_solve_danxt(web, tip)
        elif '多选题' in kind:
            special_solve_duoxt(web, tip)


def special_get_tip(web):
    time.sleep(random.randrange(1, 3))
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[3]/span').click()
    time.sleep(random.randrange(1, 3))
    try:
        tips = web.find_elements_by_xpath('//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font')
    except:
        return []
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[3]/span').click()
    tip = []
    for i in tips:
        tip.append(i.text)
    return tip


def special_get_kind(web):
    return web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[1]').text


def special_solve_tkt(web, tip):

    print(tip)
    emps = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[2]/div/input')
    t = 0
    for i in emps:
        i.send_keys(tip[t])
        t += 1
    sleep()
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[2]/button[2]').click()
    except:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[2]/button').click()
    time.sleep(random.randrange(1, 3))



def special_solve_danxt(web, tip):
    print(tip)
    op = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[4]/div')
    for i in op:
        print(i.text)
        if i.text[3:] in tip:
            i.click()
            break
    else:i.click()
    sleep()
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[2]/button[2]').click()
    except:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[2]/button').click()
    time.sleep(random.randrange(1, 4))


def special_solve_duoxt(web, tip):
    print(tip)
    op = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[4]/div')
    ans = ''.join(tip)
    for i in op:
        if i.text[3:] in ans:
            i.click()
    sleep()
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[2]/button[2]').click()
    except:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[2]/button').click()
    time.sleep(random.randrange(1, 3))



def special_solve_vedio(web):
    emps = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[2]/div/input')
    t = 0
    for i in emps:
        i.send_keys('123')
        t += 1
    sleep()
    try:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[2]/button[2]').click()
    except:
        web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div[2]/button').click()
    time.sleep(random.randrange(1, 4))


def changeTheHandles(web,xpth):
    web.find_element_by_xpath(f'{xpth}').click()
    sleep()
    web.close()
    web.switch_to.window(web.window_handles[0])


def changeBackMyPoint(web):
    my_learning_xpth='//*[@id="app"]/div/div[2]/div/div[1]/span[2]/span[1]/a'
    changeTheHandles(web,my_learning_xpth)
    my_point_xpth='//*[@id="app"]/div/div[2]/div/div/div[1]/div/a[3]/div/div[1]/div'
    changeTheHandles(web,my_point_xpth)


def answer(web):
    # for i in range(len(unfin_but[0])):
    #     if unfin_but[1][i].text=='去答题':
    unfin_but = get_all_jifeng_but(web)

    print(unfin_but[3])
    while '去答题' in unfin_but[3]:
        i = unfin_but[3].index('去答题')
        if unfin_but[0][i] == "每日答题":
            unfin_but[1][i].click()
            sleep()
            solve_anyone(web)
            sleep()
            changeBackMyPoint(web)
            sleep()
            unfin_but = get_all_jifeng_but(web)
        elif unfin_but[0][i] == "每周答题":
            unfin_but[1][i].click()
            sleep()
            enter_weekly(web)
            sleep()
            changeBackMyPoint(web)
            sleep()
            unfin_but = get_all_jifeng_but(web)
        elif unfin_but[0][i] == "专项答题":
            unfin_but[1][i].click()
            sleep()
            enter_special(web)
            sleep()
            changeBackMyPoint(web)
            sleep()
            unfin_but = get_all_jifeng_but(web)


def get_article_point(web):
    web.find_element_by_xpath('//*[@id="25fa"]/div/div/div/div/div/div/div[1]').click()
    sleep()
    web.switch_to.window(web.window_handles[1])
    sleep()
    get_all_article_title(web)

def get_all_article_title(web):
    with open('已经听过的音频.txt',mode='r+') as f:
        already=f.read()
    print(already)
    #already=[]
    t=0
    f=0
    while t<6:
        t=enter_each_article(web,already,t)
        sleep()
        if f==0:

            web.find_element_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div[3]/section/div/div/div/div/div/section/div/div/div[2]/div/div[5]').click()
            f+=1
        else:
            web.find_element_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div[3]/section/div/div/div/div/div/section/div/div/div[2]/div/div[7]').click()


def enter_each_article(web,already,t):
    with open('用户信息.txt', mode='r+') as r:
        a = r.readline()
    f = open(a.strip()+'已经听过的音频.txt', mode='a+')
    items = web.find_elements_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/d'
                                       'iv/section/div/div/div/div/div/section/div/div/div/div/'
                                       'div/section/div/div/div/div/div[3]/section/div/div/div/div/d'
                                       'iv/section/div/div/div[1]/div/div')


    for i in items:
        if i.text in already:
            continue
        f.write(i.text)
        i.click()
        switch_to_play_and_switch_back(web)
        t += 1
        if t == 6:
            break


    f.close()
    return t

def switch_to_play_and_switch_back(web):
    web.switch_to.window(web.window_handles[-1])
    sleep()

    play_audio(web)

    sleep()
    web.switch_to.window(web.window_handles[1])
    sleep()


def close_atrticle(web):
    try:
        web.switch_to.window(web.window_handles[1])
        web.close()
        return True
    except:
        return False


def play_audio(web):

    audio = web.find_element_by_xpath('//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[3]/div[1]/div[1]/audio')
    audio.click()
    web.execute_script("return arguments[0].play()",audio)
    sleep()
    page = web.find_elements_by_xpath(
        '//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[3]/div[1]/p')
    l=len(page)
    waittime=math.ceil(60/l)
    for i in page:
        web.execute_script("arguments[0].scrollIntoView();", i)  # 拖动到可见的元素去
        time.sleep(waittime)

def play_vedio(web):
    vedio_items=web.find_elements_by_xpath('//*[@id="6231cc81a4"]/div/div/div/div/div/div/section/div/div/div/div/div')
    t=0
    already_time=0
    for i in vedio_items:

        vedio_time=i.text[:5].split(':')
        true_time=int(vedio_time[0])*60+int(vedio_time[1])
        print(true_time,'-----',vedio_time)
        already_time+=true_time
        i.click()
        sleep()
        close_vedio(web,true_time)
        sleep()
        t+=1
        if t>=6 and already_time>360:
            break



def close_vedio(web,wait_time):
    web.switch_to.window(web.window_handles[1])
    sleep()
    title=web.find_element_by_xpath('//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div/div[2]/div[1]')
    web.execute_script("arguments[0].scrollIntoView();", title)  # 拖动到可见的元素去
    time.sleep(wait_time+random.randrange(1,3))
    web.close()
    web.switch_to.window(web.window_handles[0])


def enter_bialing(web):
    sleep()
    target = web.find_element_by_id("JEDXfdDkvQ")
    web.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
    sleep()
    web.find_element_by_xpath('//*[@id="JEDXfdDkvQ"]/div/div/div/div/div/div/span/img').click()

    sleep()
    web.close()
    web.switch_to.window(web.window_handles[0])
    sleep()
    play_vedio(web)


def back_my_point(web):
    web.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div/a').click()
    sleep()
    web.close()
    web.switch_to.window(web.window_handles[0])
    sleep()
    web.find_element_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/div[4]/section/div[4]').click()
    sleep()
    web.close()
    web.switch_to.window(web.window_handles[0])
    sleep()



def obtian_another_point(web):
    unfin_but = get_all_jifeng_but(web)
    if unfin_but[3][2]=='去看看':
        unfin_but[1][2].click()

        sleep()

        sleep()
        web.switch_to.window(web.window_handles[0])

        sleep()
        enter_bialing(web)
        sleep()
        back_my_point(web)
    unfin_but = get_all_jifeng_but(web)
    if unfin_but[3][1]=='去看看':
        unfin_but[1][1].click()

        web.switch_to.window(web.window_handles[0])
        sleep()

        sleep()


        sleep()

        get_article_point(web)


def Save_point(unfin_but):
    with open('用户信息.txt', mode='r+') as r:
        a = r.readlines()
        out = []
        for i in a:
            out.append(i.strip())
    user=out[0]
    f_name=user+'--当前积分'+'.txt'
    with open(file=f_name,mode='w+') as f:
        for i in range(len(unfin_but[0])):
            f.write(f'{unfin_but[0][i]}:{unfin_but[2][i]}\n')


def get_QRcode(web):
    iframe = web.find_element_by_xpath('//*[@id="ddlogin-iframe"]')
    web.switch_to.frame(iframe)
    img=web.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div[1]/img').screenshot_as_png
    web.switch_to.default_content()
    return img


def get_users(web):
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/span[2]/span[1]/a').click()
    sleep()
    web.close()
    web.switch_to.window(web.window_handles[0])
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/div/a[2]/div/div[2]/div[1]/span').click()
    sleep()
    web.close()
    web.switch_to.window(web.window_handles[0])
    sleep()
    us_name=web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[1]/span[2]').text
    us_information=web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div').text
    with open('用户信息.txt',mode='w+') as f:
        f.write(us_name+'\n')
        f.write(us_information)
    changeBackMyPoint(web)


def main():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.maximize_window()

    web.get('https://pc.xuexi.cn/points/my-points.html')

    with open('二维码.png',mode='wb+') as p:
        img=get_QRcode(web)
        p.write(img)

    time.sleep(10)  # 请务必在10秒内进行扫码登录，否则程序将报错
    get_users(web)
    sleep()

    answer(web)
    sleep()
    changeBackMyPoint(web)
    sleep()

    obtian_another_point(web)


def text_daily():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.get('https://pc.xuexi.cn/points/exam-practice.html')
    time.sleep(10)  # 请务必在10秒内进行扫码登录，否则程序将报错
    solve_anyone(web)


def text_special():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.get('https://pc.xuexi.cn/points/exam-paper-list.html')
    time.sleep(10)  # 请务必在10秒内进行扫码登录，否则程序将报错
    enter_special(web)


def text_article():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.get('https://www.xuexi.cn/')
    time.sleep(10)  # 请务必在10秒内进行扫码登录，否则程序将报错
    get_article_point(web)


def text_audio_play():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.get('https://www.xuexi.cn/lgpage/detail/index.html?id=560334405098711986&item_id=560334405098711986')
    time.sleep(2)
    play_audio(web)


def text_weeklyToMypoint():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.get('https://pc.xuexi.cn/points/exam-weekly-list.html')
    time.sleep(10)
    changeBackMyPoint(web)


def text_vedioplay():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.get('https://www.xuexi.cn/xxqg.html?id=c7c3b74e1887422c9733b0d22bf25498')
    time.sleep(10)
    play_vedio(web)


def text_enterbailing():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.maximize_window()
    web.implicitly_wait(3)
    web.get('https://www.xuexi.cn/')
    time.sleep(10)  # 请务必在10秒内进行扫码登录，否则程序将报错
    enter_bialing(web)


def text_backMyPoint():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.maximize_window()
    web.implicitly_wait(3)
    web.get('https://www.xuexi.cn/xxqg.html?id=c7c3b74e1887422c9733b0d22bf25498')
    time.sleep(10)  # 请务必在10秒内进行扫码登录，否则程序将报错
    back_my_point(web)


if __name__ == '__main__':
    main()