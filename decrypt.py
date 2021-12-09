from cryptography.fernet import Fernet


key = " " #key generated from "Generate key" program

file_to_decrypt = " " #name of the file to be decrypted

filepath = " " path of the file


decrypted_files = [filepath + file_to_decrypt]
count = 0

for decrypting_file in decrypted_files:
    with open(decrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(decrypted_files[count], 'wb') as f:
        f.write(decrypted)

    count += 1 #for multiple files
