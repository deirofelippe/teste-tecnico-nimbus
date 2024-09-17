import smtplib
from email.message import EmailMessage
from constants import (
    FROM_EMAIL,
    NAME_EMAIL,
    SMTP_HOST,
    SMTP_PORT,
    SMTP_HOST_TEST,
    SMTP_PORT_TEST,
    SMTP_TEST,
    FROM_PASSWORD,
)
from src.logger import logger


def send_mail(
    report_path: str, is_send_mail: bool, to_emails: list[str], date: str
) -> None:
    logger.info("SEARCHDATA -> Input: ")
    logger.info(report_path)
    logger.info(is_send_mail)
    logger.info(to_emails)
    logger.info("SENDMAIL -> Iniciando a etapa de envio de email...")

    if is_send_mail == False:
        logger.info("SENDMAIL -> Finalizando a etapa de envio de email (flag)...")
        return

    logger.info("SENDMAIL -> Construindo a mensagem...")
    message = build_message(report_path, to_emails, date)

    logger.info("SENDMAIL -> iniciando o envio de email...")
    send(message)

    logger.info("SENDMAIL -> Finalizando a etapa de envio de email...")
    logger.info("SENDMAIL -> Output:")
    logger.info(None)


def build_message(report_path: str, to_emails: list, date: str) -> EmailMessage:
    subject = "Relatório Meteorológico"
    to_email = ",".join(to_emails)

    message = EmailMessage()
    message["Subject"] = subject + " " + date
    message["From"] = FROM_EMAIL
    message["To"] = to_email
    message.set_content(
        f"<html><body><p>Olá, segue em anexo o relatório meteorológico.</p><p>Data de confecção: {date}</p></body></html>",
        subtype="html",
    )

    report_file = load_file(report_path)

    filename = report_path.split("/").pop()
    message.add_attachment(
        report_file, maintype="application", subtype="pdf", filename=filename
    )

    return message


def load_file(report_path: str):
    with open(report_path, "rb") as file:
        return file.read()


def send(message: EmailMessage):
    smtp = {}
    if SMTP_TEST == True:
        smtp = smtplib.SMTP(SMTP_HOST_TEST, SMTP_PORT_TEST)
    else:
        smtp = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)

    with smtp as server:
        server.login(FROM_EMAIL, FROM_PASSWORD)
        server.send_message(message)
        server.quit()
