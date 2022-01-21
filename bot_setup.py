import sqlite3

config_queries = ["""
    CREATE TABLE IF NOT EXISTS del_log_config (
        guild_id integer,
        channel_id integer,
        enabled bit
        )
    """, 
    """
    CREATE TABLE IF NOT EXISTS edit_log_config (
        guild_id integer,
        channel_id integer,
        enabled bit
        )
    """]

mod_queries = ["""
    CREATE TABLE IF NOT EXISTS warns (
        user_id integer,
        giver_id integer,
        reason text,
        date date
    )
"""]


def config_tables():
    con = sqlite3.connect("./dbs/config.db")
    cur = con.cursor()
    for query in config_queries:
        cur.execute(query)
    con.close() 

def mod_tables():
    con = sqlite3.connect("./dbs/mod.db")
    cur = con.cursor()
    for query in mod_queries:
        cur.execute(query)
    con.close() 

def create_tables():
    """create needed tables for a functioning bot. Used when starting up the bot"""
    config_tables()
    mod_tables()