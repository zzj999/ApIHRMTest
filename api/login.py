class LoginApi:
    def __init__(self):
        self.verify_code_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 获取验证码
    def get_login_verify_code(self,session):
        return session.get(self.verify_code_url)

    # 登陆
    def login(self,session,username,password,verify_code):
        # 发送请求
        data = {
            "username":username,
            "password":password,
            "verify_code":verify_code,
        }
        return session.post(self.login_url,data=data)