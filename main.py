import webbrowser
import sys

url = 'http://docs.python.org/'

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

print(sys.argv[1:])

webbrowser.get(chrome_path).open(url)