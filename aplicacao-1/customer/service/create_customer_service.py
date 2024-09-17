import uuid
from customer.repository.customer_repository import CustomerRepository
from customer.validator.create_customer_validator import CreateCustomerValidator
from logger import logger


class CreateCustomerService:
    def __init__(
        self,
        customer_repository: CustomerRepository,
        create_customer_validator: CreateCustomerValidator,
    ):
        self.customer_repository = customer_repository
        self.create_customer_validator = create_customer_validator

    def execute(self, customer_data) -> dict:
        logger.info("SERVICE -> Iniciando o service...")
        logger.debug("SERVICE -> Input:")
        logger.debug(customer_data)

        result = {"errors": {}}

        data = customer_data["data"]
        data = data.split(",")

        if len(data) != 4:
            result["errors"]["others"] = [
                "Falta campos ou o número de campos foi excedido. Informe o nome, email, telefone e idade."
            ]

            logger.warning("Falha na validação")
            logger.warning(result)
            return result

        customer = {
            "name": data[0],
            "email": data[1],
            "phone": data[2],
            "age": data[3],
        }

        logger.info("SERVICE -> Iniciando validação...")
        errors = self.create_customer_validator.execute(customer)

        if len(errors) > 0:
            result["errors"].update(errors)

            logger.warning("Falha na validação")
            logger.warning(result)
            return result

        customer["id"] = uuid.uuid4()

        self.customer_repository.create(customer)

        logger.debug("SERVICE -> Finalizando o service...")
        logger.debug("SERVICE -> Output:")
        logger.debug(result)

        return result
