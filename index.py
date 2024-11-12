from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///books.db', echo=True)

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)


Base.metadata.create_all(engine)

def add_books(session):
    books = [
        Book(title=" The Adventures of Tom Sawyer ", year=1876),
        Book(title="Na Drini Ćuprija", year=1945),
        Book(title="Gulliverova Putovanja", year=1726),
        Book(title="Oranje Mora",year=2016),
        Book(title="Zasto Tone Venecija",year=2012)
    ]
    session.add_all(books)
    session.commit()

def read_books(session):
    books = session.query(Book).all()
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Year: {book.year}")

Session = sessionmaker(bind=engine)
session = Session()


add_books(session)


read_books(session)


session.close()
