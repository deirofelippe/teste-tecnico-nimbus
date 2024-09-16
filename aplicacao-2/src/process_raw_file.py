import re
import json
from datetime import datetime


def process_raw_file(raw_file_path: str) -> dict:
    data = load_raw_file(raw_file_path)

    analysis = create_new_phenomena_list_structure(data["análise"], "Análise")
    forecast = create_new_phenomena_list_structure(data["previsao"], "Previsão")

    return {
        "analysis": analysis,
        "forecast": forecast,
    }


def load_raw_file(raw_file_path: str):
    with open(raw_file_path, "r") as file:
        return json.load(file)


def create_new_phenomena_list_structure(phenomena_list: list, type: str) -> dict:
    new_phenomena_list = []
    for item in phenomena_list:
        words_found = re.findall(pattern="[Ff]orte", string=item["mensagem"])
        highlight = len(words_found) > 0

        phenomenon = ""
        if "fenomeno" in item:
            phenomenon = item["fenomeno"].capitalize()
        else:
            phenomenon = "Outros"

        date = datetime.fromisoformat(item["data"]).strftime("%d/%m/%Y às %H:%m")

        info = {"date": date, "message": item["mensagem"]}

        phenomenon_dict = {
            "highlight": highlight,
            "phenomenon": phenomenon,
            "infos": [],
        }
        phenomenon_dict["infos"].append(info)

        if phenomenon_exist_in_list(new_phenomena_list, phenomenon):
            updated_phenomena_list = add_phenomenon_info_in_list(
                new_phenomena_list, phenomenon_dict
            )
            new_phenomena_list = updated_phenomena_list
            continue

        new_phenomena_list.append(phenomenon_dict)

    return {"type": type, "phenomena": new_phenomena_list}


def phenomenon_exist_in_list(phenomena_list: list, phenomenon: str) -> bool:
    if len(phenomena_list) < 1:
        return False

    for item in phenomena_list:
        if item["phenomenon"] == phenomenon:
            return True

    return False


def add_phenomenon_info_in_list(phenomena_list: list, phenomenon_dict: dict) -> list:
    phenomenon_is_different = lambda item: item["phenomenon"] != phenomenon

    updated_dict = {}
    phenomena_list_filtered = []
    for item in phenomena_list:
        phenomenon = phenomenon_dict["phenomenon"]
        if item["phenomenon"] == phenomenon_dict["phenomenon"]:
            updated_dict = item
            phenomena_list_filtered = filter(phenomenon_is_different, phenomena_list)
            phenomena_list_filtered = list(phenomena_list_filtered)
            break

    if phenomenon_dict["highlight"] == True:
        updated_dict["highlight"] = True

    updated_dict["infos"].append(
        {
            "date": phenomenon_dict["infos"][0]["date"],
            "message": phenomenon_dict["infos"][0]["message"],
        }
    )
    phenomena_list_filtered.append(updated_dict)

    return phenomena_list_filtered
