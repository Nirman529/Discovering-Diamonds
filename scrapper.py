from seleniumwire import webdriver
import requests
import json
import time
import sys
import os


def main(argv):

    print(argv)
    # Header required for receiving the file in the localhost
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'content-type': 'application/octet-stream'
    }

    # Create a new instance of the Chrome driver
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)

    # Go to the specified website
    # pass (argv --> video link) in the get method

    driver.get(
        argv[0]
        # 'https://v3601506.v360.in/vision360.html?d=11914-516259491&z=1&surl=https%3a%2f%2fv3601506.v360.in%2f'
    )

    time.sleep(20)
    # Access requests via the `requests` attribute
    count = 0
    urls = []
    folder=''

    for request in driver.requests:
        count = count + 1

        if request.response:
            # ----- startswith will fetch all the files with the file name and store them to urls
            if request.url.startswith("https://v3601506.v360.in/imaged/"):
                getUrl = request.url
                print("url : ", getUrl)
                urls.append(getUrl)

                start = 'https://v3601506.v360.in/imaged/'
                end = '/'
                folder = (getUrl.split(start))[1].split(end)[0]
                print(folder)
                
                
                # folder = 'tempDir'
                try:
                    # Create target Directory
                    os.mkdir(folder)
                    print("Directory " , folder ,  " Created ") 
                except FileExistsError:
                    print("Directory " , folder ,  " already exists")

    print("Total requests made:", count)
    print("Urls extracted:", urls)

    count = 0

    # Check in individual url for the contents of the json file
    for url in urls:
        json_result = []
        # Create file name for image file
        # path = 'C:\\Users\\Username\\Path\\To\\File'

        fileName = folder + '\\' + str(count) + '.json'

        # open a file with given name with overwrite method
        with open(fileName, 'w') as f:
            # append the obtained result to res
            json_result.append((requests.get(url, headers=headers)).json())

            # convert the json response to string to paste it to the file
            fileContent = json.dumps(json_result[0])

            # write the content of res[i] to the file
            f.write(fileContent)
            print('Saving content to ', fileName)

            # close the file
            print('length of file: ', len(json_result[0]))

        count = count + 1

    # After the program execution is complete the driver is cleared
    del driver.requests


if __name__ == "__main__":
    main(sys.argv[1:])
