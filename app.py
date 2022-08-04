from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def preview_page():
    """Отображает всех кандидатов"""
    data = load_candidates_from_json()
    return render_template("list.html", data=data)


@app.route("/candidate/<int:idx>")
def link_to_info(idx):
    """Выводит информацию о кандидате при нажатии ссылки"""
    person = get_candidate_by_id(idx)
    return render_template("card.html", person=person)


@app.route("/search/<candidate_name>")
def search_by_name(candidate_name):
    """Выводит кандидатов по введенному имени"""
    persons = get_candidates_by_name(candidate_name)
    return render_template("search.html", persons=persons)


@app.route("/skills/<skill_name>")
def search_by_skill(skill_name):
    """Выводит кандидатов по введенному навыку"""
    persons = get_candidates_by_skill(skill_name)
    return render_template("skills.html", persons=persons, skill_name=skill_name)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
