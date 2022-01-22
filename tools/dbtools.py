import sqlite3


async def insert_log_db(guild_id, channel_id, enabled, table):
    con = sqlite3.connect("dbs/config.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM " + table + " WHERE guild_id = ?", (guild_id,))
    exists = cur.fetchone()
    if exists:
        cur.execute("UPDATE " + table + " SET guild_id = ?, channel_id = ?, enabled = ?", (guild_id, channel_id, enabled))
    else:
        cur.execute("INSERT INTO " + table + " VALUES (?,?,?)", (guild_id, channel_id, enabled))
    con.commit()
    con.close()

async def log_config_reader(guild_id, table):
    con = sqlite3.connect("dbs/config.db")
    cur = con.cursor()
    cur.execute(f"SELECT channel_id FROM " + table + " WHERE guild_id = ? AND enabled = ?", (guild_id, 1))
    enabled = cur.fetchone()
    if enabled:
        return enabled[0]
    else:
        return None

async def insert_warn(guild_id, user_id, giver_id, reason, date):
    con = sqlite3.connect("dbs/mod.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO warns values (?,?,?,?,?,?)""", (None, guild_id, user_id, giver_id, reason, date))
    con.commit()
    con.close()

async def list_warns(guild_id, user_id):
    con = sqlite3.connect("dbs/mod.db")
    cur = con.cursor()
    cur.execute("""SELECT * FROM warns WHERE guild_id = ? AND user_id = ?""", (guild_id, user_id))
    results = cur.fetchall()
    return results
    con.close()