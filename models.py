from sqlalchemy import Boolean, Column, Integer, String
from database import Base, engine


# Note: Setting index=True when defining a column in an ORM model 
# indicates that an index should be created for that column. 
# This can significantly improve the performance of queries that 
# filter or sort results based on this column.
# Additional Information: An index is a database structure that improves 
# the speed of data retrieval operations on a table at the cost of 
# additional storage and some overhead on data modification operations. 
# Indexes are particularly useful for columns that are frequently used 
# in search conditions (WHERE clauses), joins, and ordering (ORDER BY clauses).
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    country = Column(String)
    is_active = Column(Boolean)
    hashed_password = Column(String)
