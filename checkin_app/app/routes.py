from flask import render_template, flash, redirect
from app import app
from app.forms import card_form
from csv import writer

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = card_form()
    if form.validate_on_submit():
        nnum = f'N{form.card_data.data[2:10]}'
        List = [nnum]
        with open('swipes.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()
        flash(f'Added {nnum} to CSV.')
        return redirect('/index')
    return render_template('index.html', title='Home', form=form)