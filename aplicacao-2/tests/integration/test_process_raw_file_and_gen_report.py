import pytest
from pytest_mock.plugin import MockerFixture
from src.process_raw_file import process_raw_file
from src.generate_report import generate_report
from tests.mocks.mock_raw_file import raw_file


def test_process_raw_file_and_gen_report(mocker: MockerFixture):
    mocker.patch("src.process_raw_file.load_raw_file", return_value=raw_file)

    header_info = {
        "customer": "Felippe",
        "date": "15/09/2024",
    }
    raw_file_path = "/app/aplicacao-2/arquivo_bruto.json"

    processed_file = process_raw_file(raw_file_path=raw_file_path)
    filename = generate_report(
        header_info=header_info,
        analysis=processed_file["analysis"],
        forecast=processed_file["forecast"],
    )

    assert "analysis" in processed_file
    assert "forecast" in processed_file
    assert "/reports/Relatorio_Meteorologico_" in filename
