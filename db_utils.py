import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Create database engine
engine = create_engine(DATABASE_URL)

# Create base class for models
Base = declarative_base()

# Create a session factory
Session = sessionmaker(bind=engine)

# Define the Kaomoji model
class Kaomoji(Base):
    __tablename__ = 'kaomoji_history'
    
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    
    def __repr__(self):
        return f"<Kaomoji(text='{self.text}', category='{self.category}')>"

# Create the tables in the database
def init_db():
    Base.metadata.create_all(engine)

# Functions for database operations
def save_kaomoji(text, category):
    """Save a kaomoji to the database"""
    session = Session()
    try:
        kaomoji = Kaomoji(text=text, category=category)
        session.add(kaomoji)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error saving kaomoji: {e}")
        return False
    finally:
        session.close()

def get_all_kaomoji():
    """Get all kaomoji from the database, ordered by creation time (newest first)"""
    session = Session()
    try:
        kaomojis = session.query(Kaomoji).order_by(Kaomoji.created_at.desc()).all()
        return kaomojis
    except Exception as e:
        print(f"Error retrieving kaomoji: {e}")
        return []
    finally:
        session.close()

def search_kaomoji(search_term):
    """Search for kaomoji in the database"""
    session = Session()
    try:
        # Search in text or category
        kaomojis = session.query(Kaomoji).filter(
            (Kaomoji.text.ilike(f"%{search_term}%")) | 
            (Kaomoji.category.ilike(f"%{search_term}%"))
        ).order_by(Kaomoji.created_at.desc()).all()
        return kaomojis
    except Exception as e:
        print(f"Error searching kaomoji: {e}")
        return []
    finally:
        session.close()

def clear_history():
    """Clear all kaomoji history"""
    session = Session()
    try:
        session.query(Kaomoji).delete()
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error clearing history: {e}")
        return False
    finally:
        session.close()

# Initialize the database
init_db()