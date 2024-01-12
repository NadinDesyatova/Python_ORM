import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale


connection_driver = 'postgresql'
user='postgres'
password=''
server_name = 'localhost'
server_port = '5432'
db_name = 'book_sales_db'


DSN = f"{connection_driver}://{user}:{password}@{server_name}:{server_port}/{db_name}"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)


# def read_data_file(file_path):
#     with open(file_path, "r") as f:
#         data = json.load(f)
    

# def insert_data(session, data):
#     for item in data:
#         if item["model"] == "publisher":
#             session.add(Publisher(pk_publisher=item["pk"], publisher_name=item["fields"]["name"]))
#             session.commit()
#         elif item["model"] == "book":
#             session.add(Book(pk_book=item["pk"], title=item["fields"]["title"], id_publisher=item["fields"]["id_publisher"]))
#             session.commit()
#         elif item["model"] == "shop":
#             session.add(Shop(pk_shop=item["pk"], shop_name=item["fields"]["name"]))
#             session.commit()
#         elif item["model"] == "stock":
#             session.add(Stock(
#                 pk_stock=item["pk"], 
#                 id_shop=item["fields"]["id_shop"], 
#                 id_book=item["fields"]["id_book"], 
#                 count=item["fields"]["count"]
#             ))
#             session.commit()
#         elif item["model"] == "sale":
#             session.add(Sale(
#                 pk_sale=item["pk"], 
#                 price=item["fields"]["price"],
#                 date_sale=item["fields"]["date_sale"],
#                 id_stock=item["fields"]["id_stock"]
#             ))
#             session.commit()


# def get_book_sales_information(session, required_publisher_name=None, required_publisher_id=None):
#     subq_1 = session.query(Book).join(Publisher.book).filter(
#         Publisher.publisher_name == required_publisher_name or Publisher.pk_publisher == required_publisher_id
#     ).subquery("publisher_book")
#     subq_2 = session.query(Stock).join(subq_1, Stock.id_book == subq_1.c.pk_book).subquery("stock_book")
#     q = session.query(Sale).join(subq_2, Sale.id_stock == subq_2.c.pk_stock)
#     for item in q.all():
#         print(f'{item.title} | {item.publisher_name} | {item.price} | {item.date_sale}\n') 


# file = "tests_data.json"
# data_to_insert = read_data_file(file)


# Session = sessionmaker(bind=engine)
# current_session = Session()
    
# insert_data(current_session, data_to_insert)

# current_publisher = input("Введите имя или идентификатор издателя: ")

# get_book_sales_information(current_session, current_publisher, current_publisher)

# current_session.close()


# if __name__ == '__main__':
#     current_connection_driver= input("Введите название драйвера подключения: ")
#     current_user = input("Введите имя пользователя: ")
#     current_user_password = input("Введите пароль: ")
#     current_server_name = input("Введите название сервера: ")
#     current_server_port = input("Порт подключения: ")
#     current_db_name = input("Введите название базы данных: ")
