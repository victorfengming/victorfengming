# 在gitee.txt文件种
# 第一行输入用户名
# 第二行输入密码
# 第三行输入giteepages地址('https://gitee.com/此处改为你的gitee_id/此处改为你的gitee_id/pages')


# 因为是通过相对路径引用，且程序逻辑没有写完全，所以此目录里文件的位置和命名不要变动，否则无法正常运行


import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

option = webdriver.ChromeOptions()
option.binary_location = r'E:\chrome\App\chrome.exe'
option.add_argument('''--no-sandbox''')
# 谷歌文档提到需要加上这个属性来规避bug
option.add_argument('''--disable-gpu''')
# driver = webdriver.Chrome()
# driver = webdriver.Edge()
driver = webdriver.Chrome(chrome_options=option)
# driver.get('https://www.baidu.com')

# 模拟浏览器打开到gitee登录界面
# driver = webdriver.Chrome()
# driver.get('https://github.com/login')
driver.get('https://gitee.com/login')
# 将窗口最大化
driver.maximize_window()
time.sleep(2)

# 输入账号--通过html的id属性定位输入位置--改为你的账号
user_login = driver.find_element_by_id('user_login')
user_login.send_keys("victorfengming")
# 输入密码--通过html的id属性定位输入位置--改为你的密码
driver.find_element_by_id('user_password').send_keys("21EWsn")
# 点击登录按钮--通过xpath确定点击位置
driver.find_element_by_xpath(
    '//*[@id="new_user"]/div/div/div/div[4]/input').click()


# //*[@id="new_user"]/div/div/div/div[4]/input

time.sleep(2)

# 切换到gitee pages界面--改为you_gitee_id
driver.get('https://gitee.com/victorfengming/go-camp/pages')
# 点击更新按钮--通过xpath确定点击位置
driver.find_element_by_xpath('//*[@id="pages-branch"]/div[6]').click()

# 确认更新提示框--这个函数的作用是确认提示框
Alert(driver).accept()

# 等待5秒更新
time.sleep(5)

# 这个print其实没事什么用,如果真的要测试脚本是否运行成功，可以用try来抛出异常
print("成功")

# 脚本运行成功,退出浏览器
driver.quit()

# 写上更新日志
# 我这里是写在D盘，可以改为自己喜欢的目录
fp = open("./log.txt", "a+")
now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
fp.write("部署时间:{0}\n".format(now_time))
fp.close()
