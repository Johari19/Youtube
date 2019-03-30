from subprocess import call, DEVNULL
import subprocess
import time
import os
if __name__ == "__main__":
    print("DO NOT RUN THIS SCRIPT! IT DOES NOTHING")
    time.sleep(10)
else:


    def installModule():
        def install(name):
            subprocess.call(['pip', 'install', name], stderr=DEVNULL, stdout=DEVNULL)
        if __name__ == "wsinstalls":
            print("Installing requests modules...")
            install('requests')
            time.sleep(1)
            print("Installing beautifulsoup4 modules...")
            install("beautifulsoup4")
            time.sleep(1)
            print("Installed all modules!")
            print("Importing modules...")


            from requests import get
            from requests.exceptions import RequestException
            from contextlib import closing
            from bs4 import BeautifulSoup

            time.sleep(1)
            print("Imported all modules!")
        else:
            print("Installation process failed!")
            os.system('pause')


    def get_URL(url):

        try:
            with closing(get(url, stream=True, allow_redirects=False)) as resp:
                if responsetest(resp):
                    return resp.content
                else:
                    return None

        except RequestException as e:
            log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None


    def responsetest(resp):
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)


    def log_error(e):
        print(e)
