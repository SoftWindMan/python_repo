书籍《虫师selenium python自动化测试》中的学习实例

webdriver的原理：
  1、webdriver启功浏览器并绑定指定端口，该浏览器实例作为web driver的Remote server；
  2、Clint端通过CommandExecuter发送HTTPResquest给remote server监听端口；
  3、Remoteserver需要依赖原生的浏览器组件转化浏览器的native调用。

webdriver三种等待：
  1、time.sleep(1)：强制等待，最好不用；
  2、driver.implicitly_wait(10)：隐性等待，一般都用；
  3、from selenium.webdriver.support.wait import WebDriverWait
     from selenium.webdriver.support import expected_conditions as EC
     from selenium.webdriver.common.by import By
     WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_loacated((By.CLASS_NAME, 'class attribute')))
     显性等待，比如点击登录按钮后确定登录成功时使用。
   
   
