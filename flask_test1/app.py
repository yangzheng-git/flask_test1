from flask import Flask,request,render_template,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key='nihao'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Date(db.Model):
    __tablename__='dates'
    id=db.Column(db.Integer,primary_key=True)
    date_name=db.Column(db.String(16),unique=True)
    texts=db.relationship('Text',backref='Date')


class Text(db.Model):
    __tablename__='text'
    id = db.Column(db.Integer, primary_key=True)
    author=db.Column(db.String)
    text_main=db.Column(db.String)
    text_id=db.Column(db.Integer,db.ForeignKey('dates.id'))


@app.route('/delate_text/<text_id>')
def delate_text(text_id):
    text=Text.query.get(text_id)
    if text:
        db.session.delete(text)
        db.session.commit()
    return redirect(url_for('main_1'))

@app.route('/delate_date/<date_id>')
def delate_date(date_id):
    print(date_id)
    date=Date.query.get(date_id)
    if date:
        print(date.date_name)
        print('nihao')
        db.session.delete(date)
        db.session.commit()
    return redirect(url_for('main_1'))


@app.route('/main',methods=['GET','POST'])
def main():
    # return redirect('https://www.baidu.com/')    #用重定向访问外部网站，用render tenplate跳转到内部网页
    return render_template('main.html')


@app.route('/main_1',methods=['GET','POST'])
def main_1():


    dates=Date.query.all()
    # print(authors)
    # return redirect('https://www.baidu.com/')    #用重定向访问外部网站，用render tenplate跳转到内部网页
    return render_template('main_1.html',dates=dates)


@app.route('/main_2',methods=['GET','POST'])
def main_2():

    if request.method=='POST':
        # print('daodao')
        if request.form.get('date') and request.form.get('author') and request.form.get('zhengwen'):
            date1=request.form.get('date')
            author=request.form.get('author')
            zhengwen=request.form.get('zhengwen')
            date_new=Date(date_name=date1)


            db.session.add(date_new)
            db.session.commit()
            text_new = Text(author=author, text_main=zhengwen, text_id=date_new.id)

            db.session.add(text_new)
            db.session.commit()
            print(date1)
            print(author)
            print(zhengwen)
            pass
        else:
            flash('请完整填写')
    # return redirect('https://www.baidu.com/')    #用重定向访问外部网站，用render tenplate跳转到内部网页
    return render_template('main_2.html')
@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_name = request.form.get('username')
        pass_word=request.form.get('password')
        print(pass_word)
        print(user_name)

        if user_name=='yeang' and pass_word=='102506':

            return  render_template('main.html')
        else:
            flash("登陆失败")





    return render_template('login.html')


if __name__ == '__main__':
# db.drop_all()
# db.create_all()
#
# da1=Date(date_name='11.2.3')
# da2=Date(date_name='13.4.5')
# db.session.add_all([da1,da2])
# db.session.commit()
# text1=Text(author='杨铮',text_main='安神补脑代发表示大富科技·即可BADSFKB第三方即可·看JBNSDFK·',text_id=da1.id)
# text2=Text(author='叶书君',text_main='anmdfiand你好nd',text_id=da2.id)
# text3=Text(author='叶书君',text_main='anmdfiand你afsdfawsedfasdfaseawefASDFAEFDAF ASEDFAWEFASDFAWE好nd',text_id=da2.id)
# db.session.add_all([text1,text2,text3])
# db.session.commit()
   app.run(debug=True,host='192.168.137.1',port=8090)
