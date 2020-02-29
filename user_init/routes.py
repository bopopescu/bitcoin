from flask import render_template, url_for, redirect, flash
from user_init import app, db, bcrypt
from user_init.form import RegistrationForm, LoginForm ,Make_DepositForm
from user_init.models import User
from flask_login import login_user, current_user ,logout_user, login_required




Deposits = [
    {
        'username': 'Azizi',
        'last_deposit': '$234 last deposit',
        'total_deposit': '$2200 total deposits',
        'date_deposited': 'December 10, 2019'
    },
    {
        'username': 'Jumanne',
        'last_deposit': '$678 last Deposit',
        'total_deposit': '$4000 total deposited',
        'date_deposited': 'December 10, 2019'
    },
    {
        'username': 'Herman',
        'last_deposit': '$3498 last deposit',
        'total_deposit': '$6400 total deposits',
        'date_deposited': 'December 10, 2019'
    },
    {
        'username': 'Michael',
        'last_deposit': '$500 last Deposit',
        'total_deposit': '$6543 total deposited',
        'date_deposited': 'December 10, 2019'
    },
    {
        'username': 'Erick Sholo',
        'last_deposit': '$2900 last deposit',
        'total_deposit': '$3420 total deposits',
        'date_deposited': 'December 10, 2019'
    },
    {
        'username': 'Alpha',
        'last_deposit': '$459 last Deposit',
        'total_deposit': '$1892 total deposited',
        'date_deposited': 'December 10, 2019'
    },
    {
        'username': 'Erick fupi',
        'last_deposit': '$2340 last deposit',
        'total_deposit': '$22000 total deposits',
        'date_deposited': 'December 10, 2019'
    },
    {
        'username': 'Neema',
        'last_deposit': '$230 last Deposit',
        'total_deposit': '$5389 total deposited',
        'date_deposited': 'December 10, 2019'
    }
]



Withdraws = [
    {
        'username': 'Azizi',
        'last_withdraw': '$234 last withdrew',
        'total_withdraw': '$2200 total withdraw',
        'withdrew_date': 'December 10, 2019'
    },
    {
        'username': 'Jumanne',
        'last_withdraw': '$678 last withdrew',
        'total_withdraw': '$4000 total withdrew',
        'withdrew_date': 'December 10, 2019'
    },
    {
        'username': 'Herman',
        'last_withdraw': '$3498 last withdrew',
        'total_withdraw': '$6400 total withdrew',
        'withdrew_date': 'December 10, 2019'
    },
    {
        'username': 'Michael',
        'last_withdraw': '$500 last withdrew',
        'total_withdraw': '$6543 total withdraw',
        'withdrew_date': 'December 10, 2019'
    },
    {
        'username': 'Erick Sholo',
        'last_withdraw': '$2900 last withdraw',
        'total_withdraw': '$3420 total withdraw',
        'withdrew_date': 'December 10, 2019'
    },
    {
        'username': 'Alpha',
        'last_withdraw': '$459 last withdraw',
        'total_withdraw': '$1892 total withdraw',
        'date_deposited': 'December 10, 2019'
    },
    {
        'username': 'Erick fupi',
        'last_withdraw': '$2340 last withdraw',
        'total_withdraw': '$22000 total withdraw',
        'withdrew_date': 'December 10, 2019'
    },
    {
        'username': 'Neema',
        'last_withdraw': '$230 last withdraw',
        'total_withdraw': '$5389 total withdraw',
        'date_deposited': 'December 10, 2019'
    }
]



News = [
    {
        'Latest_news': 'Recently Uploaded',
        'news_content': 'Since the existence of cryptocurrency on the world financial markets, it has become very popular among the investors. The most ambitious of them realizing that eventually an interest of the people, who want to make a profit from fluctuations of cryptocurrency exchange rate and its mining, will grow.',
        'date_deposited': 'December 10, 2019'
    },
    {
         'Latest_news': 'Recently Uploaded',
        'news_content': 'Since the existence of cryptocurrency on the world financial markets, it has become very popular among the investors. The most ambitious of them realizing that eventually an interest of the people, who want to make a profit from fluctuations of cryptocurrency exchange rate and its mining, will grow.',
        'date_deposited': 'December 10, 2019'
    },
    {
        'Latest_news': 'Recently Uploaded',
        'news_content': 'Since the existence of cryptocurrency on the world financial markets, it has become very popular among the investors. The most ambitious of them realizing that eventually an interest of the people, who want to make a profit from fluctuations of cryptocurrency exchange rate and its mining, will grow.',
        'date_deposited': 'December 10, 2019'
    }
    ]



@app.route('/')
@app.route('/home', methods =['GET','POST'])
def home():
    logo = url_for("static", filename="logo/logo.jpg")
    return render_template('home.html', title='home',Deposits=Deposits, Withdraws=Withdraws, News=News, logo=logo)


@app.route('/deposits', methods =['GET','POST'])
def deposits():
	return render_template('deposits.html', title='last deposits',Deposits=Deposits)	

@app.route('/withdraws', methods =['GET','POST'])
def withdraws():
	return render_template('withdraws.html', title='last withdraws',Withdraws=Withdraws)

@app.route('/news', methods =['GET','POST'])
def news():
	return render_template('News.html', title='News',News=News)


@app.route('/contact', methods =['GET','POST'])
def contact():
	return render_template('contact.html', title='contact')	

@app.route('/')
def layout():
    logo = url_for("static", filename="logo/logo.jpg")
    return render_template('layout.html', logo=logo)


@app.route('/make_withdraw', methods =['GET','POST'])
@login_required
def make_withdraw():
    return render_template('Make_withdraw.html', title='Make withdraw')

@app.route('/make_deposit', methods =['GET','POST'])
@login_required
def make_deposit():
    form = Make_DepositForm()

    if form.validate_on_submit():

        flash(f'Your deposit has been sent! Now wait for confirmation massage which may take up to 5minutes', 'success')

        flash(f'confirmation massage will be sent to your email address', 'info')

        return redirect(url_for('Account'))

    return render_template('Make_deposit.html', title='Make Deposits',form=form)  

@app.route('/active_deposit', methods =['GET','POST'])
@login_required
def active_deposit():
    return render_template('Active_deposit.html', title='Active deposit')

@app.route('/withdraw_history', methods =['GET','POST'])
@login_required
def withdraw_history():
    return render_template('Withdraws_history.html', title='Withdraws history')

@app.route('/deposit_history', methods =['GET','POST'])
@login_required
def deposit_history():
    return render_template('Deposits_history.html', title='Deposits history') 

@app.route('/edit_account', methods =['GET','POST'])
@login_required
def edit_account():
    return render_template('Edit_account.html', title='Edit account')        
               	


@app.route('/about', methods =['GET','POST'])
def about():
	return render_template('about.html', title='about')	
    


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has been created! You are now able to log in', 'success')
        return redirect(url_for('Login'))

    
            
    return render_template('register.html', title='Register', form=form)

@app.route("/Login", methods=['GET', 'POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'successfull logedd in', 'success')
            return render_template('Account.html',title='Account')
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/Logout")
def Logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/Account")
@login_required
def Account():
    image_file = url_for('static',filename='profiles/Author__Placeholder.png')
    return render_template('Account.html',title='Account', image_file=image_file)
    
