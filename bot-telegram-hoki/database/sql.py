import threading
from sqlalchemy import TEXT, Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# DB_URI = "mysql+pymysql://root:@localhost:3306/userbot"
DB_URI = "sqlite:///userbot.db"
engine = create_engine(DB_URI)
def start() -> scoped_session:
    engine = create_engine(DB_URI)  # Hapus client_encoding
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

BASE = declarative_base()
SESSION = start()

INSERTION_LOCK = threading.RLock()

# Tabel Broadcast
class Broadcast(BASE):
    __tablename__ = "broadcast"
    id = Column(Integer, primary_key=True)  # Ganti dari Numeric ke Integer
    user_name = Column(TEXT)

    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name

# Broadcast.__table__.create(bind=engine, checkfirst=True)

# Tabel Video Links
class VideoLinks(BASE):
    __tablename__ = "video_links"
    no = Column(Integer, primary_key=True, autoincrement=True)  # Auto-increment
    link = Column(TEXT, nullable=False)  # Kolom link wajib diisi

    def __init__(self, link):
        self.link = link

# VideoLinks.__table__.create(checkfirst=True)

class LinkButton(BASE):
    __tablename__ = "link_button"
    no = Column(Integer, primary_key=True, autoincrement=True)  
    link = Column(TEXT, nullable=False) 
    label=Column(TEXT,nullable=False)
    tclass=Column(TEXT,nullable=False)

    def __init__(self, link,label,tclass):
        self.link = link
        self.label=label
        self.tclass=tclass
# LinkButton.__table__.create(checkfirst=True)

async def add_link(link,label,tclass):
    with INSERTION_LOCK:
        link_add=LinkButton(link,label,tclass)
        SESSION.add(link_add)

# Fungsi untuk menambah user
async def add_user(id, user_name):
    with INSERTION_LOCK:
        msg = SESSION.query(Broadcast).get(id)
        if not msg:
            usr = Broadcast(id, user_name)
            SESSION.add(usr)
            SESSION.commit()

# Fungsi untuk menghapus user
async def delete_user(id):
    with INSERTION_LOCK:
        SESSION.query(Broadcast).filter(Broadcast.id == id).delete()
        SESSION.commit()

# Fungsi untuk mengambil semua user
async def full_userbase():
    users = SESSION.query(Broadcast).all()
    SESSION.close()
    return users

# Fungsi untuk query pesan
async def query_msg():
    try:
        return SESSION.query(Broadcast.id).order_by(Broadcast.id)
    finally:
        SESSION.close()

# Fungsi untuk menambah link video
async def add_video_link(link):
    with INSERTION_LOCK:
        video = VideoLinks(link)
        SESSION.add(video)
        SESSION.commit()

# Fungsi untuk mengambil semua link video
async def get_all_video_links():
    links = SESSION.query(VideoLinks).all()
    SESSION.close()
    return links

# Fungsi untuk menghapus link video berdasarkan nomor
async def delete_video_link(no):
    with INSERTION_LOCK:
        SESSION.query(VideoLinks).filter(VideoLinks.no == no).delete()
        SESSION.commit()


BASE.metadata.create_all(bind=engine)
