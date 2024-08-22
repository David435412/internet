from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/v_d')
def v_d ():
    return render_template('ven_des.html')
@app.route('/empresas')
def empresas ():
    return render_template('empresas.html')
@app.route('/form')
def form ():
    return render_template('form.html')
if __name__=='__main__':
    app.run(debug = True)