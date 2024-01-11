from flask import Blueprint, render_template

company_page = Blueprint("company_page", __name__, url_prefix="/company")


@company_page.route("/list")
def show_list():
    return render_template(
        "companyList.html",
        context={
            "message": "Hello, 就集!"
        },
    )
