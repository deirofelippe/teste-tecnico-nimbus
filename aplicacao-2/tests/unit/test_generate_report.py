from faker import Faker
import pytest
from pytest_mock.plugin import MockerFixture
from mocks.processed_raw_file import analysis, forecast, header_info
from src.generate_report import generate_report


@pytest.fixture
def setup_data():
    data = 1
    yield data


def test_deve_gerar_o_relatorio(mocker: MockerFixture, setup_data: int):
    generate_report(header_info=header_info, analysis=analysis, forecast=forecast)
