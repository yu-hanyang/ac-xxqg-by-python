from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options
import random


def sleep():
    time.sleep(random.randrange(2, 5))


def get_tip(web):
    time.sleep(random.randrange(1, 3))
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span').click()
    time.sleep(random.randrange(1, 3))
    try:
        tips = web.find_elements_by_xpath('//*[@id="body-body"]/div[4]/div/div/div/div[2]/div/div/div/font')
    except:
        return []
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[3]/span').click()
    tip = []
    for i in tips:
        tip.append(i.text)
    return tip


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
    emps = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input')
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
    if tip == []:
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
        solve_anyone()
        break
    web.back()


def get_special_item(web):
    items = web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div/div/div/div')
    return items


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


def answer(web):
    # for i in range(len(unfin_but[0])):
    #     if unfin_but[1][i].text=='去答题':
    unfin_but = get_all_jifeng_but(web)
    while '去答题' in unfin_but[3]:
        i = unfin_but[3].index('去答题')
        if unfin_but[0][i] == "每日答题":
            unfin_but[1][i].click()
            sleep()
            solve_anyone(web)
            web.back()
            sleep()
            unfin_but = get_all_jifeng_but(web)
        elif unfin_but[0][i] == "每周答题":
            unfin_but[1][i].click()
            sleep()
            enter_weekly(web)
            web.back()
            sleep()
            unfin_but = get_all_jifeng_but(web)
        elif unfin_but[0][i] == "专项答题":
            unfin_but[1][i].click()
            sleep()
            enter_special(web)
            web.back()
            sleep()
            unfin_but = get_all_jifeng_but(web)


def main():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option("detach", True)

    web = Chrome(options=option)
    web.get('https://pc.xuexi.cn/points/my-points.html')
    time.sleep(10)  # 请务必在10秒内进行扫码登录，否则程序将报错
    answer(web)


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


if __name__ == '__main__':
    main()
