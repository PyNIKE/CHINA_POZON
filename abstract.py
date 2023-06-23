from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import datetime



desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "com.shizhuang.duapp",
    "appActivity": "modules.home.ui.SplashActivity"
}
driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=desired_caps)

# Получить данные о размере экрана
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# Проведите вниз по экрану
def swipeUp():
    l = getSize()
    x1 = int(l[0] * 0.5)  # x координата
    y1 = int(l[1] * 0.9)  # Начальная координата y
    y2 = int(l[1] * 0.1)  # Координата Y конечной точки
    driver.swipe(x1, y1, x1, y2)


# Проведите вверх по экрану
def swipeDown():
    l = getSize()
    x1 = int(l[0] * 0.5)  # x координата
    y1 = int(l[1] * 0.25)  # Начальная координата y
    y2 = int(l[1] * 0.75)  # Координата Y конечной точки
    driver.swipe(x1, y1, x1, y2)


# Определить, существует ли указанный элемент
def isElement(driver, identifyBy, c):
    time.sleep(1)
    flag = False
    try:
        if identifyBy == "id":
            driver.find_element_by_id(c)
        elif identifyBy == "xpath":
            driver.find_element_by_xpath(c)
        elif identifyBy == "class":
            driver.find_element_by_class_name(c)
        elif identifyBy == "link text":
            driver.find_element_by_link_text(c)
        elif identifyBy == "partial link text":
            driver.find_element_by_partial_link_text(c)
        elif identifyBy == "name":
            driver.find_element_by_name(c)
        elif identifyBy == "tag name":
            driver.find_element_by_tag_name(c)
        elif identifyBy == "css selector":
            driver.find_element_by_css_selector(c)
        flag = True
    except Exception as e:
        flag = False
    finally:
        print("результат")
        return flag



driver.find_element(By.XPATH,
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
time.sleep(2)
# Нажмите кнопку поиска пользователя
# driver.find_element_by_id("com.xingin.xhs:id/c8t").click()
driver.find_element(By.XPATH,
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.a.b[3]/android.widget.TextView").click()
time.sleep(1)
# Нажмите первую
driver.find_element(By.XPATH,
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]").click()
time.sleep(1)
# Нажмите, чтобы показать только видео
driver.find_element(By.XPATH,
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.TextView").click()
time.sleep(1)

#


if (isElement(driver, "xpath",
              "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.TextView")):
    print("tag：" + driver.find_element(By.XPATH,
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.TextView").text)
else:
    print("Без тега")
print("likeNum：" + driver.find_element(By.ID,"com.xingin.xhs:id/likeTextView").text)
print("collectNum：" + driver.find_element(By.ID,"com.xingin.xhs:id/qz").text)
print("commentNum：" + driver.find_element(By.ID,"com.xingin.xhs:id/commentTextView").text)
print("==========")
# Нажмите кнопку "Назад"
driver.find_element(By.ID,"com.xingin.xhs:id/backButton").click()
time.sleep(1)


driver.find_element(By.XPATH,
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageView[1]").click()
time.sleep(0.5)
driver.find_element(By.XPATH,
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView").click()
time.sleep(0.5)
driver.find_element(By.XPATH,
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView").click()
time.sleep(0.5)

print(datetime.datetime.now())