from traceback import print_tb
from seleniumwire import webdriver
from seleniumwire.utils import decode
import requests
import json
import time
import sys


def main(argv):

    print(argv)
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'content-type': 'application/octet-stream'
    }

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(
        "C:/Users/Nirman/AppData/Local/Programs/Python/Python37/chromedriver.exe")

    # Go to the specified website
    # pass (argv --> video link) in the get method

    driver.get(
        'https://v3601506.v360.in/vision360.html?d=11914-516259491&z=1&surl=https%3a%2f%2fv3601506.v360.in%2f'
    )

    time.sleep(20)
    # Access requests via the `requests` attribute
    count = 0
    urls = []

    for request in driver.requests:
        count = count + 1
        if request.response:
            # startswith will fetch all the files with the file name

            if request.url.startswith("https://v3601506.v360.in/imaged/"):
                print("url : ", request.url)
                urls.append(request.url)

    print("Total requests made:", count)
    print("Urls extracted:", urls)

    count = 0
    json_result = []

    for url in urls:
        # Create file name for image file
        fileName = str(count)+'.json'

        # open a file with given name with overwrite method
        f = open(fileName, 'w')

        # append the obtained result to res
        json_result.append((requests.get(url, headers=headers)).json())

        # convert the json response to string to paste it to the file
        fileContent = json.dumps(json_result[count])

        # write the content of res[i] to the file
        f.write(fileContent)
        print('Saving content to ', fileName)

        # close the file
        f.close()
        print('length of file: ', len(json_result[count]))

        count = count + 1


if __name__ == "__main__":
    main(sys.argv[2:])
