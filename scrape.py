from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# From "https://v360.in/movie/1506_9366-497172313" kind of links the
# iframes will be grabbed------------------------------------------------done
#
# The iframe src link will be open in new tab
# From
#
#

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://v360.in/movie/1506_9366-497172313"
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

iframes = soup.find_all('iframe')

# print(soup.find_all('iframe'))
print(iframes[0]['src'])
