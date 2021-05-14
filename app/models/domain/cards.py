from odmantic import Model

from app.models.domain.rwmodel import RWModel


class Card(Model, RWModel):
    question_text: str
    answer_text: str
