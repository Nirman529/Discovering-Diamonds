from seleniumwire import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json
import time
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def main():

    argv = input("Enter url: ")
    turl = argv
    html = urlopen(turl).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find('iframe')
    gotourl = tags.get('src')

    # print(gotourl)
    # Header required for receiving the file in the localhost
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'content-type': 'application/octet-stream'
        # 'content-type': 'text/html'
    }

    # Create a new instance of the Chrome driver
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)

    # Go to the specified website
    # pass (argv --> video link) in the get method

    driver.get(
        gotourl
        # 'https://v3601506.v360.in/vision360.html?d=11914-516259491&z=1&surl=https%3a%2f%2fv3601506.v360.in%2f'
    )

    time.sleep(20)
    # Access requests via the `requests` attribute
    count = 0
    urls = []
    folder = ''

    for request in driver.requests:
        count = count + 1

        if request.response:
            # ----- startswith will fetch all the files with the file name and store them to urls
            if request.url.startswith("https://v3601506.v360.in/imaged/"):

                getUrl = request.url
                # print("url : ", getUrl)
                urls.append(getUrl)

                start = 'https://v3601506.v360.in/imaged/'
                end = '/'
                folder = (getUrl.split(start))[1].split(end)[0]
                # print(folder)

                # folder = 'tempDir'
                # folder = "../"+folder
                try:
                    # Create target Directory
                    os.mkdir(folder)
                    # print("Directory ", folder,  " Created ")
                except FileExistsError:
                    print()
                    # print("Directory ", folder,  " already exists")

                    # print("Total requests made:", count)
                    # print("Urls extracted:", urls)

    count = 0

    # Check in individual url for the contents of the json file
    json_result = []
    for url in urls:
        # Create file name for image file
        # path = 'C:\\Users\\Username\\Path\\To\\File'

        fileName = folder + '\\' + str(count) + '.json'

        # open a file with given name with overwrite method
        with open(fileName, 'w') as f:
            # append the obtained result to res
            json_result.append((requests.get(url, headers=headers)).json())

            # convert the json response to string to paste it to the file
            fileContent = json.dumps(json_result[count])

            # write the content of res[i] to the file
            f.write(fileContent)
            # print('Saving content to ', fileName)

            # close the file
            # print('length of file: ', len(json_result[count]))

        f.close()
        count = count + 1

    # After the program execution is complete the driver is cleared
    del driver.requests
    print("Done execution")


if __name__ == "__main__":
    main()
