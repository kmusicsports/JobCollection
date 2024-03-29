from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.wrappers.response import Response

from app.config.flash_config import SUCCESS_CLASS, ERROR_CLASS, ERROR_MESSAGE
from app.view_model.company_name import CompanyName
from app.service.company_service import CompanyService
from app.service.company_service_impl import CompanyServiceImpl
from app.repository.company_repository_impl import CompanyRepositoryImpl

company_page = Blueprint("company_page", __name__, url_prefix="/company")
company_service: CompanyService = CompanyServiceImpl(CompanyRepositoryImpl())


@company_page.route("/create", methods=["GET", "POST"])
def create() -> Response:
    company_name: CompanyName = None

    if request.method == "POST":
        company_name = company_service.create(request.form)

    if company_name:
        flash("企業を登録しました", SUCCESS_CLASS)
    else:
        flash(ERROR_MESSAGE, ERROR_CLASS)

    return redirect(
        url_for("company_page.show_detail", id=company_name.get_id())
    )


@company_page.route("/list")
def show_list() -> str:
    companies_name: list[CompanyName] = company_service.make_list()
    return render_template(
        "companyList.html",
        context={
            "companies_name": companies_name
        },
    )


@company_page.route("/<int:id>")
def show_detail(id: int) -> str:
    company_name: CompanyName = company_service.find(id)

    if company_name:
        return render_template(
            "companyDetail.html",
            context={
                "company_name": company_name
            },
        )

    flash("企業が見つかりませんでした", ERROR_CLASS)
    return redirect(url_for("company_page.show_list"))


@company_page.route("/delete/<id>")
def delete(id: int) -> Response:
    deleted = company_service.delete(id)

    if deleted:
        flash("企業を削除しました", SUCCESS_CLASS)
    else:
        flash(ERROR_MESSAGE, ERROR_CLASS)

    return redirect(url_for("company_page.show_list"))
