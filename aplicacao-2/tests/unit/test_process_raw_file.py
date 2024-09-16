from pytest_mock.plugin import MockerFixture
from pytest_mock.plugin import MockerFixture
from src.process_raw_file import process_raw_file
from tests.mocks.mock_raw_file import raw_file


def test_deve_conseguir_processar_o_arquivo_bruto(mocker: MockerFixture):
    mocker.patch("src.process_raw_file.load_raw_file", return_value=raw_file)

    raw_file_path = "/app/aplicacao-2/arquivo_bruto.json"

    processed_file = process_raw_file(raw_file_path=raw_file_path)

    analysis_phenomena = processed_file["analysis"]["phenomena"]
    forecast_phenomena = processed_file["forecast"]["phenomena"]

    assert len(analysis_phenomena) == 5
    assert analysis_phenomena[2]["phenomenon"] == "Outros"
    assert analysis_phenomena[4]["highlight"] == True

    assert len(forecast_phenomena) == 5
    assert len(forecast_phenomena[3]["infos"]) == 2
    assert forecast_phenomena[0]["highlight"] == True
    assert forecast_phenomena[3]["highlight"] == True
