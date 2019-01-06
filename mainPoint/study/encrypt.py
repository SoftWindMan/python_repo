#coding=utf-8
import hashlib

testStr = 'HelloWorld'

md5 = hashlib.md5()
md5.update(testStr.encode('utf-8'))
md5_res = md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update(testStr.encode('utf-8'))
sha1_res = sha1.hexdigest()

sha256 = hashlib.sha256()
sha256.update(testStr.encode('utf-8'))
sha256_res = sha256.hexdigest()

sha384 = hashlib.sha384()
sha384.update(testStr.encode('utf-8'))
sha384_res = sha384.hexdigest()

sha512 = hashlib.sha512()
sha512.update(testStr.encode('utf-8'))
sha512_res = sha512.hexdigest()

print('md5    - {}'.format(md5_res))
print('sha1   - {}'.format(sha1_res))
print('sha256 - {}'.format(sha256_res))
print('sha384 - {}'.format(sha384_res))
print('sha512 - {}'.format(sha512_res))

