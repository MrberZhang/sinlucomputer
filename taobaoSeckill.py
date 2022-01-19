# 淘宝秒杀

# 导入模块，我们需要一个时间模块，抢购的时间，还有一个Python的自动化操作。
import datetime  # 模块
import time
from selenium import webdriver   # 全自动化Python代码操作

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


# 根据我们的思路，首先需要程序帮我们打开谷歌浏览器，并输入“www.taobao.com”，然后点击登录，进入到购物车
times = "2021-11-04 21:00:00.00000000"
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
time.sleep(3)                               # 点击
browser.find_element_by_link_text("亲，请登录").click()

# 我们不能把我们的账户、密码写在代码里边，这样很容易泄露，所以这里采取手动扫码登录
print(f"请尽快扫码登录")
time.sleep(10)
browser.get("https://cart.taobao.com/cart.htm")
time.sleep(3)

# 进入购物车，等待抢购时间然后购买。 首先这个程序不能帮我们去挑选商品，所以我们得提前把商品加入到购物车里面。等到了抢购时间，直接全选商品购买就可以了
# 是否全选购物车
while True:
    try:
        if browser.find_element_by_id("J_SelectAll1"):
            browser.find_element_by_id("J_SelectAll1").click()
            break
    except:
        print(f"找不到购买按钮")




while True:
    # 获取电脑现在的时间, year month day
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # 对比时间，时间到的话就点击结算
    print(now)
    # 判断是不是到了秒杀时间?
    if now > times:
        # 点击结算按钮
        while True:
            try:
                if browser.find_element_by_link_text("结 算"):
                    print("here")
                    browser.find_element_by_link_text("结 算").click()
                    print(f"主人,程序锁定商品,结算成功")
                    break
            except:
                pass
        # 点击提交订单按钮
        while True:
            try:
                if browser.find_element_by_link_text('提交订单'):
                    browser.find_element_by_link_text('提交订单').click()
                    print(f"抢购成功，请尽快付款")
            except:
                print(f"主人,我已帮你抢到商品啦,您来支付吧")
                break
        time.sleep(0.01)

