import hashlib

# 密码加密
def hash_code(s, salt='wuyuchao'):
    h = hashlib.sha256()
    s = str(s) + salt
    h.update(s.encode())
    return h.hexdigest()

# print(hash_code('123'))