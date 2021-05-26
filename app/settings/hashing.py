from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes = ['bcrypt'], deprecated = "auto")

class Hash():
    
    def bcrypt(self,password : str):
        return pwd_ctx.hash(password)

    def verify(self,hashed_password, plain_password):
        return pwd_ctx.verify(plain_password, hashed_password)