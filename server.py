from flask import Flask, render_template, redirect, request, session, url_for
import common
import queries

app = Flask(__name__)
MENU_LIST = ["mentors", "applicants", "schools"]


@app.route("/")
def index():
    menu_titles = common.menu_zip(MENU_LIST)
    return render_template("home.html", menu_titles = menu_titles)

# Mentors

@app.route("/mentors", methods=['POST'])
def mentors():
    menu_titles = common.menu_zip(MENU_LIST)
    mentor_names = queries.mentor_names()
    return render_template("mentors.html", mentor_names = mentor_names, menu_titles = menu_titles)


@app.route("/mentors/<mentor_id>")
def mentor_page(mentor_id):
    menu_titles = common.menu_zip(MENU_LIST)
    headers = ["full_name", "phone_number", "email", "city", "favourite_number"]
    final_headers = common.header_format(headers)
    mentor_info = queries.mentor_info(mentor_id)
    return render_template("mentorpage.html", final_headers=final_headers, menu_titles=menu_titles, mentor_info=mentor_info)

# Applicants

@app.route("/applicants", methods=['GET','POST'])
def applicants():
    menu_titles = common.menu_zip(MENU_LIST)
    headers = ["full_name", "phone_number", "email", "application_code"]
    formatted_headers = common.header_format(headers, zipped=False)
    table = queries.applicant_info()
    return render_template("applicants.html", menu_titles=menu_titles, headers=headers, formatted_headers=formatted_headers, table=table)


@app.route("/new-applicant", methods=['POST'])
def new_applicant():
    menu_titles = common.menu_zip(MENU_LIST)
    headers = ["first_name", "last_name", "phone_number", "email", "application_code"]
    final_headers = common.header_format(headers)
    return render_template("new_applicant.html", menu_titles=menu_titles, final_headers=final_headers)


@app.route("/save-applicant", methods=['POST'])
def save_applicant():
    formdata = request.form
    queries.save_applicant(formdata)
    return redirect("/applicants")

# Schools

@app.route("/schools", methods=['POST'])
def schools():
    menu_titles = common.menu_zip(MENU_LIST)
    info_table = queries.school_info()
    return render_template("schools.html", menu_titles=menu_titles, info_table=info_table)

# Contacts

@app.route("/contacts")
def contacts():
    menu_titles = common.menu_zip(MENU_LIST)
    return render_template("contacts.html", menu_titles=menu_titles)


if __name__ == "__main__":
    app.secret_key = "whoeventriestoguessthis"
    app.run(
        debug=True,
        port=5000
    )