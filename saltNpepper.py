"""
SaltNPeppering
@autor: @roopesh90
Logs:
-v1.0: get value, make hashable string, obscure string, check string and hash integrity
-v1.0.1: Long integer sample mage int, python3 compatibility issues
"""
import os, sys, hashlib

class SaltNPeppering(object):
    def __init__(self):
        self.PARAM1 = "salt"
        self.PARAM2 = "pepper"
        self.HASHER = "ripemd160"

    def make_input(self, value):
        val = "%s_%s_%s" % (self.PARAM1, value, self.PARAM2)
        return bytearray(val, 'utf-8')

    def obscurify(self, value):
        val = self.make_input(value)
        h = hashlib.new(self.HASHER)
        h.update(val)
        hash1 = h.hexdigest()[:20]
        return hash1

    def check_integrity(self, value, hash):
        h_digest = self.obscurify(value)
        return (h_digest==hash)

if __name__ == '__main__':
    for arg in range(0,len(sys.argv)):
        SaltNPeppering1 = SaltNPeppering()
        if arg == 1:
            arg1 = sys.argv[arg]
            arg1 = long(arg1)
            print(SaltNPeppering1.obscurify(arg1))
            break
        else:
            print(SaltNPeppering1.obscurify(1))
            print(len(SaltNPeppering1.obscurify(1)))
            print(SaltNPeppering1.check_integrity(1, "27a04b2c5496935c5ec7"))
            #break
