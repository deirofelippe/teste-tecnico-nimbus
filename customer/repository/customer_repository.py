from customer.models import Customer
from logger import logger


class CustomerRepository:
    def __init__(self) -> None:
        pass

    def create(self, input: dict):
        try:
            logger.info("Criando customer no banco de dados")
            Customer.objects.create(
                id=input["id"],
                name=input["name"],
                email=input["email"],
                phone=input["phone"],
                age=input["age"],
            ).save()
            logger.info("Customer criado")
        except Exception as e:
            logger.error("Falha ao criar o customer no banco de dados")
            logger.error(e)
            raise e
