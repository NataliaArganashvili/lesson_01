from sqlalchemy import create_engine 
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr"
db = create_engine(db_connection_string)

def test_db_connection():
    db = create_engine(db_connection_string)
    name = db.name
    assert name is not None


def test_seleсt():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]

    assert row1["id"] == 111
    assert row1["name"] == "Барбершоп ЦирюльникЪ"

def test_seleсt_by_id():
    db = create_engine(db_connection_string)
    row = db.execute("select * from company where id = 112").fetchall()
    assert row["name"] == "jjkd"

def test_seleсt_by_any_id():
    db = create_engine(db_connection_string)
    sql_statment = text("select * from company where id = :company_id")
    rows = db.execute(sql_statment, company_id=112).fetchall()
    
    assert len(rows) == 1
    assert rows[0]["name"] == "jjkd"

def test_seleсt_by_two_params():
    db = create_engine(db_connection_string)
    sql_statment = text("select * from company where \"is_avtive\" = :is_active and id >= :id")
    rows = db.execute(sql_statment, is_active = True, id=112).fetchall()
    
    assert len(rows) == 3

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into company(\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = 'SkyPro')

def test_update():
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr where id = :id")
    rows = db.execute(sql, descr = 'New descr', id = 1704)