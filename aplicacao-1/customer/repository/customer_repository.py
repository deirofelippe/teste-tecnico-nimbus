from customer.models import Customer
from logger import logger


class CustomerRepository:
    def __init__(self) -> None:
        pass

    def create(self, input: dict):
        logger.debug("REPOSITORY -> Input:")
        logger.debug(input)
        try:
            logger.info("REPOSITORY -> Criando customer no banco de dados.")
            Customer.objects.create(
                id=input["id"],
                name=input["name"],
                email=input["email"],
                phone=input["phone"],
                age=input["age"],
            ).save()
            logger.info("REPOSITORY -> Customer criado.")
        except Exception as e:
            logger.error("REPOSITORY -> Falha ao criar o customer no banco de dados.")
            logger.error(e)
            raise e
