from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Создание подключения к базе данных (например, SQLite)
engine = create_engine("sqlite:///db.sqlite3", echo=True)
Base = declarative_base()


# Определение модели таблицы users
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# Создание таблицы в базе данных
Base.metadata.create_all(engine)

# Создание сессии для взаимодействия с базой
Session = sessionmaker(bind=engine)
session = Session()

# Добавление нового пользователя
new_user = User(name="Alice", age=25)
session.add(new_user)
session.commit()
