from logger import logger
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.service.create_customer_service import CreateCustomerService
from customer.repository.customer_repository import CustomerRepository
from customer.validator.create_customer_validator import CreateCustomerValidator

customer_repository = CustomerRepository()
create_customer_validator = CreateCustomerValidator()
create_customer_service = CreateCustomerService(
    customer_repository, create_customer_validator
)


@api_view(["GET"])
def hello_world(request):
    request.data
    return Response({"message": "Hello, world!"})


@api_view(["POST"])
def create(request):
    logger.info("VIEW -> Iniciando a execução da view...")
    try:
        result = create_customer_service.execute(request.data)

        if len(result["errors"]):
            return Response(
                data={"message": "Os dados enviados estão fora do formato."}, status=422
            )

    except Exception as e:
        logger.error("VIEW -> Error")
        logger.error(e)
        return Response(data={"message": "Internal Server Error"}, status=500)

    return Response({"message": "Ok"}, status=201)
