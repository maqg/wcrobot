#!/usr/bin/python
# -*- coding: utf-8 -*-

from base64 import b64encode, b64decode

RC4_Key = "octopuslink!"


def gen_random_bytes(k):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + k[i]) % 256
        k[i], k[j] = k[j], k[i]
        yield k[(k[i] + k[j]) % 256]


def rc4_crypt(data, key):
    S = list(range(256))
    j = 0
    out = []

    # Algoritmo pseudo aleatorio
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # Algoritmo de 1 clave
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    return ''.join(out)


def encrypt(data, key, encode=False):
    data = rc4_crypt(data, key)
    if encode:
        # b64encode para is bytes.
        data = b64encode(data.encode(encoding="utf-8"))

    # turn data(bytes) to str
    return data.decode()


def decrypt(data, key, decode=False):
    if decode:
        # b64decode para is bytes.
        data = b64decode(data.encode(encoding="utf-8"))

    # data type is <class 'bytes'>, need turn to str using decode, or rc4_crypt char is <class 'int'>.
    # then, TypeError: ord() expected string of length 1, but int found
    return rc4_crypt(data.decode(), key)


def getCipherPassword(password, source="client"):
    newText = source + "#" + password
    return encrypt(newText, RC4_Key, encode=True)


def getPlainPassword(password):
    outText = decrypt(password, RC4_Key, decode=True)
    return outText.split("#")[-1]

def decrypt_temp(data, decode=False):
    if decode:
        # b64decode para is bytes.
        data = b64decode(data.encode(encoding="utf-8"))

    return data.decode()

def getPlainPassword_temp(password):
    outText = decrypt_temp(password, decode=True)
    return outText.split("#")[-1]

if __name__ == "__main__":
    x = getCipherPassword("nihao")
    print(x)
    y = getPlainPassword(x)
    print(y)
