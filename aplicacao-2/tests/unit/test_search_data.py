from pytest_mock.plugin import MockerFixture
from src.search_data import search_data


def test_search_data(mocker: MockerFixture):
    mock_return = [("teste1", "teste1@gmail.com"), ("teste2", "teste2@gmail.com")]
    mocker.patch(
        "src.search_data.execute_query",
        return_value=mock_return,
    )

    phones = ["21991028955", "998580055"]
    customers = search_data(phones)

    assert len(customers) == 2
    assert customers[0]["name"] == mock_return[0][0]
    assert customers[0]["email"] == mock_return[0][1]
    assert customers[1]["name"] == mock_return[1][0]
    assert customers[1]["email"] == mock_return[1][1]
