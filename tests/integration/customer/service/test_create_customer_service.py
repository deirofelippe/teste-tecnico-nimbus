from uuid import UUID
from faker import Faker
import pytest
from pytest_mock.plugin import MockerFixture
from customer.service.create_customer_service import CreateCustomerService
from customer.repository.customer_repository import CustomerRepository
from customer.validator.create_customer_validator import CreateCustomerValidator

faker = Faker("pt_BR")


@pytest.fixture
def setup_data():
    data = {
        "name": faker.first_name(),
        "email": faker.email(),
        "phone": str(faker.random_number(fix_len=True, digits=11)),
        "age": str(faker.random_number(digits=2)),
    }
    yield data


@pytest.fixture
def setup_service():
    customer_repository = CustomerRepository()
    create_customer_validator = CreateCustomerValidator()
    customer_service = CreateCustomerService(
        customer_repository, create_customer_validator
    )
    yield customer_service


def test_deve_conseguir_criar_customer_no_mock(mocker: MockerFixture, setup_data: dict):
    customer_repository = CustomerRepository()
    mock = mocker.patch.object(customer_repository, "create", return_value=None)

    create_customer_validator = CreateCustomerValidator()

    customer_service = CreateCustomerService(
        customer_repository, create_customer_validator
    )

    name = setup_data["name"]
    email = setup_data["email"]
    phone = setup_data["phone"]
    age = setup_data["age"]
    input = {"data": f"{name},{email},{phone},{age}"}

    result = customer_service.execute(input)

    call_args = mock.call_args[0][0]

    assert type(call_args["id"]) == UUID
    assert call_args["name"] == name
    assert call_args["email"] == email
    assert call_args["phone"] == phone
    assert call_args["age"] == age
    assert len(result["errors"]) == 0
