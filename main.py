import re
import os
import smtplib
import time
import imghdr
from email.message import EmailMessage

# spams emails every 45 seconds

# returns the image name for each email count
# loops through the 5 images
def getImageName(countMail):
    imgNum = countMail%5
    imageName = 'image' + str(imgNum)+'.jpg'
    return imageName


# setting all variables
fromEmail = 'your.email@gmail.com' # your email id
pwd = 'password' # put your password
toEmail = 'recipient.email@email.com' # email id of recipient

message = EmailMessage()

# counts the number of emails sent 
countMail = 0


#openin text file and getting each sentence using regex
text = open("text.txt", "r", errors='ignore')
doclist = [ line for line in text ]
docstr = '' . join(doclist)
sentences = re.split(r'[.]', docstr)
countSentences = len(sentences)

# closing file
text.close()

print(countSentences)

#connecting with smtp
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 

    message['From'] = fromEmail
    message['To'] = toEmail
    
    # logging in 
    smtp.login(fromEmail,pwd)

    #looping through each sentence in the text file
    for sentence in sentences:

        # subject of the message is the sentence from the text file
        message['Subject'] = sentence

        #content of all emails is this ->
        message.set_content('Enjoy this email :)')  # can set this to anything

        print('Sending mail ', countMail+1)
        
        # getting image name based on the number of the current email being sent
        imageName = getImageName(countMail)

        # opening image in ReadBytes mode
        with open('images/'+imageName,'rb') as img: 
            fileData = img.read()
            fileType = imghdr.what(img.name)
            fileName = img.name.split('/')[1]
        
        # attaching the image to the message
        message.add_attachment(fileData, maintype= 'image', subtype= fileType, filename= fileName)
    
        # sending message and clearing its content after being sent 
        smtp.send_message(message)
        message.clear_content()
    
        print('Sent succesfully! ', countMail+1)    
        
        # continue as long as the text isnt over
        if countMail != countSentences:
            # wait for 45 secs to send the next one
            time.sleep(45) 
            countMail+=1
            del message['Subject']  # deletes the old subject line so that in the next loop, the new subject can be added
            
        # all sentences in the text file have been sent
        else: 
            print('Completed Run Successfully!')






