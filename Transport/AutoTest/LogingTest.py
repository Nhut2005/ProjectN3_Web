import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class PythonOrgSearch(unittest.TestCase):
    # Initialization of WebDriver
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Cleanup method called after every test
    def tearDown(self):
        self.driver.quit()
    #TH1: uername dung, pw sai
    #TH2: uername sai, pw dung
    #TH3: Nhập đúng cả username và password
    #TH4: No input 
    def test_unit_login1(self):
        print('Bắt đầu kiểm tra đăng nhập với username đúng và password sai')
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

        # Nhập đúng username
        inputUserName = driver.find_element(By.NAME, "username")
        inputUserName.send_keys("admin")  # Thay bằng username đúng

        # Nhập sai password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("wrong_password")  # Thay bằng password sai
        password.send_keys(Keys.RETURN)

        time.sleep(3)  # Chờ trang tải

        # Kiểm tra thông báo lỗi
        try:
            error_message = driver.find_element(By.CSS_SELECTOR, ".errornote").text
            print(f"Lỗi hiển thị: {error_message}")
            self.assertIn("Please enter the correct", error_message) 
        except:
            print("Không tìm thấy thông báo lỗi! Test thất bại.")
            self.fail("Không hiển thị thông báo lỗi khi nhập sai password.")

    def test_unit_login2(self):
        print('Bắt đầu kiểm tra đăng nhập với username sai và password đúng')
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

        # Nhập sai username
        inputUserName = driver.find_element(By.NAME, "username")
        inputUserName.send_keys("wrong_username")  # Thay bằng username sai

        # Nhập đúng password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("123")  
        password.send_keys(Keys.RETURN)

        time.sleep(3)  # Chờ trang tải

        # Kiểm tra 
        try:
            error_message = driver.find_element(By.CSS_SELECTOR, ".errornote").text
            print(f"Lỗi hiển thị: {error_message}")
            self.assertIn("Please enter the correct", error_message)  # Kiểm tra thông báo lỗi chứa nội dung mong đợi
        except:
            print("Không tìm thấy thông báo lỗi! Test thất bại.")
            self.fail("Không hiển thị thông báo lỗi khi nhập sai username.")

    def test_unit_login3(self):
        print('Bắt đầu kiểm tra đăng nhập')
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        
        # Nhập username
        inputUserName = driver.find_element(By.NAME, "username")
        inputUserName.send_keys("admin")  # Thay bằng username thực tế
        
        # Nhập password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("123")  # Thay bằng password thực tế
        password.send_keys(Keys.RETURN)

        time.sleep(3)  # Chờ trang tải
        
        # Kiểm tra tiêu đề trang
        actualTitle = driver.title
        print(actualTitle)
        self.assertEqual(actualTitle, "Site administration | Django site admin")
    
    def test_unit_login_no_credentials(self):
        print('Bắt đầu kiểm tra đăng nhập khi không nhập username và password')
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

        # Không nhập username
        inputUserName = driver.find_element(By.NAME, "username")
        inputUserName.send_keys("")  # Không nhập username

        # Không nhập password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("")  # Không nhập password
        password.send_keys(Keys.RETURN)

        time.sleep(3)  # Chờ trang tải

        # Kiểm tra thông báo lỗi
        try:
            error_message = driver.find_element(By.CSS_SELECTOR, ".errornote").text
            print(f"Lỗi hiển thị: {error_message}")
            self.assertIn("This field is required", error_message)  # Kiểm tra thông báo lỗi yêu cầu điền username và password
        except:
            print("Không tìm thấy thông báo lỗi! Test thất bại.")
            self.fail("Không hiển thị thông báo lỗi khi không nhập username và password.")


if __name__ == "__main__":
    unittest.main()
