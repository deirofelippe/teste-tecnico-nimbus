from tests.mocks.mock_processed_raw_file import analysis, forecast, header_info
from src.generate_report import generate_report


def test_deve_gerar_o_relatorio():
    filename = generate_report(
        header_info=header_info, analysis=analysis, forecast=forecast
    )

    assert "/reports/Relatorio_Meteorologico_" in filename
