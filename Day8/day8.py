alp= ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def encrypt(plain_text, sh):
    ciphertext=""
    for i in plain_text:
        position= alp.index(i)
        newposition= position+sh
        newletter= alp[newposition]
        ciphertext+=newletter
    print(f"the encoded text is {ciphertext}")



def decrypt(plain_text, sh):
    ciphertext=""
    for i in plain_text:
        position= alp.index(i)
        newposition= position-sh
        newletter= alp[newposition]
        ciphertext+=newletter
    print(f"the decoded text is {ciphertext}")

direction= input('type "encode" to encrypt and "decode" to decrypt: ').lower()
text= input("enter your message: ").lower()
shift= int(input("enter the shift number: "))


if direction == "encode":
    encrypt(plain_text=text, sh=shift)

elif direction == "decode":
    decrypt(plain_text=text, sh=shift)

else:
    print("type the correct word")