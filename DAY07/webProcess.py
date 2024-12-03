from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#%%
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https:/mail.sejong.ac.kr")
driver.maximize_window()



#mailid
mailid = driver.find_element(By.CSS_SELECTOR, "#mailid")
mailid.send_keys("ihywon")
#password
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("")

#loginForm > div.login.skin1 > section > div > div.login_content > div.login_form.non_findId > div.input_area > ul > li.btn_line > button
login_btn = driver.find_element(By.CSS_SELECTOR, "#loginForm > div.login.skin1 > section > div > div.login_content > div.login_form.non_findId > div.input_area > ul > li.btn_line > button")
login_btn.click()


#total_mail_count\
all_mail = driver.find_element(By.CSS_SELECTOR,"#total_mail_count")
all_mail.click()

#search_mail
search_mail = driver.find_element(By.CSS_SELECTOR, "#simplesearch")
search_mail.click()

#search_mail
search_mail = driver.find_element(By.CSS_SELECTOR, "#simplesearch")
search_mail.send_keys("PYTHON")
search_mail.send_keys(Keys.ENTER)


# #search_form > button:nth-child(4)
# search = driver.find_element(By.CSS_SELECTOR, "#search_form > button:nth-child(4)")
# search.click()

#wrap > div.left_area > div > div.left_write_bt.\30 7 > ul > li:nth-child(1) > button
write_mail = driver.find_element(By.CSS_SELECTOR,"#wrap > div.left_area > div > div.left_write_bt.\\30 7 > ul > li:nth-child(1) > button")
write_mail.click()

#tagit_input_to
from_who = driver.find_element(By.CSS_SELECTOR, "#tagit_input_to")
from_who.click()
from_who.send_keys("ihywon@sejong.ac.kr")

#subject
subject = driver.find_element(By.CSS_SELECTOR, "#subject")
subject.click()
subject.send_keys("python study test")

#첨부파일
file_input = driver.find_element(By.CSS_SELECTOR, "#pickfiles")

inputF = driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
inputFattrId = 0
for i, input in enumerate(inputF):
    print(f"inputF {i}: {input.get_attribute('id')}, {input.get_attribute('name')}")
    if i == 1 :
        inputFattrId = input.get_attribute('id')
print("inputFattrId" + inputFattrId)
file_input = driver.find_element(By.CSS_SELECTOR, "#"+inputFattrId)
file_input.send_keys(r"C:\\pythonRPAwithIACF\\Project\\89900100056880_1.xlsx")

# iframe 어떻게 처리하는지 gpt한테 물어보고 공부하기
