from flask import Blueprint, render_template,request,flash, jsonify
from flask_login import login_user,login_required, current_user
from .models import Note,Project
from . import db
import json
import pdb
#import sqlite3 as sql

views = Blueprint('views', __name__)

@views.route("/home/note", methods=['GET','POST'])
def note():
    if request.method == 'POST':
        data = request.form
        print(data)
        notes = request.form.get('note')
        new_note = Note(data=notes, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash("note added", category="success")
    return render_template("notes.html", user=current_user)


@views.route('/home')
@login_required
def home():

    return render_template("home.html", user=current_user)

@views.route('/gp_yocto')
def gp_yocto():
    
    
    return render_template("gp_yocto.html", user=current_user)

@views.route('/fusa', methods=['GET','POST'])
def fusa():
    try:
        if request.method == 'POST':
            data = request.form
            print(data)
            title = request.form.get('title1')
            summary = request.form.get('summary')
            start_date = request.form.get('start_date')
            status = str(request.form.getlist("status")[0])
            help_needed = request.form.get('help')
            remark = request.form.get('remark')

            new_info = Project(title=title,summary=summary, start_date=start_date, status=status, help_needed=help_needed,remark=remark)
            db.session.add(new_info)
            db.session.commit()
            flash('New info added!', category='success')
    except Exception as e:
        print(e)
        flash('Failed to add new info', category='error')
    
    return render_template("fusa.html", user=current_user, project=Project.query.all())


@views.route('/list')
def list():
    #conn = sql.connnect("database.db")
    #conn.row_factory = sql.Row
    #cur = conn.cursor()
    #cur.execute("select * from Project")
    #rows = cur.fetchall()
    #return render_template("list.html", user=current_user, rows=rows)

    return render_template("list.html", project=Project.query.all())

@views.route('/time')
def tsn_tcc():

    return render_template("time.html", user=current_user)

@views.route('/inb')
def inb():
    return render_template("inb.html", user=current_user)

@views.route('/ipu')
def ipu():
    return render_template("ipu.html", user=current_user)

@views.route('/sriov')
def sr_iov():
    return render_template("sriov.html", user=current_user)

@views.route('/graphic')
def graphic():
    return render_template("graphic.html", user=current_user)

@views.route('/ips')
def ips():
    return render_template("ips.html", user=current_user)


@views.route('/ice')
def ice():
    return render_template("ice.html", user=current_user)

@views.route('/gp_android')
def android():
    return render_template("gp_android.html", user=current_user)



