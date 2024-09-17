import mysql.connector
import traceback
from src.logger import logger


def search_data(phones: list) -> list:
    logger.info("SEARCHDATA -> Input: ")
    logger.info(phones)
    logger.info(
        "SEARCHDATA -> Iniciando a etapa de busca de customers no banco de dados..."
    )
    list_in = list(map(lambda item: "%s", phones))
    list_in = ",".join(list_in)
    list_in = f"({list_in})"

    customers = []

    customers = execute_query(list_in, phones)

    customer_tuple_to_dict = lambda customer: {
        "name": customer[0],
        "email": customer[1],
    }

    customers = map(customer_tuple_to_dict, customers)  # type: ignore
    customers = list(customers)

    logger.info(
        "SEARCHDATA -> Finalizando a etapa de busca de customers no banco de dados..."
    )
    logger.info("SEARCHDATA -> Output:")
    logger.info(customers)
    return customers


def execute_query(list_in: str, phones: list):
    try:
        connection = mysql.connector.connect(
            host="db", user="root", password="root", database="teste_nimbus"
        )
        cursor = connection.cursor()
        logger.info("SEARCHDATA -> Buscando customers no banco de dados...")
        cursor.execute(
            f"SELECT name, email FROM customers WHERE phone IN {list_in}",
            phones,
        )
        customers = cursor.fetchall()
        logger.info("SEARCHDATA -> Customers buscados")
        logger.info(customers)
    except Exception as e:
        logger.error("SEARCHDATA -> Erro")
        logger.error(traceback.format_exc())
        raise e
    finally:
        cursor.close()
        connection.close()

    if len(customers) < 1:
        raise Exception("Nenhum cliente foi encontrado")

    return customers
