import os, time
from dotenv import load_dotenv
from driver import WebDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

email_fb = os.getenv('EMAIL_FB')
password_fb = os.getenv('PASSWORD_FB')
link_login = os.getenv('LINK_LOGIN')
link_group = os.getenv('LINK_GROUP')

driver = WebDriverManager()

# LOGIN KE AKUN  FACEBOOK
driver.authentication(link_login, email_fb, password_fb)
time.sleep(5)

driver.get(link_group)
time.sleep(3)

# SCROLL HALAMAN GROUP FACEBOOK
driver.scroll(4)
time.sleep(3)

# MENGAMBIL SEMUA POSTINGAN
feed = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
feed_posts = feed.find_elements(By.XPATH, './div')

for post in feed_posts:
    try:
        # Tombol komentar postingan
        button_comment = post.find_element(By.CSS_SELECTOR, 'div[aria-label="Beri komentar"][role="button"]')
        button_comment.click()

        # Berpindah ke input komentar yang aktif
        input_comment = driver.switch_to.active_element
        input_comment.send_keys("Jasa CV Online Terbaik")
        input_comment.send_keys(Keys.SHIFT, Keys.ENTER)
        input_comment.send_keys("WhatsApp : 0821 3763 3527")
        input_comment.send_keys(Keys.ENTER)

        print("Komentar berhasil dikirim!")

        time.sleep(30)
    except:
        continue

driver.quit()
print("Program berhasil dijalankan")