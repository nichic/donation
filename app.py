from flask import *
from persistence import *

app = Flask(__name__)

@app.route('/Donor', methods=['GET', 'POST'])
def donor():
    if request.method == "POST":

        item = request.form['Item']
        expiry = request.form['Expiry']
        quantity = request.form ['Quantity']
        req = request.form ['Req']
        email = 'email'
        donor = Donor(item, expiry, quantity, req, email)
        create_donor(donor)
        return render_template('DonorSubmit.html', donor=donor)
    return render_template('Donor.html')


@app.route('/DonorSubmit')
def DonorSubmit():
    return render_template('DonorSubmit.html')

@app.route('/userprofile')
def userprofile():
    return render_template('userprofile.html')

if __name__ == '__main__':
    app.run(debug=True)
