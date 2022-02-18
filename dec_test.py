import rsa

privKey = rsa.PrivateKey.load_pkcs1(open("Keys/privKey.pem", "rb").read())

dec_file = open("For_Aspen.txt", "rb").read()

print(rsa.decrypt(dec_file, privKey))