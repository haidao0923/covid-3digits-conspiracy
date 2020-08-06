# Import selenium webdriver for web scraping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# incognito window
chrome_options.add_argument("--incognito")
# open chrome browser
browser = webdriver.Chrome(chrome_options = chrome_options)
# go to website
browser.get('https://www.google.com')

# open csv file ('a' = append mode; 'w' = write mode)
filename = 'covidReport.csv'
f = open(filename, 'w')

#LOOP
for i in range(100, 201):
    search = browser.find_element_by_name('q')
    search.send_keys(Keys.CONTROL + 'a' + Keys.DELETE) #backspace
    search_text = '"' + str(i) + '" new cases georgia'
    search.send_keys(search_text)
    search.send_keys(Keys.ENTER) # hit return after you enter search text
    f.write('Searched: ' + search_text + '\n')
    search_page = browser.find_element_by_css_selector('#rso')
    results = search_page.find_elements_by_class_name('g')
    print(len(results))
    for i in range(len(results)):
        name = ascii(results[i].find_element_by_xpath(".//div[1]//div[1]//a[1]//h3[1]").text)
        if len(name) > 5:
            f.write(name.replace(',','|') + '\n')
    f.write('\n')
    
# close file    
f.close()

# wait to close browser
a = input()
# close browser
browser.quit()
