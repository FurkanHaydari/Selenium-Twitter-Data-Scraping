from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys




user= input("kullanıcı adınız:")
password = input("şifreniz:")
search=input("aranacak öğe:")
browser = webdriver.Firefox()

browser.get("https://twitter.com/i/flow/login")

time.sleep(3)

kullanıcı_adı = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")

kullanıcı_adı.send_keys(user)

time.sleep(3)

ileri = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span")

ileri.click()

time.sleep(3)

sifre = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input")

sifre.send_keys(password)

time.sleep(3)

son_giris = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")

son_giris.click()

time.sleep(3)

search_box=browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")

search_box.click()

time.sleep(3)

button=browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[1]")

search_box.send_keys(search)

search_box.send_keys(Keys.ENTER);

time.sleep(3)

latest =browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div")

latest.click()

time.sleep(3)

tweets = []

print("twitler çekiliyor..")

count=""

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    
    lastCount = lenOfPage
    elements = browser.find_elements_by_css_selector(".css-901oao.r-1fmj7o5.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")
    for element in elements:
        tweets.append(element.text)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(5)
    if lastCount == lenOfPage:
        match=True
        





time.sleep(5)

tweetCount = 1

with open("tweets.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("*******************************************\n")
        tweetCount += 1
    

time.sleep(5)
    
browser.close()
