from selenium import webdriver
import time

pin = input('Enter the Empty Pinned Group Name : ')
cycle = int(input('Enter the time interval(in seconds) to check for Messages : '))
username = 'unknown'

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

print('Scan and Wait for 30 seconds')
time.sleep(30)

print('Program Started')
box = driver.find_elements_by_xpath("//div[@class='_3j7s9']")

#Clicking the initial chat box
for k in range (0,len(box)):
    top = driver.find_elements_by_xpath("//div[@class='_2FBdJ']")
    name = top[k].find_element_by_class_name('_25Ooe')
    if(name.text == pin):
        pinnedMessage = name
        pinnedMessage.click()
        
        # UNCOMMENT THESE LINES TO SPAM A FRIEND ;)
        #Enter your Friends Name displayed in your Chat in the place of Pinned Message

        # for i in range(0,100):
        #     messageBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        #     messageBox.send_keys('SPAM MESSAGE HERE')

        #     sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
        #     sendButton.click()


for j in range (0,1000):
    box = driver.find_elements_by_xpath("//div[@class='_3j7s9']")
    print(len(box))
    for i in range(0, len(box)):
        top = box[i].find_elements_by_xpath("//div[@class='_2FBdJ']")
        name = top[i].find_element_by_class_name('_25Ooe')
        username = name.text
        print(f'Username : {username}')

        #Checking whether the user received a Message or Not
        try:
            bottom = box[i].find_elements_by_xpath("//div[@class='_1AwDx']")
            new = bottom[i].find_element_by_class_name('OUeyt')

            #Checking whether the chat is Group or a individual User (Muted Chats)
            try:
                group = bottom[i].find_element_by_tag_name('svg')
                print(f'{username} : Group')

            #Sending the message if it is not a Group
            except:
                print(f'{username} : Not a Group')
                name.click()

                messageBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                messageBox.send_keys('Hey guys. This is an automated message sent from a Python Script. I am replying to all the reveived messages when i am busy Playing Games or Studying. Will reply to you people shortly :)')

                sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
                sendButton.click()

        except:
            print(f'No Message')

        print('****************************************************')

    pinnedMessage.click()
    print('Next Cycle')
    time.sleep(cycle)
