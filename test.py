import datetime
import time

from Blowfish import Blowfish
from DES import DES
from TRIPLEDES import TripleDES
from MAGMA import MAGMA

def test_blowfish(key, text):
    print("BLOWFISH TEST\n-------------------")
    start = datetime.datetime.now()
    p_start = start
    cipher = Blowfish(key)

    res = cipher.encrypt(text)
    print("ENCRYPTED TEXT IS:\n", res)
    end = datetime.datetime.now()
    print("ENCRYPTED IN", end - start)
    print()

    start = datetime.datetime.now()
    cipher = Blowfish(key)
    res2 = cipher.decrypt(res)
    print("DECRYPTED TEXT IS:", res2)
    end = datetime.datetime.now()
    print("DECRYPTED IN", end - start)
    print()

    print("TOTALLY TIME SPENT:", end - p_start)
    print()

    return end - p_start

def test_des(key, text):
    print("DES TEST\n-------------------")
    start = datetime.datetime.now()
    p_start = start
    cipher = DES(key)

    res = cipher.encrypt(text)
    print("ENCRYPTED TEXT IS:\n", res)
    end = datetime.datetime.now()
    print("ENCRYPTED IN", end - start)
    print()

    start = datetime.datetime.now()
    cipher = DES(key)
    res2 = cipher.decrypt(res)
    print("DECRYPTED TEXT IS:", res2)
    end = datetime.datetime.now()
    print("DECRYPTED IN", end - start)
    print()

    print("TOTALLY TIME SPENT:", end - p_start)
    print()

    return end - p_start

def test_tdes(key, text):
    print("3DES TEST\n-------------------")
    start = datetime.datetime.now()
    p_start = start
    cipher = TripleDES(key)

    res = cipher.encrypt(text)
    print("ENCRYPTED TEXT IS:\n", res)
    end = datetime.datetime.now()
    print("ENCRYPTED IN", end - start)
    print()

    start = datetime.datetime.now()
    cipher = TripleDES(key)
    res2 = cipher.decrypt(res)
    print("DECRYPTED TEXT IS:", res2)
    end = datetime.datetime.now()
    print("DECRYPTED IN", end - start)
    print()

    print("TOTALLY TIME SPENT:", end - p_start)
    print()

    return end - p_start

def test_magma(key, text):
    print("MAGMA TEST\n-------------------")
    start = datetime.datetime.now()
    p_start = start
    cipher = MAGMA(key)

    res = cipher.encrypt(text)
    print("ENCRYPTED TEXT IS:\n", res)
    end = datetime.datetime.now()
    print("ENCRYPTED IN", end - start)
    print()

    start = datetime.datetime.now()
    cipher = MAGMA(key)

    res2 = cipher.decrypt(res)
    print("DECRYPTED TEXT IS:", res2)
    end = datetime.datetime.now()
    print("DECRYPTED IN", end - start)
    print()

    print("TOTALLY TIME SPENT:", end - p_start)
    print()

    return end - p_start

def main():

    key = "supersecretkeyformytests"

    start_text = "Lorem ipsum dolor sit amet," \
                 " consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
                 "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. " \
                 "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. " \
                 "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


    time_blowifsh = test_blowfish(key, start_text)
    time_des = test_des(key, start_text)
    time_tdes = test_tdes(key, start_text)
    time_magma = test_magma(key, start_text)

    print("BLOWFISH:", time_blowifsh)
    print("DES:", time_des)
    print("Triple DES:", time_tdes)
    print("MAGMA:", time_magma)

if __name__ == '__main__':
    main()

