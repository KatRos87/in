from selenium import webdriver
import time
import re

# log/pass
f = open("files/sign.txt", "r", encoding='utf-8')
for line in f:
    x = line.split(":")
    print(x)
    username = x[0]
    password = x[1]
f.close()

time.sleep(.5)
# comment
fc = open("files/cat_comment_rus.txt", "r", encoding='utf-8')
for line in fc:
    comment = line
fc.close()
print(comment)
time.sleep(2)
# tags
ft = open("files/cat_tags_rus.txt", "r", encoding='utf-8')
time.sleep(2)
tags = []
for line in ft:
    tags.append("#" + line[:-1])
tags[-1] += '\n'
ft.close()
time.sleep(2)

browser = webdriver.Chrome(executable_path="driver/chromedriver")

# entrance
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(1)
path_form = "//section/main/div/article/div/div[1]/div/form/"
for c in username:
    browser.find_element_by_xpath(xpath= path_form + "div[2]/div/label/input").send_keys(c)
    time.sleep(.3)
time.sleep(1)
for c in password:
    browser.find_element_by_xpath(xpath= path_form + "div[3]/div/label/input").send_keys(c)
    time.sleep(.3)
time.sleep(1)
browser.find_element_by_xpath(xpath="//section/main/div/article/div/div[1]/div/form/div[4]/button").click()
time.sleep(5)

# Action on the site with the selfname
browser.get("https://www.instagram.com/" + username + "/")
time.sleep(3)

# go to the first post 
browser.find_element_by_xpath(
    xpath="//section/main/div/div[2]/article/div/div/div[1]/div[1]/a").click()
time.sleep(2)

# comment in the post
path_post = "/html/body/div[4]/div[2]/div/article/div[2]/"
path_comment = path_post + "section[3]/div/form/"
browser.find_element_by_xpath(xpath=path_comment + "textarea").click()
time.sleep(1)

for c in comment:
    browser.find_element_by_xpath(xpath = path_comment + "textarea").send_keys(c)
    time.sleep(.5)
time.sleep(3)

# click on the replay button
path_replay_btn = path_post + "div[1]/ul/ul[1]/div/li/div/div[1]/div[2]/div/div/button"
browser.find_element_by_xpath(xpath=path_replay_btn).click()
time.sleep(1)

# type the replay comment
path_replay_comment = path_post + "section[3]/div/form/"
for c in tags[:-1]:
    browser.find_element_by_xpath(xpath = path_replay_comment + "textarea").send_keys(c + " ")
    time.sleep(.5)
browser.find_element_by_xpath(xpath = path_replay_comment + "textarea").send_keys(tags[-1])
time.sleep(10)

# click on the popup button of the first comment
path_popup_btn = path_post + "div[1]/ul/ul[1]/div/li/div/div[2]/button"
browser.find_element_by_xpath(xpath = path_popup_btn).click()
time.sleep(2)

# click on the delete button of the popup
path_del = "/html/body/div[5]/div/div/div/button[2]"
browser.find_element_by_xpath(xpath = path_del).click()
time.sleep(2)


browser.delete_all_cookies()
browser.quit() 