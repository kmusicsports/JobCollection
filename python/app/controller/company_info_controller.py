from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.wrappers.response import Response

from app.config.flash_config import SUCCESS_CLASS, ERROR_CLASS, ERROR_MESSAGE
from app.service.company_service import CompanyService
from app.service.company_service_impl import CompanyServiceImpl
from app.service.company_info_service import CompanyInfoService
from app.service.company_info_service_impl import CompanyInfoServiceImpl
from app.repository.company_repository_impl import CompanyRepositoryImpl

#Buleprintの作成、アプリの分割が可能？
#ここでアプリのページの定義をしているっぽい
company_info_page = Blueprint("company_info_page", __name__, url_prefix="/info")

company_info_service: CompanyInfoService = CompanyInfoServiceImpl(CompanyRepositoryImpl())


#以下の関数は基本情報を表示するもの
#route():リクエスト内容とサーバとの処理を紐づけるもの
@company_info_page.route("/info/<id>")
def show(id: int) -> str:
    return render_template(
        "companyInfo.html"
    )

#以下の関数は基本情報を更新するもの
#ここもよく分かりません…
'''
@company_info_page.route("/info/<id>", methods=["GET", "POST"])
def update(self, form: ImmutableMultiDict[str, str]) -> Response:
    company_info = None

    if request.method == "POST":
        company_info = company_info_service.update(request.form)

    if company_info:
        flash("編集が完了しました", SUCCESS_CLASS)
    else:
        flash(ERROR_MESSAGE, ERROR_CLASS)

    return redirect(
        url_for("company_info_page.show", id=company_name.get_id()) #idがいるならget_idが使えるcompany_nameが必要?
    )
'''
