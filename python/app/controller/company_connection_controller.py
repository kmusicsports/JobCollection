# from json import dumps as json_dumps

from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.wrappers.response import Response

from app.config.flash_config import SUCCESS_CLASS, ERROR_CLASS, ERROR_MESSAGE
from app.repository.company_repository_impl import CompanyRepositoryImpl
from app.repository.company_connection_repository_impl import (
    CompanyConnectionRepositoryImpl
)
from app.service.company_service import CompanyService
from app.service.company_service_impl import CompanyServiceImpl
from app.service.company_connection_service import CompanyConnectionService
from app.service.company_connection_service_impl import (
    CompanyConnectionServiceImpl
)
from app.view_model.company_connection_form import CompanyConnectionForm


company_connection_page = Blueprint(
    "company_connection_page",
    __name__,
    url_prefix="/company/<int:company_id>/connection"
)
company_service: CompanyService = CompanyServiceImpl(CompanyRepositoryImpl())
connection_service: CompanyConnectionService = CompanyConnectionServiceImpl(
    CompanyConnectionRepositoryImpl()
)


@company_connection_page.route("/create", methods=["GET", "POST"])
def create(company_id: int) -> Response:
    company_connection_form = None

    if request.method == "POST":
        company_connection_form = connection_service.create(request.form)

    if company_connection_form:
        flash("企業との接触情報を登録しました", SUCCESS_CLASS)
    else:
        flash(ERROR_MESSAGE, ERROR_CLASS)

    return redirect(
        url_for(
            "company_connection_page.show_list",
            company_id=company_id
        )
    )


@company_connection_page.route("/list")
def show_list(company_id: int) -> str:
    company_name = company_service.find(company_id)
    company_connection_forms = connection_service.make_list(company_id)
    return render_template(
        "companyConnectionList.html",
        context={
            "company_name": company_name,
            "company_connection_forms": company_connection_forms
        },
    )


@company_connection_page.route("/<int:id>")
def show_detail(
    company_id: int, id: int
) -> dict[str, CompanyConnectionForm] | Response:
    company_connection_form = connection_service.find(id)

    if company_connection_form:
        return {
            "company_connection_form": company_connection_form.__dict__
        }

    flash("接触情報が見つかりませんでした", ERROR_CLASS)
    return redirect(
        url_for(
            "company_connection_page.show_list",
            company_id=company_id
        )
    )


@company_connection_page.route("/update", methods=["GET", "POST"])
def update(company_id: int) -> Response:
    company_connection_form = None

    if request.method == "POST":
        company_connection_form = connection_service.update(request.form)

    if company_connection_form:
        flash("接触情報を更新しました", SUCCESS_CLASS)
    else:
        flash(ERROR_MESSAGE, ERROR_CLASS)

    return redirect(
        url_for(
            "company_connection_page.show_list",
            company_id=company_id
        )
    )


@company_connection_page.route("/delete/<int:id>")
def delete(company_id: int, id: int) -> Response:
    deleted = connection_service.delete(id)

    if deleted:
        flash("接触情報を削除しました", SUCCESS_CLASS)
    else:
        flash(ERROR_MESSAGE, ERROR_CLASS)

    return redirect(
        url_for(
            "company_connection_page.show_list",
            company_id=company_id
        )
    )
