from datetime import datetime
import re
from src.logger import logger
import traceback
from src import search_data, process_raw_file, generate_report, send_mail


def phone_validate(phones: str):
    phones = phones.replace(" ", "")
    if phones == "":
        print("Telefone não está no formato válido.")
        return False

    found = re.search(pattern=r"[\d,]", string=phones)
    if found == None:
        print("Telefone não está no formato válido.")
        return False

    phones_list = phones.split(",")
    for phone in phones_list:
        found = re.search(pattern=r"[\d]{8,13}", string=phone)
        if found == None:
            print("Telefone não está no formato válido.")
            return False

    return True


def data_validate(date: str):
    date = date.replace(" ", "")
    if date == "":
        print("Data não está no formato válido.")
        return False

    is_valid = re.search(
        pattern=r"[\d]{4}-[\d]{2}-[\d]{2}T[\d]{2}:[\d]{2}", string=date
    )
    if is_valid == None:
        print("Data não está no formato válido. (YYYY-MM-DDTHH:mm)")
        return False

    return True


def caminho_arquivo_validate(path_raw_file: str):
    path_raw_file = path_raw_file.replace(" ", "")
    if path_raw_file == "":
        print("Caminho do arquivo não está no formato válido.")
        return False

    return True


def enviar_email_validate(send_mail: str):
    send_mail = send_mail.replace(" ", "")
    if send_mail == "":
        print("Digite 'Sim' ou 'Não', para enviar o relatório por email.")
        return False

    send_mail = send_mail.lower()
    if send_mail != "sim" and send_mail != "nao":
        print("Digite 'Sim' ou 'Nao', para enviar o relatório por email.")
        return False

    return True


def main():
    logger.info("MAIN -> Iniciando a aplicação...")

    phones = ""
    send_mail = ""
    path_raw_file = ""
    date = ""

    while True:
        phones = input("Telefone(s): ")
        is_valid = phone_validate(phones)
        if is_valid == True:
            break

    while True:
        date = input("Data da confecção: ")
        is_valid = data_validate(date)
        if is_valid == True:
            break

    while True:
        send_mail = input("Envia o relatório por email? (Sim/Nao): ")
        is_valid = enviar_email_validate(send_mail)
        if is_valid == True:
            break

    while True:
        path_raw_file = input("Caminho do arquivo bruto: ")
        is_valid = caminho_arquivo_validate(path_raw_file)
        if is_valid == True:
            break

    logger.info("MAIN -> Input:")
    logger.info(phones)
    logger.info(date)
    logger.info(send_mail)
    logger.info(path_raw_file)

    execute_flow(
        phones=phones, date=date, is_send_mail=send_mail, path_raw_file=path_raw_file
    )

    logger.info("MAIN -> Finalizando a aplicação...")


def execute_flow(phones, date, is_send_mail, path_raw_file):
    phones = phones.replace(" ", "")
    phones = phones.split(",")
    customers = search_data.search_data(phones=phones)

    data = process_raw_file.process_raw_file(raw_file_path=path_raw_file)

    date = datetime.fromisoformat(date).strftime("%d/%m/%Y %H:%M")
    name = customers[0]["name"]
    name = name[0:25]
    header_info = {"customer": name, "date": date}
    analysis = data["analysis"]
    forecast = data["forecast"]
    report_path = generate_report.generate_report(
        analysis=analysis, forecast=forecast, header_info=header_info
    )

    is_send_mail = True if is_send_mail == "sim" else False
    emails = list(map(lambda item: item["email"], customers))
    send_mail.send_mail(
        date=date, is_send_mail=is_send_mail, report_path=report_path, to_emails=emails
    )


try:
    main()
except Exception as e:
    logger.error(traceback.format_exc())
    print("Houve algum erro, leia os logs para saber qual o problema.")
