from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename



auth = Blueprint('auth', __name__)
x = "result shown her"

@auth.route('/tires')
def login():
    return render_template("tires.html")


@auth.route('/Bethune-Awards')
def logout():
    dara = request.form
    print(dara)
    return render_template("Bethune-Awards.html", text=x)






