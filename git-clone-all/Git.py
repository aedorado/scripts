import os
import shutil

class Git:

    @staticmethod
    def clone(url):
        repo = url[url.rfind('/') + 1: ]
        if os.path.exists(repo):
            shutil.rmtree(repo)
        os.system('git clone ' + url)