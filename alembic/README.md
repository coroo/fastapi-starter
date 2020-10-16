# Alembic Migrations

:bulb: Instead of automatically change migrations, it will be more secure enough for using Migrations.

> You can view detail documentation [here](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## How does it work?

Run your migrations by:
```
PYTHONPATH=. alembic upgrade head
```

## Relative migration identifiers

Relative upgrades/downgrades are also supported. To move two versions from the current, a decimal value “+N” can be supplied:
```
alembic upgrade +2
```

Negative values are accepted for downgrades:
```
PYTHONPATH=. alembic downgrade -1
```

Relative identifiers may also be in terms of a specific revision. For example, to upgrade to revision ae1027a6acf plus two additional steps:
```
PYTHONPATH=. alembic upgrade ae10+2
```

## How to create a new migration file?

With the environment in place we can create a new revision, using `alembic revision`, here the example:
```
alembic revision -m "create item table"
```