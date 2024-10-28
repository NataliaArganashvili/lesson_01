from sqlalchemy import create_engine 
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr"
db = create_engine(db_connection_string)

new_name = "Natalia's company"
new_descr = 'New descr'

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into company(\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = new_name)
    assert rows["name"] == new_name
    sql = text("delete from company where name = :name")
    rows = db.execute(sql, name = new_name)

def test_update():
    db = create_engine(db_connection_string)
        #создать
    sql = text("insert into company(\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = new_name)
    #изменить
    sql = text("update company set description = :descr where name = :name")
    rows_updated = db.execute(sql, descr = new_descr, name = new_name)
    #проверить
    assert rows_updated["description"] == new_descr
    #удалить
    sql = text("delete from company where name = :name")
    rows = db.execute(sql, name = new_name)

def test_delete():
    db = create_engine(db_connection_string)
    #создать
    sql = text("insert into company(\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = new_name)
    #удалить
    sql = text("delete from company where name = :name")
    rows = db.execute(sql, name = new_name)
    assert rows["name"] is None