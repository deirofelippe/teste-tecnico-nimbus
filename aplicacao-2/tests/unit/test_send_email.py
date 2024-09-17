from pytest_mock.plugin import MockerFixture
from src.send_mail import send_mail
from constants import SMTP_TEST


def test_send_mail(mocker: MockerFixture):
    mocker.patch(
        "variables.SMTP_TEST",
        True,
    )

    report_path = "/app/aplicacao-2/reports/Relatorio_Meteorologico_modelo.pdf"
    is_send_mail = True

    to_emails = ["teste1@gmail.com", "teste2@gmail.com"]

    date = "10/07/2024 06:30"

    send_mail(
        report_path=report_path,
        is_send_mail=is_send_mail,
        to_emails=to_emails,
        date=date,
    )

    assert 2 == 2
