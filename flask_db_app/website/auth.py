from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        if len(email) < 4:
            flash('Длина электронной почты должна быть не менее 4 символов', category='error')
        elif len(first_name) < 2:
            flash('Длина имени должна быть не менее 2 символов.', category='error')
        elif password1 != password2:
            flash('Пароль не совпадает.', category='error')
        elif len(password1) < 8:
            flash('Пароль должен быть не менее 8 символов.', category='error')
        else:
            # Добавляем пользователя в базу данных
            flash('Аккаунт создан.', category='success')
            

    return render_template("sign-up.html")