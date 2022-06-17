import requests
import json

headers = {
    'X-Requested-With': 'XMLHttpRequest'
}

'''
    To do:
    --> Make the program dynamic
    --> Convert program to functional program
'''

res = []
url = ''
for i in range(0, 8):
    print("response {}:".format(i))

    # Create file name for image file
    fileName = str(i)+'.json'

    # open a file with given name with overwrite method
    f = open(fileName, 'w')

    # url for fetching image of i.json file from v360 site
    url = 'https://v3601506.v360.in/imaged/9366-497172313/' + \
        str(i) + '.json?version=1'

    # append the obtained result to res
    res.append((requests.get(url, headers=headers)).json())

    # convert the json response to string to paste it to the file
    fileContent = json.dumps(res[i])

    # write the content of res[i] to the file
    f.write(fileContent)
    print('Saving content to ', fileName)

    # close the file
    f.close()

    print('length of file: ', len(res[i]))
