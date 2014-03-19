import urllib2, cookielib
from lxml import html
import datetime

url = 'https://www.myicomfort.com/Dashboard.aspx'
txheaders =  {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

cj = cookielib.MozillaCookieJar('C:\Users\jerome.avondo\Desktop\lennox\cookie.txt')
cj.load() 

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

req  = urllib2.Request(url, None, txheaders)
response = urllib2.urlopen(req )
page = html.fromstring(response.read())
response.close()

status = page.xpath( '(//span[@id="RightContent_zoneName1_Status"]/text())' )[0]
temp = page.xpath( '(//span[@id="RightContent_zoneName1_Current_Temp"]/text())' )[0]
coolheat = page.xpath( '(//input[@name="ctl00$RightContent$hidden_SetPoints"])' )[0].attrib['value']
cool = coolheat.split('|')[0]
heat = coolheat.split('|')[1]

humid = page.xpath( '(//span[@id="LeftContent_home_current_humidity"]/text())' )[0]
update = page.xpath( '(//span[@id="LeftContent_last_updated_Home"]/text())' )[0]

print("Updated: " + str(update))
print("Status: " + str(status))
print("Temp: " + str(temp) + " humidity " + str(humid) + "%")
print("Heat to: " + str(heat) + " Cool to: " + str(cool))

dt = datetime.datetime.now().strftime("%Y, %m, %d, %H, %M")

myFile = open('C:\Users\jerome.avondo\Desktop\lennox\data.txt', 'a')
myFile.write(dt + ", " + str(temp) + ", " + str(humid) + ", " + str(heat) + ", " + str(cool) + ", " + str(status) + "\n")	
myFile.close()

