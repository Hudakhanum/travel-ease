from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms import BookingForm
from app.models import Booking

@app.route('/', methods=['GET', 'POST'])
def home():
    form = BookingForm()
    if form.validate_on_submit():
        booking = Booking(
            name=form.name.data,
            email=form.email.data,
            destination=form.destination.data,
            date=form.date.data
        )
        db.session.add(booking)
        db.session.commit()
        flash('Booking successful!', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', form=form)
