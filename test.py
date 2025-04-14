from flask import Flask, request, render_template_string, redirect, url_for
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import hashlib
import base64

app = Flask(__name__)

# 模拟数据库存储用户信息
users = {}

def generate_weak_rsa_key():
    """生成存在ROCA漏洞的弱RSA密钥对（示例用简化版）"""
    # 注意：此处使用小素数简化演示，真实场景应符合CVE具体参数
    p = 104438888141315250667960271984652954583126906099213502902444003793690376390551  # 示例弱素数
    q = 104438888141315250667960271984652954583126906099213502902444003793690376390553  # 示例弱素数
    n = p * q
    e = 65537
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    return RSA.construct((n, e, d))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users:
            return "用户已存在！"
        
        # 生成弱RSA密钥对
        key = generate_weak_rsa_key()
        users[username] = {
            'pass_hash': hashlib.sha256(password.encode()).hexdigest(),
            'pub_key': key.publickey().export_key(),
            'priv_key': key.export_key()
        }
        return "注册成功！"
    
    return render_template_string('''
        <form method="post">
            <input type="text" name="username" placeholder="用户名" required><br>
            <input type="password" name="password" placeholder="密码" required><br>
            <input type="submit" value="注册">
        </form>
    ''')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        encrypted = request.form['encrypted']
        
        if username not in users:
            return "用户不存在！"
        
        user = users[username]
        try:
            # RSA解密
            cipher = PKCS1_OAEP.new(RSA.import_key(user['priv_key']), hashAlgo=SHA256)
            password = cipher.decrypt(base64.b64decode(encrypted)).decode()
        except:
            return "解密失败！"
        
        if hashlib.sha256(password.encode()).hexdigest() == user['pass_hash']:
            return "登录成功！"
        return "密码错误！"
    
    return render_template_string('''
        <form method="post">
            <input type="text" name="username" placeholder="用户名" required><br>
            <input type="text" name="encrypted" placeholder="加密密码" required><br>
            <input type="submit" value="登录">
        </form>
    ''')

@app.route('/pubkey/<username>')
def get_pubkey(username):
    if username in users:
        return users[username]['pub_key'].decode()
    return "用户不存在！"

if __name__ == '__main__':
    app.run(port=5000, debug=True)