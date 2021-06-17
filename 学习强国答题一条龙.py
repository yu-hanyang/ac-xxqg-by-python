from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import random


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

    useful_but = [[], [], [], []]

    for i in buts:
        # if i.find_element_by_xpath("./div[2]/div[2]/div").text!='已完成':
        tmp_name = i.find_element_by_xpath("./p").text
        tmp = i.find_element_by_xpath('.//div[@class="buttonbox"]')
        tmp_s = i.find_element_by_xpath('.//div[@class="my-points-card-text"]').text.split('分/')
        a = int(tmp_s[0])
        b = int(tmp_s[1][:-1])
        useful_but[0].append(tmp_name)
        useful_but[1].append(tmp)
        useful_but[2].append([a, b])
        useful_but[3].append(tmp.text)
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
    # f=open('已经听过的音频.txt',mode='a+')
    # items=web.find_elements_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/d'
    #                                  'iv/section/div/div/div/div/div/section/div/div/div/div/'
    #                                  'div/section/div/div/div/div/div[3]/section/div/div/div/div/d'
    #                                  'iv/section/div/div/div[1]/div/div')
    # t=0
    #
    # for i in items:
    #     if i.text in already:
    #         continue
    #     f.write(i.text)
    #     i.click()
    #     switch_to_play_and_switch_back(web)
    #     t+=1
    #     if t==12:
    #         break
    # if t!=12:
    #
    # f.close()
    t=0
    f=0
    while t<12:
        t=enter_each_article(web,already,t)
        sleep()
        if f==0:

            web.find_element_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div[3]/section/div/div/div/div/div/section/div/div/div[2]/div/div[5]').click()
            f+=1
        else:
            web.find_element_by_xpath('//*[@id="root"]/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div[3]/section/div/div/div/div/div/section/div/div/div[2]/div/div[7]').click()


def enter_each_article(web,already,t):
    f = open('已经听过的音频.txt', mode='a+')
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
        if t == 12:
            break


    f.close()
    return t

def switch_to_play_and_switch_back(web):
    web.switch_to.window(web.window_handles[-1])
    sleep()
    #audio=web.find_element_by_xpath('//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[3]/div[1]/div[1]/audio')
    play_audio(web)
    #ActionChains(web).move_to_element_with_offset(audio,27,27).click().perform()
    sleep()
    web.switch_to.window(web.window_handles[2])
    sleep()


def play_audio(web):

    audio = web.find_element_by_xpath('//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[3]/div[1]/div[1]/audio')
    audio.click()
    web.execute_script("return arguments[0].play()",audio)
    #ActionChains(web).move_to_element_with_offset(audio, 1, 28).click().perform()



def obtian_another_point(web):
    unfin_but = get_all_jifeng_but(web)
    get_article_point(web)



def main():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.maximize_window()
    web.implicitly_wait(3)
    web.get('https://pc.xuexi.cn/points/my-points.html')
    time.sleep(10)  # 请务必在10秒内进行扫码登录，否则程序将报错
    answer(web)
    #obtian_another_point(web)


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


if __name__ == '__main__':
    main()

