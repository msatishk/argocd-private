from flask import Flask
app = Flask(__name__)

@app.route('/')
def msg():
    return 'Hello, World! Deployed using Argo CD!'

@app.route('/argocd')
def srgocd_msg():
    return 'ArgoCD is amazing!!!!!'

if __name__ == "__main__":
    app.run(host ='0.0.0.0')