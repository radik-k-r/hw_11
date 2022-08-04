import json


def load_candidates_from_json():
    """Возвращает список всех кандидатов"""
    with open("candidates.json", 'r', encoding='utf-8') as file:
        return json.loads(file.read())


def get_candidate_by_id(candidate_id: int) -> dict:
    """Возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """Возвращает кандидатов по имени"""
    candidates_list = []
    for candidate in load_candidates_from_json():
        if candidate['name'].lower() == candidate_name.lower():
            candidates_list.append(candidate)
    return candidates_list


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    candidates_skills_list = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate['skills'].lower():
            candidates_skills_list.append(candidate)
    return candidates_skills_list

