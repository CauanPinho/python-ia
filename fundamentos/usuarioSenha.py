usuario=input("Digite o seu usuario:")

senha=input("Digite a sua senha:")

login_valido = usuario == "admin" and senha == "123456"


print(f"Login permitido? {login_valido}")