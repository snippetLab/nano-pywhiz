email = str(input("Enter email : ")).strip();
username = email[:email.index("@")];
domain_name = email[email.index("@")+1:];

print(f"The username : {username}\nDomain Name : {domain_name}");
