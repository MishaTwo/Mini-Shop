from . import app, login_manager
from .models import User, Item, session
from .forms.login import LoginForm
from .forms.registration import RegisterForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, logout_user, login_user
from werkzeug.security import check_password_hash, generate_password_hash

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(id=user_id)



@app.route("/")
def home():
    items = session.query(Item).all()
    return render_template("home.html", items=items)


@app.route("/login", methods=["GET", "POST"])
def log_in():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = session.query(User).filter_by(email=email).first()
        if not user:
            flash(f"User with email {email} does not exist.<br> <a href={url_for('register')}>Register</a>", "error")
            return redirect(url_for("log_in"))
        elif check_password_hash(user.password, form.password.data):
            login_user(user=user)
            return redirect(url_for("home"))
        else:
            flash("Password or email is incorrect", "error")
            return redirect(url_for("log_in"))
    else:
        return render_template("login.html", form=form)


@app.route("/register", methods=["POST", "GET"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        user = session.query(User).filter_by(email=email).first()
        if user:
            flash(f"User with email {email} exists.<br> <a href={url_for('log_in')}>Log in</a>", "error")
            return redirect(url_for("registration"))
        new_user = User(
            name=form.name.data,
            email=email,
            password=generate_password_hash(form.password.data),
            phone=form.phone.data
        )

        try:
            session.add(new_user)
            session.commit()
            flash("Thanks for registration! You can log in now!", "success")
            return redirect(url_for("log_in"))
        except Exception as exc:
            raise exc
        finally:
            session.close()
    return render_template("register.html", form=form)


@app.route("/logout")
@login_required
def log_out():
    logout_user()
    return redirect(url_for("log_in"))

@app.route("/add/<id>", methods=["POST"])
def add_to_card(id):
    if current_user.is_authenticated:
        flash("You must log in")
        return redirect(url_for("home"))
    item = session.query(Item).get(id=id)
    if request.method == "POST":
        quantitly = request.form["quantitly"]
        current_user.add_to_card(id, quantitly)
        flash(f'''{item.name} successfully added to the <a href=cart>cart</a>.<br> <a href={url_for("cart")}>view cart!</a>''','success')
        return redirect(url_for("home"))
    

@app.route('/orders')
@login_required
def orders():
    return render_template("order.html", orders=current_user.orders)

@app.route("/cart")
@login_required
def cart():
    price = 0
    quantity = []
    items = []
    price_ids = []
    
    for cart in current_user.cart:
        items.append(cart.item)
        quantity.append(cart.quantity)
        price_id_dict = {
            "price": cart.item.price_id,
            "quantity": cart.quantity
        }
        price_ids.append(price_id_dict)
        price += cart.item.price * cart.quantity
    return render_template("cart.html", items=items, quantity=quantity, price_ids=price_ids, price=price)

@app.route('/remove/<id>/<quntitly>')
@login_required
def remove(id, quntitly):
    current_user.remove_from_cart(id, quntitly)
    return redirect(url_for('cart'))

@app.route('/item/<int:id>')
def item(id):
    item = session.query(Item).get(id=id)
    return render_template('item.html', item=item)
        

@app.route('/search')
def search():
    query = request.args["query"]
    search = f"%{query}%"
    item = session.query(Item).filter(Item.name.like(search)).all()