import databases
import sqlalchemy
from datetime import datetime


DATABASE_URL = "sqlite:///./notebooks.db"
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

notebooks = sqlalchemy.Table(
    "notebooks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("url", sqlalchemy.String),
    sqlalchemy.Column("visited_at", sqlalchemy.DateTime, default=datetime.now),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("disp_inch", sqlalchemy.Float),
    sqlalchemy.Column("cpu_hhz", sqlalchemy.Float),
    sqlalchemy.Column("ram_gb", sqlalchemy.Integer),
    sqlalchemy.Column("ssd_gb", sqlalchemy.Integer),
    sqlalchemy.Column("price_rub", sqlalchemy.Integer),
    sqlalchemy.Column("rank", sqlalchemy.Float),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
conn = engine.connect()


def insert_spec(list2db):
    for specification in list2db:
        ins = notebooks.insert().values(url=specification['url'], name=specification['name'],
                                        cpu_hhz=specification['cpu_hhz'], ram_gb=specification['ram_gb'],
                                        ssd_gb=specification['ssd_gb'], disp_inch=specification['disp_inch'],
                                        price_rub=specification['price_rub'], rank=specification['rank'])
        conn.execute(ins)
