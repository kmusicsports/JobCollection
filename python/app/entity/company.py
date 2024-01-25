from sqlalchemy import Column, Integer, String, Text

from app.database import db


class Company(db.Model):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    business = Column(Text)
    mvv = Column(Text)
    required_skill = Column(Text)
    location = Column(Text)
    benefit = Column(Text)
    applying_motivation = Column(Text)

    def __init__(
        self,
        id: int | None = None,
        name: str = "",
        business: str | None = None,
        mvv: str | None = None,
        required_skill: str | None = None,
        location: str | None = None,
        benefit: str | None = None,
        applying_motivation: str | None = None
    ):
        self.id = id
        self.name = name
        self.business = business
        self.mvv = mvv
        self.required_skill = required_skill
        self.location = location
        self.benefit = benefit
        self.applying_motivation = applying_motivation

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_business(self) -> str:
        return self.business

    def get_mvv(self) -> str:
        return self.mvv

    def get_required_skill(self) -> str:
        return self.required_skill

    def get_location(self) -> str:
        return self.location

    def get_benefit(self) -> str:
        return self.benefit

    def get_applying_motivation(self) -> str:
        return self.applying_motivation
