from flask import Flask, session, redirect, render_template, request

app = Flask(__name__)
app.secret_key = b'1234567890123456789012345678901234567890123456789012345678234567823453456345672354563425678432qr45790[]243567890-0243567=rwqetwioypuowafdgsfgnmh,jk.j34y5u6tulibgvndrkngwerhijijijijijijijij'

@app.route('/')

def index():
	if 'color' not in session:
		session['color'] = 'white'

	return render_template('index.html', color = session['color'])

@app.route('/set')
def set_color():
	color = request.args.get('color', None)

	if color == 'r':
		session['color'] = 'red'

	elif color == 'g':
		session['color'] = 'green'

	elif color == 'b':
		session['color'] = 'blue'

	return redirect('/')


app.run(debug = True)