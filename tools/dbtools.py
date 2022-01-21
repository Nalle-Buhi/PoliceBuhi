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