#!/usr/bin/python
# coding:utf-8

# tools - demo.py
# 2018/5/28 13:41
# 

__author__ = 'Benny <benny@bennythink.com>'

import hashlib
from base64 import b64encode, b64decode
from binascii import hexlify

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def get_aes_key(plaintext):
    """
    get aes key.
    :param plaintext: str, user's login password
    :return:bytes, just for key.
    """
    m = hashlib.sha256()
    m.update(plaintext.encode('utf-8'))
    return m.digest()


def hash_filename(name):
    """
    get hash filename
    :param name: str filename: test.txt
    :return: str, 64 characters.
    """
    m = hashlib.sha256()
    m.update(name.encode('utf-8'))
    return hexlify(m.digest()).decode('utf-8')


def aes(_type, iv, password, raw, cook):
    key = get_aes_key(password)
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())

    if _type == 'encrypt':
        encryptor = cipher.encryptor()
        f_raw = open(raw, 'r', encoding='utf-8')
        raw_bytes = f_raw.read().encode('utf-8')

        ct = encryptor.update(raw_bytes) + encryptor.finalize()
        f_cook = open(cook, 'w', encoding='utf-8')
        f_cook.write(b64encode(ct).decode('utf-8'))

        f_raw.close()
        f_cook.close()

    elif _type == 'decrypt':
        decryptor = cipher.decryptor()
        f_cook = open(cook, 'r', encoding='utf-8')
        raw_bytes = b64decode(f_cook.read())

        plaintext = decryptor.update(raw_bytes) + decryptor.finalize()
        # TODO: filename in hash
        f = open(hash_filename(cook.split('.')[0]) + '.' + cook.split('.')[1], 'w', encoding='utf-8')
        f.write(plaintext.decode('utf-8'))
        f.close()


if __name__ == '__main__':
    aes('encrypt', b'asdfghjklpoiuytr', '123456', 'raw.txt', 'cook.txt')
    aes('decrypt', b'asdfghjklpoiuytr', '123456', 'raw.txt', 'cook.txt')
