import base64

def str_xor(a, b):
    return "{0:0{1}x}".format(int(a,16) ^ int(b,16), len(a))

res = str_xor('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965')

print(res)
