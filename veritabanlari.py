import sqlite3

#puan için veritabnı
def setup_db_puan():
    conn = sqlite3.connect("puan_kayit.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS kayit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        puan INTEGER
    )""")
    # Eğer hiç kayıt yoksa başlangıç seviyesini ekle
    c.execute("SELECT COUNT(*) FROM kayit")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO kayit (puan) VALUES (1)")
    conn.commit()
    conn.close()

def yukle_puan():
    conn = sqlite3.connect("puan_kayit.db")
    c = conn.cursor()
    c.execute("SELECT puan FROM kayit ORDER BY id DESC LIMIT 1")
    puan = c.fetchone()[0]
    conn.close()
    return puan

def puan_guncelle(yeni_puan):
    conn = sqlite3.connect("puan_kayit.db")
    c = conn.cursor()
    c.execute("INSERT INTO kayit (puan) VALUES (?)", (yeni_puan,))
    conn.commit()
    conn.close()
    
#seviye için veritabanı
def setup_db_seviye():
    conn = sqlite3.connect("oyun_kayit.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS kayit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        seviye INTEGER
    )""")
    # Eğer hiç kayıt yoksa başlangıç seviyesini ekle
    c.execute("SELECT COUNT(*) FROM kayit")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO kayit (seviye) VALUES (1)")
    conn.commit()
    conn.close()

def yukle_seviye():
    conn = sqlite3.connect("oyun_kayit.db")
    c = conn.cursor()
    c.execute("SELECT seviye FROM kayit ORDER BY id DESC LIMIT 1")
    seviye = c.fetchone()[0]
    conn.close()
    return seviye

def seviye_guncelle(yeni_seviye):
    conn = sqlite3.connect("oyun_kayit.db")
    c = conn.cursor()
    c.execute("INSERT INTO kayit (seviye) VALUES (?)", (yeni_seviye,))
    conn.commit()
    conn.close()

#alinabilecek12 için veritabanı
def setup_db_12():
    conn = sqlite3.connect("alinabilecek12_kayit.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS kayit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alinabilecek12 STRING
    )""")
    # Eğer hiç kayıt yoksa başlangıç seviyesini ekle
    c.execute("SELECT COUNT(*) FROM kayit")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO kayit (alinabilecek12) VALUES (1)")
    conn.commit()
    conn.close()

def yukle_alinabilecek12():
    conn = sqlite3.connect("alinabilecek12_kayit.db")
    c = conn.cursor()
    c.execute("SELECT alinabilecek12 FROM kayit ORDER BY id DESC LIMIT 1")
    seviye = c.fetchone()[0]
    conn.close()
    return seviye

def a_12_guncelle(yeni_12):
    conn = sqlite3.connect("alinabilecek12_kayit.db")
    c = conn.cursor()
    c.execute("INSERT INTO kayit (alinabilecek12) VALUES (?)", (yeni_12,))
    conn.commit()
    conn.close()

#alinabilecek22 için veritabanı
def setup_db_22():
    conn = sqlite3.connect("alinabilecek22_kayit.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS kayit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alinabilecek22 STRING
    )""")
    # Eğer hiç kayıt yoksa başlangıç seviyesini ekle
    c.execute("SELECT COUNT(*) FROM kayit")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO kayit (alinabilecek22) VALUES (1)")
    conn.commit()
    conn.close()

def yukle_alinabilecek22():
    conn = sqlite3.connect("alinabilecek22_kayit.db")
    c = conn.cursor()
    c.execute("SELECT alinabilecek22 FROM kayit ORDER BY id DESC LIMIT 1")
    seviye = c.fetchone()[0]
    conn.close()
    return seviye

def a_22_guncelle(yeni_22):
    conn = sqlite3.connect("alinabilecek22_kayit.db")
    c = conn.cursor()
    c.execute("INSERT INTO kayit (alinabilecek22) VALUES (?)", (yeni_22,))
    conn.commit()
    conn.close()

