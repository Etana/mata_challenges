import base64

chaine = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

def hex_to_b64(hex_str):
    return str(base64.b64encode(base64.b16decode(hex_str.upper())),'ascii')

print(hex_to_b64(chaine))
