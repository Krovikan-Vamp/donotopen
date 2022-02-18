import rsa

publicKey, privateKey = rsa.newkeys(2048)

with open("Keys/privKey.pem", "wb") as f:
   f.write(privateKey.save_pkcs1())
   f.close()
with open("Keys/pubKey.pem", "wb") as f:
   f.write(publicKey.save_pkcs1())
   f.close()

msg = input(f'What would you like to say?\n')

encMsg = rsa.encrypt(msg.encode(), publicKey)

with open('output.txt', 'wb') as f:
   f.write(encMsg)
   f.close()

print(encMsg)