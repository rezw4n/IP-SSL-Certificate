import os

os.system("openssl genrsa -aes256 -out ca-key.pem 4096")
os.system("openssl req -new -x509 -sha256 -days 3650 -key ca-key.pem -out ca.pem")
os.system("openssl genrsa -out cert-key.pem 4096")

CN = input("Please enter your Certificate Authority Name: ")
IP = input("Enter the local IP for which you want to enable SSL: ")
organization = input("Enter the name of your organization: ")
organization_unit = input("Enter the name of your organization unit: ")

os.system(f'openssl req -new -sha256 -subj "/CN={CN}/O={organization}/OU={organization_unit}" -key cert-key.pem -out cert.csr')

with open('extfile.cnf', 'w') as f:
    f.write(f"subjectAltName=IP:{IP}")

os.system("openssl x509 -req -sha256 -days 3650 -in cert.csr -CA ca.pem -CAkey ca-key.pem -out cert.pem -extfile extfile.cnf -CAcreateserial")
os.system("openssl verify -CAfile ca.pem -verbose cert.pem")

os.system('powershell Import-Certificate -FilePath ".\ca.pem" -CertStoreLocation Cert:\LocalMachine\Root')
