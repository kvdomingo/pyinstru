import os
from calendar import month_name
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, exc
from manage import *


@app.context_processor
def inject_now():
    return {"now": datetime.now()}


@app.context_processor
def inject_month():
    month_list = [m for m in month_name]
    return {"month_list": month_list}


@app.route("/")
def index():
    slider_files = os.listdir("web/templates/content/home")
    adviser_names = ["Saloma", "Soriano", "Lim", "Tapang", "Bantang"]
    adviser_pics = [f"images/{f}.jpg" for f in adviser_names]
    recent_publ = Publication.query.filter(Publication.year == 2019).filter(Publication.pub_type != "spp").filter(Publication.volume is not None).filter(Publication.authors != "C Saloma").order_by(Publication.month.desc()).limit(3).all()
    carousel_pics = ["IPL Text.png", "National_Institute_of_Physics_logo.png",
                    "ipl grp.jpg", "Saloma.jpg",
                    "Soriano.jpg", "Lim.jpg",
                    "Tapang.jpg", "Bantang.jpg",
                    "csdean.jpg", "Saloma.jpg"]
    research_pics = ["signalproc.png", "cxsystems.png",
                    "videoimgproc.png", "bio.png",
                    "optics.png"]
    return render_template("index.html.j2",
                            adviser_names=adviser_names,
                            slider_files=slider_files,
                            adviser_pics=adviser_pics,
                            recent_publ=recent_publ,
                            carousel_pics=carousel_pics,
                            research_pics=research_pics)


@app.route("/about")
def about():
    return render_template("about.html.j2")


@app.route("/principal-investigators")
def principals():
    adviser_names = ["Caesar A. Saloma", "Maricor N. Soriano", "May T. Lim", "Giovanni A. Tapang", "Johnrob Y. Bantang"]
    adviser_surnames = [n.split(" ")[-1] for n in adviser_names]
    return render_template("principals.html.j2",
                            summary=zip(adviser_names, adviser_surnames))


@app.route("/publications")
def publications():
    reg_years = [2019, 2018, 2017]
    spp_years = [2019]
    regular = []
    spp = []
    for y in reg_years:
        res = Publication.query.filter(Publication.pub_type == "reg").filter(Publication.year == y).all()
        regular.append(res)
    for y in spp_years:
        res = Publication.query.filter(Publication.pub_type == "spp").filter(Publication.year == y).all()
        spp.append(res)
    return render_template("publications.html.j2",
                            regular=regular,
                            reg_years=reg_years,
                            spp=spp,
                            spp_years=spp_years)


@app.route("/research")
def research():
    return render_template("research.html.j2")


@app.route("/report-publication")
def add_publication():
    return render_template("add_publication.html.j2")


@app.route("/success", methods=["POST"])
def success():
    key, val = [], []
    form_items = {}
    submitter_name = "Submitted by: "
    submitter_email = ".\nContact: "
    for k, v in request.form.items():
        if v == "":
            v = None
        if k == "submitter_name":
            submitter_name += v
            continue
        if k == "submitter_email":
            submitter_email += v
            continue
        form_items[k] = v
    form_items["pub_type"] = "reg"
    form_items["remarks"] = submitter_name + submitter_email + "."
    db.session.add(Publication(**form_items))
    db.session.commit()
    return redirect(url_for('add_publication'))


if __name__ == "__main__":
    app.run()
