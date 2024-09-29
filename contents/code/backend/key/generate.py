import rsa


(public_key, private_key) = rsa.newkeys(512)


with open('public.pem', 'wb') as pfile:
    pfile.write(public_key.save_pkcs1('PEM'))

with open('private.pem', 'wb') as pfile:
    pfile.write(private_key.save_pkcs1('PEM'))
# Kiến thức mật mã
# Mã hóa thông tin
# Thuật toán RSA
