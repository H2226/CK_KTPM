from selenium import webdriver

# Khởi chạy trình duyệt Chrome (đảm bảo bạn đã tải ChromeDriver)
driver = webdriver.Chrome()

# Mở trang Google
driver.get("https://www.google.com")

# In ra tiêu đề trang
print(driver.title)

# Đóng trình duyệt
driver.quit()