#alinabilecek32 için veritabanı
def setup_db_32():
    conn = sqlite3.connect("alinabilecek32_kayit.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS kayit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alinabilecek32 STRING
    )""")
    # Eğer hiç kayıt yoksa başlangıç seviyesini ekle
    c.execute("SELECT COUNT(*) FROM kayit")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO kayit (alinabilecek32) VALUES (1)")
    conn.commit()
    conn.close()

def yukle_alinabilecek32():
    conn = sqlite3.connect("alinabilecek32_kayit.db")
    c = conn.cursor()
    c.execute("SELECT alinabilecek32 FROM kayit ORDER BY id DESC LIMIT 1")
    seviye = c.fetchone()[0]
    conn.close()
    return seviye

def a_32_guncelle(yeni_32):
    conn = sqlite3.connect("alinabilecek32_kayit.db")
    c = conn.cursor()
    c.execute("INSERT INTO kayit (alinabilecek32) VALUES (?)", (yeni_32,))
    conn.commit()
    conn.close()

#alinabilecek42 için veritabanı
def setup_db_42():
    conn = sqlite3.connect("alinabilecek42_kayit.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS kayit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alinabilecek42 STRING
    )""")
    # Eğer hiç kayıt yoksa başlangıç seviyesini ekle
    c.execute("SELECT COUNT(*) FROM kayit")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO kayit (alinabilecek42) VALUES (1)")
    conn.commit()
    conn.close()

def yukle_alinabilecek42():
    conn = sqlite3.connect("alinabilecek42_kayit.db")
    c = conn.cursor()
    c.execute("SELECT alinabilecek42 FROM kayit ORDER BY id DESC LIMIT 1")
    seviye = c.fetchone()[0]
    conn.close()
    return seviye

def a_42_guncelle(yeni_42):
    conn = sqlite3.connect("alinabilecek42_kayit.db")
    c = conn.cursor()
    c.execute("INSERT INTO kayit (alinabilecek42) VALUES (?)", (yeni_42,))
    conn.commit()
    conn.close()

#ses için veritabanı
def setup_db_ses():
    conn = sqlite3.connect("ses_kayit.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS kayit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ses STRING
    )""")
    # Eğer hiç kayıt yoksa başlangıç seviyesini ekle
    c.execute("SELECT COUNT(*) FROM kayit")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO kayit (ses) VALUES (1)")
    conn.commit()
    conn.close()

def yukle_ses():
    conn = sqlite3.connect("ses_kayit.db")
    c = conn.cursor()
    c.execute("SELECT ses FROM kayit ORDER BY id DESC LIMIT 1")
    seviye = c.fetchone()[0]
    conn.close()
    return seviye

def ses_guncelle(yeni_ses):
    conn = sqlite3.connect("ses_kayit.db")
    c = conn.cursor()
    c.execute("INSERT INTO kayit (ses) VALUES (?)", (yeni_ses,))
    conn.commit()
    conn.close()

#basim_artisi için veritabanı
def setup_db_basim_artisi():
    conn = sqlite3.connect("basim_artisi_kayit.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS kayit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        basim_artisi INTEGER
    )""")
    # Eğer hiç kayıt yoksa başlangıç seviyesini ekle
    c.execute("SELECT COUNT(*) FROM kayit")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO kayit (basim_artisi) VALUES (1)")
    conn.commit()
    conn.close()

def yukle_basim_artisi():
    conn = sqlite3.connect("basim_artisi_kayit.db")
    c = conn.cursor()
    c.execute("SELECT basim_artisi FROM kayit ORDER BY id DESC LIMIT 1")
    seviye = c.fetchone()[0]
    conn.close()
    return seviye

def basim_artisi_guncelle(yeni_basim_artisi):
    conn = sqlite3.connect("basim_artisi_kayit.db")
    c = conn.cursor()
    c.execute("INSERT INTO kayit (basim_artisi) VALUES (?)", (yeni_basim_artisi,))
    conn.commit()
    conn.close()