from sqlalchemy import create_engine
from models import Base, User


def initialize_db():
    """
    Initialize the SQLite database and create tables based on the models.
    """
    engine = create_engine('sqlite:///expense_tracking_system.db', echo=True)
    Base.metadata.create_all(engine)
    print("Database initialized and tables created.")

if __name__ == "__main__":
    initialize_db()