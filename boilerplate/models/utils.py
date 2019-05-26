import hashlib
import os

def md5(s):
    to_hash = (os.environ['DB_NAME'] + str(s)).encode()
    return haslib.md5(to_hash).hexidigest()
