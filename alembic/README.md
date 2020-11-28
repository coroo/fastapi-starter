# Alembic Migrations

:bulb: Instead of automatically change migrations, it will be more secure enough for using Migrations.

> You can view detail documentation [here](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## First Installation

For first use, please do installation in your command prompt:
```bash
pip install alembic
pip install pydantic[dotenv]
pip install mysqlclient
pip install passlib
PYTHONPATH=. alembic upgrade head
```

## How does it work?

Run your migrations by:
```bash
PYTHONPATH=. alembic upgrade head
```

## Relative migration identifiers

Relative upgrades/downgrades are also supported. To move two versions from the current, a decimal value “+N” can be supplied:
```bash
PYTHONPATH=. alembic upgrade +2
```

Negative values are accepted for downgrades:
```bash
PYTHONPATH=. alembic downgrade -1
```

Relative identifiers may also be in terms of a specific revision. For example, to upgrade to revision ae1027a6acf plus two additional steps:
```bash
PYTHONPATH=. alembic upgrade ae10+2
```

## How to create a new migration file?

With the environment in place we can create a new revision, using `alembic revision`, here the example:
```bash
PYTHONPATH=. alembic revision -m "create items table"
```

### Basic Migration

And you can edit file under folder `alembic > versions`
```python
def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer,
                  primary_key=True,
                  index=True,
                  autoincrement=True),
        sa.Column('title', sa.String(100), primary_key=True, index=True),
        sa.Column('description', sa.String(100), primary_key=True),
        sa.Column('price', sa.Numeric(13, 2), nullable=False),
        sa.Column('owner_id', sa.String(100), primary_key=True),
    )
    pass


def downgrade():
    op.drop_table('items')
    pass
```

### Migration with seeder

```python
def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer,
                  primary_key=True,
                  index=True,
                  autoincrement=True),
        sa.Column('title', sa.String(100), primary_key=True, index=True),
        sa.Column('description', sa.String(100), primary_key=True),
        sa.Column('owner_id', sa.String(100), primary_key=True),
    )

    op.bulk_insert(
        items,
        [
            {
                "id": 1,
                "title": "super-motor-protection",
                "description": "Super Motor Protection",
                "owner_id": 1,
            },
        ]
    )
    pass


def downgrade():
    op.drop_table('items')
    pass
```

### Migration with relationship seeder

```python
# import uuid for id
from app.utils.uuid import generate_uuid

def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.String(100),
                  primary_key=True,
                  index=True,
                  autoincrement=True),
        sa.Column('title', sa.String(100), primary_key=True, index=True),
        sa.Column('description', sa.String(100), primary_key=True),
        sa.Column('owner_id', sa.String(100), primary_key=True),
    )

    # use uuid
    id_random = generate_uuid()
    # use existing relationship data
    conn = op.get_bind()
    res = conn.execute("select id from users WHERE full_name='Admin'")
    results = res.fetchall()
    op.bulk_insert(
        items,
        [
            {
                "id": id_random,
                "title": "super-motor-protection",
                "description": "Super Motor Protection",
                "owner_id": results[0][0],
            },
        ]
    )
    pass


def downgrade():
    op.drop_table('items')
    pass
```