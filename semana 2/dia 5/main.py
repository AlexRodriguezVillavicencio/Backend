from flask import Flask,render_template,request

app = Flask(__name__)

lstproductos = ['LAPTOP', 'IMPRESORA HP', 'SILLA GAMER']

@app.route('/')
def index():
    name = request.args.get('n','no puso su nombre')
    user_ip = request.remote_addr


    context = {
        'name':name,
        'user_ip':user_ip,
        'productos':lstproductos
    }

    return render_template('index.html', **context )



@app.route('/productos')
def productos():

    context = {
        'productos': lstproductos
    }
    
    return render_template('productos.html', **context)



if __name__ == '__main__':
    app.run(debug=True,port=5000)