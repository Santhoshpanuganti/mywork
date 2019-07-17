from flask import *
from hstl.database.models import Personal_info,Login_credentials
from hstl.database.db import session
from flask_bcrypt import Bcrypt
from datetime import timedelta
from flask_login import LoginManager,login_required,login_user,logout_user
# import time
# from hstl.forms import Registration
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'pe'
@app.route('/',methods = ['GET','POST'])
def l_form():
    form = request.form
    if request.method == 'POST':
        name = form.get('name')
        password = form.get('password')
        h_password = bcrypt.generate_password_hash(password)
        record_count = session.query(Login_credentials).count()
        if not record_count == 0:
            record = session.query(Login_credentials).first()
            if record.username == name and bcrypt.check_password_hash(record.password,password):
                return redirect(url_for('r_form'))
            else:
                return '<h1>Invalid credentials</h1>'
        elif record_count == 0:
            session.add(Login_credentials(username = name , password = h_password))
            session.commit()
            return "<h1>Admin Registered<h1>"
    return render_template('loginbootstrap.html',form = form)

@app.route('/form',methods = ['GET','POST'])
def r_form():
    form = request.form
    if request.method == 'POST':
        newfirst_name = form.get('newfirst_name')
        newDOB = form['newDOB']
        newoccupation = form['newoccupation']
        newid_proof = form['newid_proof']
        newid_proof_no = form['newid_proof_no']
        newHno = form['newHno']
        newVillage = form['newVillage']
        newlandmark = form['newlandmark']
        newstreet = form['newstreet']
        newdistrict = form['newdistrict']
        newpincode = form['newpincode']
        newMobileno = form['newMobileno']
        count = session.query(Personal_info).filter(Personal_info.id_proof_no == newid_proof_no).count()
        if count == 0:
            session.add(Personal_info(first_name = newfirst_name,DOB = newDOB,occupation = newoccupation,
                                      id_proof = newid_proof,id_proof_no = newid_proof_no,h_no = newHno,
                                      village = newVillage,landmark = newlandmark,street = newstreet,district = newdistrict,pincode = newpincode,mobileno = newMobileno ))
            session.commit()
            return '<h1>Registered sucssesfully</h1>'
        else:
            return '<p>existed already</p>'
    return render_template('registerbootstrap.html', form=form)

@app.route('/get_details/<id_no>')
def get_details(id_no):
    exist = session.query(Personal_info).filter(Personal_info.id_proof_no == id_no).count()
    if not exist == 0:
        records = session.query(Personal_info).filter(Personal_info.id_proof_no == id_no).first()
        return render_template('bio_data.html',data = records)
    else:
        return '<h1> Enter valid Id no</h1>'


if __name__ == '__main__':
    app.run(debug=True)

