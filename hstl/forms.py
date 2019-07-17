# from flask_wtf import FlaskForm
# from wtforms import StringField,SubmitField,DateField,IntegerField,PasswordField,validators,TextField
#
#
# class Registration(FlaskForm):
#     newfirst_name = StringField('FirstName',validators=[validators.DataRequired()])
#     newlast_name = StringField('LastName',validators=[validators.DataRequired()])
#     newDOB = DateField('DOB',validators=[validators.DataRequired()],format='%Y-%m-%d')
#     newoccupation = StringField('Occupation',validators=[validators.DataRequired()])
#     newid_proof = StringField('Id_proof',validators=[validators.DataRequired()])
#     newid_proof_no = IntegerField('Id_proof_No',validators=[validators.DataRequired()])
#     newHno = StringField('H_No',validators=[validators.DataRequired()])
#     newVillage = StringField('Village',validators=[validators.DataRequired()])
#     newlandmark = StringField('LandMark',validators=[validators.DataRequired()])
#     newstreet = StringField('Street',validators=[validators.DataRequired()])
#     newdistrict = StringField('District',validators=[validators.DataRequired()])
#     newpincode = IntegerField('Pincode',validators=[validators.DataRequired()])
#     newMobileno = IntegerField('MobileNo',validators=[validators.DataRequired()])
#     submit = SubmitField('Sign Up')
#
# class Login(FlaskForm):
#     name = TextField('Name',validators=[validators.InputRequired(),validators.length(max=100)])
#     password = PasswordField('Password',validators=[validators.InputRequired(),validators.length(max=10)])
#     submit = SubmitField('login')
#
# # class AdminRegister(FlaskForm):
# #     name = TextField('Name',validators=[validators.InputRequired(),validators.length(max=100)])
# #     password = PasswordField('Password',validators=[validators.InputRequired(),validators.length(max=10)])
# #     submit = SubmitField('Signup')
