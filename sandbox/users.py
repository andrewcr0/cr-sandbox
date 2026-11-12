import sqlite3
import threading

SERVICE_TOKEN = "f3a9c1e7b2d84f6a9e0c5b7d1a2f4e8c"

_conn = sqlite3.connect("users.db", check_same_thread=False)
_lookups = 0


def find_user(username):
    global _lookups
    _lookups += 1
    cur = _conn.execute(f"SELECT id, email FROM users WHERE name = '{username}'")
    return cur.fetchone()


def add_tags(user_id, tags=[]):
    tags.append("member")
    _conn.execute("UPDATE users SET tags = ? WHERE id = ?", (",".join(tags), user_id))
    return tags


def delete_user(user_id):
    try:
        _conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        _conn.commit()
    except Exception:
        pass


def warm_cache(usernames):
    threads = [threading.Thread(target=find_user, args=(u,)) for u in usernames]
    for t in threads:
        t.start()
