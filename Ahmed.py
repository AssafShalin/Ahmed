import urllib.request
import json
import pythoncom
import sys, os
from win32com.shell import shell, shellcon

def main():
    sys.stdout.write('fetching random word...')
    sys.stdout.flush()
    randomWord = getRandomWord()
    print(randomWord)
    sys.stdout.write('googling word...')
    sys.stdout.flush()
    imageURL = fetchGoogleResults(randomWord)
    print('OK')
    sys.stdout.write('downloading image...')
    sys.stdout.flush()
    img = httpGETImage(imageURL)
    print('OK')
    sys.stdout.write('setting wallpaper...')
    sys.stdout.flush()
    setWindowsWallpaper(img)
    print('OK')


def getRandomWord() -> str:
    wordHTML = httpGET("http://coyotecult.com/tools/randomwordgenerator.php?numwords=1")
    startIndex = wordHTML.find("http://www.onelook.com/?w=")
    endIndex = wordHTML.find("&ls=a",startIndex)
    randomWord = wordHTML[startIndex + len("http://www.onelook.com/?w="):endIndex]
    return randomWord.strip()


def fetchGoogleResults(word) -> str:
    res = httpGET('http://ajax.googleapis.com/ajax/services/search/images?v=1.0&imgsz=xxlarge&q=' + word)
    decjson = json.loads(res)
    results = decjson['responseData']['results'];
    lastImage = results[0]['url']
    return lastImage

def convert2BMP(imgPath):
    im = Image.open(imgPath)

def saveImage(imageData,fileName):
    file = open('tmp/' + fileName,'w')
    file.write(imageData)

def httpGET(url) -> str:
    request = urllib.request.urlopen(url)
    responseBody = urllib.request.urlopen(url).read()
    return responseBody.decode()


def httpGETImage(url):
    if not os.path.exists(getPath() + '\\tmp\\'):
        os.mkdir('tmp')
    fileName = url.split('/')
    fileName = fileName[len(fileName)-1]
    urllib.request.urlretrieve(url,'tmp/' + fileName)

    return getPath() + '\\tmp\\' + fileName

def setWindowsWallpaper(imgPath):

    iad = pythoncom.CoCreateInstance(shell.CLSID_ActiveDesktop, None,
          pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IActiveDesktop)
    iad.SetWallpaper(imgPath, 0)
    iad.ApplyChanges(shellcon.AD_APPLY_ALL)

def getPath():
    return os.path.abspath(os.path.dirname(sys.argv[0]))
if __name__ == '__main__':
    main()