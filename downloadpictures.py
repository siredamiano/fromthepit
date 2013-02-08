import errno
import os
import urllib

def require_dir(path):
    try:
        os.makedirs(path)
    except OSError, exc:
        if exc.errno != errno.EEXIST:
            raise

directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
require_dir(directory)
filename = os.path.join(directory, "5b39a23a69dc11e2bdc622000a1fb844_7.jpg")

if not os.path.exists(filename):
    urllib.urlretrieve("http://distilleryimage3.s3.amazonaws.com/5b39a23a69dc11e2bdc622000a1fb844_7.jpg", filename)
