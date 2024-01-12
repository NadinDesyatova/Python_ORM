import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    pk_publisher = sq.Column(sq.Integer, primary_key=True)
    publisher_name = sq.Column(sq.String(length=80), unique=True, nullable=False)


class Book(Base):
    __tablename__ = "book"

    pk_book = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=80), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.pk_publisher"), nullable=False)

    publisher = relationship(Publisher, backref="book")


class Shop(Base):
    __tablename__ = "shop"

    pk_shop = sq.Column(sq.Integer, primary_key=True)
    shop_name = sq.Column(sq.String(length=40), unique=True, nullable=False)


class Stock(Base):
    __tablename__ = "stock"

    
    pk_stock = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer, nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.pk_shop"), nullable=False)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.pk_book"), nullable=False)

    shop = relationship(Shop, backref="stock")
    book = relationship(Book, backref="stock")


class Sale(Base):
    __tablename__ = "sale"

    pk_sale = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float(2), nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.pk_stock"), nullable=False)

    stock = relationship(Stock, backref="sale")


def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
