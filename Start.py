from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = r"D:\Program\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

class ClassItem:
    def __init__(self, name, url):
        self.name = name
        self.url = url
    def __str__(self):
        return self.name + " " + self.url

AllItems = []
while True:    
    i = 1
    driver.get("http://www.wowhead.com/recipe-items/type:6:4:5:8:3:11:10:1:12:2?filter=2:128;2:7;0:0#" + str(i * 50) + "-2")
    content = driver.find_element_by_xpath("//div[@class='q1 listview-cleartext']")
    for  j in content:
        AllItems.append(j.text, j.url)
    i += 1
    break
for Item in AllItems:
    print(Item)