from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "com.shizhuang.duapp",
    "appActivity": "modules.home.ui.SplashActivity"
}
driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=desired_caps)
# print(driver)


element = driver.find_element(by="id", value="com.shizhuang.duapp:id/agree_tv")
text = element.text
# print(text)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.shizhuang.duapp:id/button_layout')))
# Нажатие на кнопку
button.click()


driver.implicitly_wait(30)
driver.find_element(By.ID, "com.shizhuang.duapp:id/btn_close").click()
driver.implicitly_wait(30)

print(driver.get_window_size())
# Выполнение свайпа с использованием метода driver.swipe
start_x = 250
start_y = 780
end_x = 250
end_y = 400
duration = 100  # Длительность свайпа в миллисекундах

# # driver.swipe(start_x, start_y, end_x, end_y, duration)
# action = TouchAction(driver)
# action.press(x=start_x, y=start_y).wait(duration).move_to(x=end_x, y=end_y).release().perform()

# driver.swipe(start_x, start_y, end_x, end_y, duration)
action = TouchAction(driver)
action.press(x=start_x, y=start_y).wait(duration).move_to(x=end_x, y=end_y).release().perform()


# item_field = driver.find_element(By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView')


# items = driver.find_element(By.CLASS_NAME, value='androidx.recyclerview.widget.RecyclerView')
# print(len(items.find_elements(By.CLASS_NAME, value='android.widget.FrameLayout')))

# y = driver.find_element(By.ID, value='com.shizhuang.duapp:id/mall_product_card_price_id')
# print(y.text)
# print(item.find_element(By.XPATH, value='/android.widget.LinearLayout/android.widget.TextView'))
# items = []
# i = 0
# while True:
#     i += 1
#     items.append(driver.find_elements(By.XPATH, f'(//android.widget.FrameLayout[@content-desc="product_item"])[{i}]'))
#     print(items)
# print(items[0].text)
# Закрытие драйвера
driver.quit()