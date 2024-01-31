from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.wrappers.response import Response

from app.config.flash_config import SUCCESS_CLASS, ERROR_CLASS, ERROR_MESSAGE
from app.service.company_service import CompanyService
from app.service.company_service_impl import CompanyServiceImpl
from app.service.company_info_service import CompanyInfoService
from app.service.company_info_service_impl import CompanyInfoServiceImpl
from app.repository.company_repository_impl import CompanyRepositoryImpl

company_info_page = Blueprint("company_info_page", __name__, url_prefix="/company/<int:id>/info")
company_info_service: CompanyInfoService = CompanyInfoServiceImpl(CompanyRepositoryImpl())


@company_info_page.route("/show")
def show(id: int) -> str:
    company_info = company_info_service.find(id)

    if company_info:
        return render_template(
            "companyInfo.html",
            context={
                "company_info": company_info
            },
        )

    flash("企業が見つかりませんでした", ERROR_CLASS)
    return redirect(url_for("company_page.show_list"))


@company_info_page.route("/update", methods=["GET", "POST"])
def update(id: int) -> Response:
    company_info = None

    if request.method == "POST":
        company_info = company_info_service.update(request.form)

    if company_info:
        flash("基本情報を更新しました", SUCCESS_CLASS)
    else:
        flash(ERROR_MESSAGE, ERROR_CLASS)

    return redirect(url_for("company_info_page.show", id=id))
