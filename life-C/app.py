from flask import Flask, render_template, request, jsonify
from life import seconds, minutes, hours, days

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    dob = request.form['dob']
    years = request.form['years']
    measure = request.form['measure']
    try:
        if measure == 'seconds':
            re = seconds(dob, years)
            result = f"If your life expectency is {years} years then only {re[1]} seconds are left in your life, because you have already passed {re[0]} seconds from your life."
        elif measure == 'minutes':
            re = minutes(dob, years)
            result = f"If your life expectency is {years} years then only {re[1]} minutes are left in your life, because you have already passed {re[0]} minutes from your life."
        elif measure == 'hours':
            re = hours(dob, years)
            result = f"If your life expectency is {years} years then only {re[1]} hours are left in your life, because you have already passed {re[0]} hours from your life."
        elif measure == 'days':
            re = days(dob, years)
            result = f"If your life expectency is {years} years then only {re[1]} days are left in your life, because you have already passed {re[0]} days from your life."
        else:
            return jsonify({'result':'Invalid Input'}) 
        return jsonify({'result':result})
    except ValueError and SystemExit:
        return jsonify({'result':'Invalid Input'})    
    
    
if __name__ == '__main__':
    app.run(debug=True)
