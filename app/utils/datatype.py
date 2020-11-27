from decimal import Decimal as D
import sqlalchemy.types as types


class SqliteNumeric(types.TypeDecorator):
    impl = types.String

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(types.VARCHAR(100))

    def process_bind_param(self, value, dialect):
        return str(value)

    def process_result_value(self, value, dialect):
        return D(value)

    """
    Use: Sqlalchemy for Decimal Type
    How to use:
        from app.utils.datatype import SqliteNumeric
        Numeric = SqliteNumeric

        monthly_premium = Column(Numeric(13, 2), default=0.00)
    """
