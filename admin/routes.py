from flask import Blueprint, render_template, url_for, flash, redirect
from ..models import Order, session, items
from .utills import admin_only
from .form_admin.item import AddItemForm
from .form_admin.order import OrderEditForm

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin",
    static_folder="static",
    template_folder = 'templates'
)

@admin.route('/')
@admin_only
def dashboard():
    orders = session.query(Order).all()
    return render_template("admin/admin.html", orders=orders)

@admin.route('/items')
@admin_only
def items():
    items = session.query(Order).all()
    return render_template("admin/items.html")

@admin.route('/add', methods=["POST", "GET"])
@admin.only
def  add():
    form = AddItemForm()
    if form .validate_on_submit():
        name = form.name.data
        price = form.name.data
        category = form.name.data
        details = form.name.data
        price_id = form.name.data
        image = url_for("static", filename=f"uploads/{form.image.data.filename}")

        item = items(
            name=name,
            price=price,
            category=category,
            details=details,
            price_id=price_id,
        ) 

        try:
            session.add(item)
            session.commit()
            flash(f"{name} added sucesfully!", 'succes')
            return redirect(url_for("admin.items"))
        except Exception as exc:
            return exc
        finally:
            session.close()

    else:
        return render_template('admin/add.html', form=form)
    
@admin.route('/edit/<string:type>/<int:id>', methods=['GET', 'POST'])
@admin_only
def edit(type, id):
    if type == 'item':
        item = session.query(items).get(id)
        form = AddItemForm(
            name = item.name,
            price = item.price,
            category = item.category,
            image = item.image,
            details = item.details,
            price_id = item.price_id,
        )
        if form.validate_on_submit:
            item.name = form.name.data
            item.price = form.price.data
            item.category = form.category.data
            item.details = form.details.data
            item.image = url_for('static', filename=f"uploads/{form.image.data.filename}")
            item.price_id = form.price_id.data

            try:
                session.commit()
                return redirect(url_for("admin.items"))
            except Exception as e:
                raise e
            finally:
                session.close()
    elif type == "order":
        order = session.query(Order).get(id)
        form = OrderEditForm(
            status=form.status.data
        )
        if form.validate_on_submit:
            order.status = form.status.data
            
            try:
                session.commit()
                return redirect(url_for("admin.dashboard"))
            except Exception as exc:
                raise exc
            finally:
                session.close()
    else:
        return render_template("admin/add.html", form=form)
    
@admin.route('/delete/<int:id>')
@admin_only
def delete():
    item_to_delete = session.query(items).get(id)
    session.delete(item_to_delete)
    session.commit()
    flash(f"{item_to_delete} was deleted succesfuly!", "success")
    return redirect(url_for("admin.items"))