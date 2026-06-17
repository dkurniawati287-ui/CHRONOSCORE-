import streamlit as st
import sqlite3
from datetime import datetime, timedelta, date
import pandas as pd
import matplotlib.pyplot as plt
import random
import time
import io
import base64
import os

# ─── CONFIG PAGE STREAMLIT ────────────────────────────────────────────────────
st.set_page_config(page_title="Task Priority Dashboard", layout="wide")

# ─── KATEGORI ─────────────────────────────────────────────────────────────────
KATEGORI_LIST = ["Akademik", "Non Akademik"]

# ─── PALET WARNA ──────────────────────────────────────────────────────────────
FAIRY_LIGHTS = "#FFDDBD"
BLUE_TOURMALIN = "#5FBBEF"
BLUE_HEPATICA = "#5C71DD"
CANDIED_BLUEBERRY = "#522196"
BANAISAGI_PURPLE = "#CD2382"
PINK_KATYDID = "#FF62BB"

BG_MAIN = "#120820"
TITLE_CLR = PINK_KATYDID

KATEGORI_COLORS = {
    "Akademik": BLUE_TOURMALIN,
    "Non Akademik": PINK_KATYDID,
}

DB_NAME = "tasks.db"

# ─── LEVEL THRESHOLDS ────────────────────────────────────────────────────────
LEVEL_THRESHOLDS = {
    1: 0, 2: 100, 3: 250, 4: 450, 5: 700,
    6: 1000, 7: 1350, 8: 1750, 9: 2200, 10: 2700,
    11: 3250, 12: 3850, 13: 4500, 14: 5200, 15: 5950,
    16: 6750, 17: 7600, 18: 8500, 19: 9450, 20: 10500
}

BADGE_REQUIREMENTS = {
    "Task Starter": "Selesaikan 5 tugas",
    "Task Master": "Selesaikan 25 tugas",
    "Task Legend": "Selesaikan 50 tugas",
    "Speed Demon": "Selesaikan 10 tugas dalam seminggu",
    "Academic Star": "Selesaikan 10 tugas Akademik",
    "Non-Academic Star": "Selesaikan 10 tugas Non-Akademik",
    "High Priority": "Selesaikan 5 tugas High Priority",
    "Perfect Streak": "Selesaikan tugas 7 hari berturut-turut",
    "Pomodoro Master": "Selesaikan 50 sesi Pomodoro",
    "Focus Champion": "Selesaikan 100 sesi Pomodoro",
}


# ─── FUNGSI MIGRASI DATABASE ──────────────────────────────────────────────
def migrate_database():
    """Menambahkan kolom yang hilang ke database jika diperlukan"""
    if not os.path.exists(DB_NAME):
        return

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    try:
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_stats'")
        if c.fetchone():
            c.execute("PRAGMA table_info(user_stats)")
            columns = [col[1] for col in c.fetchall()]

            if 'xp' not in columns:
                c.execute("ALTER TABLE user_stats ADD COLUMN xp INTEGER DEFAULT 0")
            if 'level' not in columns:
                c.execute("ALTER TABLE user_stats ADD COLUMN level INTEGER DEFAULT 1")
            if 'tasks_completed' not in columns:
                c.execute("ALTER TABLE user_stats ADD COLUMN tasks_completed INTEGER DEFAULT 0")
            if 'current_streak' not in columns:
                c.execute("ALTER TABLE user_stats ADD COLUMN current_streak INTEGER DEFAULT 0")
            if 'longest_streak' not in columns:
                c.execute("ALTER TABLE user_stats ADD COLUMN longest_streak INTEGER DEFAULT 0")
            if 'last_completion_date' not in columns:
                c.execute("ALTER TABLE user_stats ADD COLUMN last_completion_date TEXT")
            if 'pomodoro_sessions' not in columns:
                c.execute("ALTER TABLE user_stats ADD COLUMN pomodoro_sessions INTEGER DEFAULT 0")
            if 'total_focus_minutes' not in columns:
                c.execute("ALTER TABLE user_stats ADD COLUMN total_focus_minutes INTEGER DEFAULT 0")

            c.execute("SELECT COUNT(*) FROM user_stats")
            if c.fetchone()[0] == 0:
                c.execute("INSERT INTO user_stats (xp, level, tasks_completed, pomodoro_sessions) VALUES (0, 1, 0, 0)")

            conn.commit()
    except Exception as e:
        print(f"❌ Error migrasi: {e}")
    finally:
        conn.close()


# ─── DATABASE FUNCTIONS ──────────────────────────────────────────────────────
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (
                     id
                     INTEGER
                     PRIMARY
                     KEY
                     AUTOINCREMENT,
                     name
                     TEXT
                     NOT
                     NULL,
                     estimated_minutes
                     INTEGER,
                     deadline
                     TEXT,
                     priority
                     TEXT,
                     category
                     TEXT,
                     difficulty
                     INTEGER
                     DEFAULT
                     3,
                     status
                     TEXT
                     DEFAULT
                     'pending',
                     created_at
                     TEXT
                     DEFAULT
                     CURRENT_TIMESTAMP,
                     completed_at
                     TEXT
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS user_stats
                 (
                     id
                     INTEGER
                     PRIMARY
                     KEY
                     AUTOINCREMENT,
                     xp
                     INTEGER
                     DEFAULT
                     0,
                     level
                     INTEGER
                     DEFAULT
                     1,
                     tasks_completed
                     INTEGER
                     DEFAULT
                     0,
                     current_streak
                     INTEGER
                     DEFAULT
                     0,
                     longest_streak
                     INTEGER
                     DEFAULT
                     0,
                     last_completion_date
                     TEXT,
                     pomodoro_sessions
                     INTEGER
                     DEFAULT
                     0,
                     total_focus_minutes
                     INTEGER
                     DEFAULT
                     0
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS badges
                 (
                     id
                     INTEGER
                     PRIMARY
                     KEY
                     AUTOINCREMENT,
                     name
                     TEXT
                     UNIQUE,
                     earned_date
                     TEXT,
                     description
                     TEXT
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS quiz_scores
                 (
                     id
                     INTEGER
                     PRIMARY
                     KEY
                     AUTOINCREMENT,
                     score
                     INTEGER,
                     total_questions
                     INTEGER,
                     date
                     TEXT,
                     category
                     TEXT
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS pomodoro_history
                 (
                     id
                     INTEGER
                     PRIMARY
                     KEY
                     AUTOINCREMENT,
                     task_id
                     INTEGER,
                     task_name
                     TEXT,
                     duration
                     INTEGER,
                     start_time
                     TEXT,
                     end_time
                     TEXT,
                     completed
                     BOOLEAN
                     DEFAULT
                     1
                 )''')

    c.execute("SELECT COUNT(*) FROM user_stats")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO user_stats (xp, level, tasks_completed, pomodoro_sessions) VALUES (0, 1, 0, 0)")

    conn.commit()
    conn.close()


# ─── CORE FUNCTIONS ──────────────────────────────────────────────────────────
def hitung_skor(difficulty, deadline_date):
    difficulty_score = (difficulty / 5) * 50

    if deadline_date:
        try:
            if isinstance(deadline_date, (date, datetime)):
                dl = deadline_date
            else:
                dl = datetime.strptime(str(deadline_date), "%Y-%m-%d").date()
            if isinstance(dl, datetime):
                dl = dl.date()
            hari_tersisa = (dl - date.today()).days
            if hari_tersisa < 0:
                urgency_score = 50
            elif hari_tersisa == 0:
                urgency_score = 50
            elif hari_tersisa <= 3:
                urgency_score = 40
            elif hari_tersisa <= 7:
                urgency_score = 25
            elif hari_tersisa <= 14:
                urgency_score = 15
            else:
                urgency_score = 5
        except:
            urgency_score = 0
    else:
        urgency_score = 0

    skor = round(difficulty_score + urgency_score)
    if skor >= 65:
        priority = "High"
    elif skor >= 35:
        priority = "Medium"
    else:
        priority = "Low"
    return skor, priority


def add_task(name, minutes, deadline, category, difficulty):
    skor, priority = hitung_skor(difficulty, deadline)
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO tasks (name, estimated_minutes, deadline, priority, category, difficulty, status)
                 VALUES (?, ?, ?, ?, ?, ?, 'pending')''',
              (name, minutes, str(deadline) if deadline else None, priority, category, difficulty))
    conn.commit()
    conn.close()


def get_all_tasks_df():
    conn = sqlite3.connect(DB_NAME)
    try:
        df = pd.read_sql_query(
            "SELECT id, name, estimated_minutes, deadline, priority, category, difficulty, status, completed_at FROM tasks ORDER BY id DESC",
            conn)
    except:
        df = pd.DataFrame()
    conn.close()
    return df


def clear_all_tasks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()


def complete_task_by_id(task_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        try:
            c.execute("SELECT xp FROM user_stats LIMIT 1")
        except sqlite3.OperationalError:
            c.execute("ALTER TABLE user_stats ADD COLUMN xp INTEGER DEFAULT 0")
            c.execute("ALTER TABLE user_stats ADD COLUMN level INTEGER DEFAULT 1")
            c.execute("ALTER TABLE user_stats ADD COLUMN tasks_completed INTEGER DEFAULT 0")
            c.execute("ALTER TABLE user_stats ADD COLUMN current_streak INTEGER DEFAULT 0")
            c.execute("ALTER TABLE user_stats ADD COLUMN longest_streak INTEGER DEFAULT 0")
            c.execute("ALTER TABLE user_stats ADD COLUMN last_completion_date TEXT")
            c.execute("ALTER TABLE user_stats ADD COLUMN pomodoro_sessions INTEGER DEFAULT 0")
            c.execute("ALTER TABLE user_stats ADD COLUMN total_focus_minutes INTEGER DEFAULT 0")

            c.execute("SELECT COUNT(*) FROM user_stats")
            if c.fetchone()[0] == 0:
                c.execute("INSERT INTO user_stats (xp, level, tasks_completed, pomodoro_sessions) VALUES (0, 1, 0, 0)")

            conn.commit()

        c.execute("SELECT status, priority, difficulty FROM tasks WHERE id=?", (task_id,))
        row = c.fetchone()
        if row is None:
            return False, "ID tidak ditemukan"
        if row[0] != 'pending':
            return False, "Tugas sudah selesai"

        now = datetime.now().isoformat()
        c.execute("UPDATE tasks SET status='completed', completed_at=? WHERE id=? AND status='pending'",
                  (now, task_id))

        priority = row[1]
        difficulty = row[2]
        xp_reward = 10 + {"High": 15, "Medium": 10, "Low": 5}.get(priority, 5) + difficulty * 2

        c.execute("UPDATE user_stats SET tasks_completed = tasks_completed + 1 WHERE id=1")

        c.execute("SELECT xp, level FROM user_stats WHERE id=1")
        current_xp, current_level = c.fetchone()
        new_xp = current_xp + xp_reward
        new_level = current_level
        while new_level in LEVEL_THRESHOLDS and new_xp >= LEVEL_THRESHOLDS.get(new_level + 1, float('inf')):
            new_level += 1
        c.execute("UPDATE user_stats SET xp=?, level=? WHERE id=1", (new_xp, new_level))

        today = date.today()
        c.execute("SELECT last_completion_date, current_streak, longest_streak FROM user_stats WHERE id=1")
        result = c.fetchone()
        if result:
            last_date, current_streak, longest_streak = result
            if last_date:
                try:
                    last_date = datetime.strptime(last_date, "%Y-%m-%d").date()
                except:
                    last_date = None
            if last_date == today:
                pass
            elif last_date == today - timedelta(days=1) if last_date else False:
                current_streak += 1
                if current_streak > longest_streak:
                    longest_streak = current_streak
            else:
                current_streak = 1
            c.execute("UPDATE user_stats SET last_completion_date=?, current_streak=?, longest_streak=? WHERE id=1",
                      (today.isoformat(), current_streak, longest_streak))

        conn.commit()

        new_badges = check_badges()

        success_message = f"✅ Tugas selesai! +{xp_reward} XP"
        if new_badges:
            success_message += f"\n🏆 Badge baru: {', '.join(new_badges)}!"

        return True, success_message
    except Exception as e:
        return False, f"Error: {str(e)}"
    finally:
        conn.close()


def recalc_all_scores():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("SELECT id, difficulty, deadline FROM tasks WHERE status='pending'")
        for tid, diff, dl in c.fetchall():
            skor, prio = hitung_skor(diff or 3, dl)
            c.execute("UPDATE tasks SET priority=? WHERE id=?", (prio, tid))
        conn.commit()
    except:
        pass
    finally:
        conn.close()


def insert_sample_tasks():
    df = get_all_tasks_df()
    if df.empty:
        sample = [
            ("Presentasi Akhir", 75, "2026-06-14", "Akademik", 5),
            ("Belajar UAP", 100, "2026-06-12", "Akademik", 4),
            ("Menulis Ilmiah", 60, "2026-06-10", "Akademik", 3),
            ("Video Resume FPO", 90, "2026-06-13", "Non Akademik", 3),
            ("Notulensi", 30, "2026-06-09", "Non Akademik", 2),
        ]
        for nama, menit, deadline, kat, diff in sample:
            add_task(nama, menit, deadline, kat, diff)


# ─── BADGE SYSTEM ────────────────────────────────────────────────────────────
def get_user_stats():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute(
            "SELECT xp, level, tasks_completed, current_streak, longest_streak, pomodoro_sessions, total_focus_minutes FROM user_stats WHERE id=1")
        result = c.fetchone()
        if result:
            return {
                "xp": result[0], "level": result[1], "tasks_completed": result[2],
                "current_streak": result[3] or 0, "longest_streak": result[4] or 0,
                "pomodoro_sessions": result[5] or 0, "total_focus_minutes": result[6] or 0
            }
    except:
        pass
    finally:
        conn.close()
    return {"xp": 0, "level": 1, "tasks_completed": 0, "current_streak": 0,
            "longest_streak": 0, "pomodoro_sessions": 0, "total_focus_minutes": 0}


def get_earned_badges():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("SELECT name, earned_date, description FROM badges ORDER BY earned_date DESC")
        result = c.fetchall()
        return result
    except:
        return []
    finally:
        conn.close()


def award_badge(badge_name, description):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO badges (name, earned_date, description) VALUES (?, ?, ?)",
                  (badge_name, datetime.now().isoformat(), description))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    except:
        return False
    finally:
        conn.close()


def check_badges():
    stats = get_user_stats()
    earned_badges = [b[0] for b in get_earned_badges()]
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    try:
        c.execute("SELECT category, priority, completed_at FROM tasks WHERE status='completed'")
        completed_tasks = c.fetchall()

        academic_count = sum(1 for t in completed_tasks if t[0] == "Akademik")
        non_academic_count = sum(1 for t in completed_tasks if t[0] == "Non Akademik")
        high_priority_count = sum(1 for t in completed_tasks if t[1] == "High")

        week_ago = datetime.now() - timedelta(days=7)
        weekly_count = sum(
            1 for t in completed_tasks if t[2] and datetime.strptime(t[2], "%Y-%m-%dT%H:%M:%S.%f") > week_ago)
    except:
        academic_count = non_academic_count = high_priority_count = weekly_count = 0
    finally:
        conn.close()

    new_badges = []

    badge_checks = [
        (stats["tasks_completed"] >= 5, "Task Starter"),
        (stats["tasks_completed"] >= 25, "Task Master"),
        (stats["tasks_completed"] >= 50, "Task Legend"),
        (academic_count >= 10, "Academic Star"),
        (non_academic_count >= 10, "Non-Academic Star"),
        (high_priority_count >= 5, "High Priority"),
        (weekly_count >= 10, "Speed Demon"),
        (stats["current_streak"] >= 7, "Perfect Streak"),
        (stats["pomodoro_sessions"] >= 50, "Pomodoro Master"),
        (stats["pomodoro_sessions"] >= 100, "Focus Champion"),
    ]

    for condition, badge_name in badge_checks:
        if condition and badge_name not in earned_badges:
            if award_badge(badge_name, BADGE_REQUIREMENTS[badge_name]):
                new_badges.append(badge_name)

    return new_badges


# ─── POMODORO FUNCTIONS ──────────────────────────────────────────────────────
def save_pomodoro_session(task_name, duration, task_id=None):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        now = datetime.now().isoformat()
        c.execute("""INSERT INTO pomodoro_history
                         (task_id, task_name, duration, start_time, end_time, completed)
                     VALUES (?, ?, ?, ?, ?, 1)""",
                  (task_id, task_name, duration, now, now))
        c.execute(
            "UPDATE user_stats SET pomodoro_sessions = pomodoro_sessions + 1, total_focus_minutes = total_focus_minutes + ? WHERE id=1",
            (duration,))
        conn.commit()
    except:
        pass
    finally:
        conn.close()
    xp_reward = 5 + duration // 5
    add_xp_direct(xp_reward)
    check_badges()
    return xp_reward


def add_xp_direct(xp_amount):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("SELECT xp, level FROM user_stats WHERE id=1")
        current_xp, current_level = c.fetchone()
        new_xp = current_xp + xp_amount
        new_level = current_level
        while new_level in LEVEL_THRESHOLDS and new_xp >= LEVEL_THRESHOLDS.get(new_level + 1, float('inf')):
            new_level += 1
        c.execute("UPDATE user_stats SET xp=?, level=? WHERE id=1", (new_xp, new_level))
        conn.commit()
    except:
        pass
    finally:
        conn.close()


def get_pomodoro_stats():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("SELECT COUNT(*), SUM(duration) FROM pomodoro_history")
        total_sessions, total_minutes = c.fetchone()
        today = date.today().isoformat()
        c.execute("SELECT COUNT(*), SUM(duration) FROM pomodoro_history WHERE date(start_time) = ?", (today,))
        today_sessions, today_minutes = c.fetchone()
        return {
            "total_sessions": total_sessions or 0,
            "total_minutes": total_minutes or 0,
            "today_sessions": today_sessions or 0,
            "today_minutes": today_minutes or 0
        }
    except:
        return {"total_sessions": 0, "total_minutes": 0, "today_sessions": 0, "today_minutes": 0}
    finally:
        conn.close()


# ─── QUIZ FUNCTIONS ──────────────────────────────────────────────────────────
QUIZ_QUESTIONS = {
    "Science": [
        {"question": "Apa yang dimaksud dengan fotosintesis?",
         "options": ["Proses pembuatan makanan dari cahaya", "Proses pernapasan tumbuhan",
                     "Proses pembelahan sel", "Proses penguapan air"],
         "correct": 0,
         "explanation": "Fotosintesis adalah proses pembuatan makanan oleh tumbuhan menggunakan energi cahaya."},
        {"question": "Berapakah jumlah planet dalam tata surya kita?",
         "options": ["6", "7", "8", "9"], "correct": 2,
         "explanation": "Tata surya kita memiliki 8 planet."},
        {"question": "Apa yang menyebabkan terjadinya siang dan malam?",
         "options": ["Rotasi Bumi", "Revolusi Bumi", "Gravitasi Bulan", "Pergeseran Sumbu"],
         "correct": 0, "explanation": "Rotasi Bumi pada sumbunya menyebabkan siang dan malam."}
    ],
    "General": [
        {"question": "Ibu kota Indonesia adalah...",
         "options": ["Jakarta", "Surabaya", "Bandung", "Medan"], "correct": 0,
         "explanation": "Jakarta adalah ibu kota Indonesia."},
        {"question": "Negara mana yang memiliki populasi terbanyak di dunia?",
         "options": ["India", "China", "USA", "Indonesia"], "correct": 0,
         "explanation": "India saat ini memiliki populasi terbanyak di dunia."},
        {"question": "Apa bahasa pemrograman yang paling populer untuk AI?",
         "options": ["Python", "Java", "C++", "JavaScript"], "correct": 0,
         "explanation": "Python adalah bahasa pemrograman yang paling populer untuk AI."}
    ],
    "Math": [
        {"question": "Berapakah hasil dari 7 × 8 + 6?",
         "options": ["62", "64", "66", "68"], "correct": 0,
         "explanation": "7 × 8 = 56, lalu 56 + 6 = 62."},
        {"question": "Apa akar kuadrat dari 144?",
         "options": ["10", "11", "12", "13"], "correct": 2,
         "explanation": "Akar kuadrat dari 144 adalah 12."},
        {"question": "Berapa sudut dalam segitiga sama sisi?",
         "options": ["45°", "60°", "90°", "120°"], "correct": 1,
         "explanation": "Segitiga sama sisi memiliki sudut 60° di setiap sisinya."}
    ]
}


def get_quiz_questions(category=None):
    if category and category in QUIZ_QUESTIONS:
        return random.sample(QUIZ_QUESTIONS[category], min(3, len(QUIZ_QUESTIONS[category])))
    all_questions = []
    for q_list in QUIZ_QUESTIONS.values():
        all_questions.extend(q_list)
    return random.sample(all_questions, min(5, len(all_questions)))


def save_quiz_score(score, total, category):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO quiz_scores (score, total_questions, date, category) VALUES (?, ?, ?, ?)",
                  (score, total, datetime.now().isoformat(), category))
        conn.commit()
    except:
        pass
    finally:
        conn.close()


def get_quiz_stats():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("SELECT AVG(score * 1.0 / total_questions * 100), COUNT(*) FROM quiz_scores")
        avg_score, total_attempts = c.fetchone()
        return avg_score or 0, total_attempts or 0
    except:
        return 0, 0
    finally:
        conn.close()


# ─── HELPER FUNCTIONS ────────────────────────────────────────────────────────
def bintang(n):
    return "★" * n + "☆" * (5 - n)


def score_color(skor):
    if skor >= 65: return BANAISAGI_PURPLE
    if skor >= 35: return BLUE_HEPATICA
    return BLUE_TOURMALIN


def norm_kat(k):
    if not k: return "Non Akademik"
    kl = k.strip().lower()
    if "non" in kl or kl in ["pribadi", "olahraga", "organisasi"]:
        return "Non Akademik"
    return "Akademik"


def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', facecolor=BG_MAIN, dpi=110)
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode()
    plt.close(fig)
    return b64


# ─── CSS ─────────────────────────────────────────────────────────────────────
def get_css():
    return f"""
    <style>
        .stApp {{
            background: linear-gradient(135deg, {BG_MAIN} 0%, #1e0a3c 60%, #2a0a2e 100%) !important;
            color: {FAIRY_LIGHTS};
            font-family: 'Poppins', sans-serif;
        }}
        .cs-title {{
            font-family: 'Playfair Display', serif;
            font-size: 3.5em;
            font-weight: 800;
            text-align: center;
            background: linear-gradient(90deg, {BLUE_TOURMALIN}, {PINK_KATYDID}, {BLUE_HEPATICA});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
            filter: drop-shadow(0 0 18px {BANAISAGI_PURPLE});
        }}
        .cs-sub {{
            text-align: center;
            font-style: italic;
            color: {BLUE_TOURMALIN};
            margin-bottom: 20px;
            border-top: 1px solid {BLUE_HEPATICA};
            border-bottom: 1px solid {BLUE_HEPATICA};
            display: inline-block;
            padding: 5px 24px;
            letter-spacing: 2px;
            font-size: 0.95em;
            width: fit-content;
            margin: 0 auto 20px auto;
        }}
        .cs-card {{
            background: linear-gradient(135deg, rgba(82,33,150,0.55) 0%, rgba(26,5,53,0.85) 100%);
            border-radius: 18px;
            padding: 18px 20px;
            margin: 14px 0;
            border: 1px solid {BLUE_HEPATICA};
            box-shadow: 0 4px 24px rgba(205,35,130,0.12), inset 0 1px 0 rgba(255,221,189,0.08);
            backdrop-filter: blur(4px);
        }}
        .cs-card h3 {{
            color: {PINK_KATYDID};
            font-weight: 700;
            margin-top: 0;
            letter-spacing: 1px;
            text-transform: uppercase;
            font-size: 0.95em;
        }}
        .level-badge {{
            background: linear-gradient(135deg, #FFD700, #FFA500);
            color: #120820;
            padding: 8px 20px;
            border-radius: 30px;
            font-weight: 800;
            font-size: 18px;
            display: inline-block;
            box-shadow: 0 0 20px rgba(255,215,0,0.3);
        }}
        .xp-bar-wrap {{
            background: rgba(255,255,255,0.15);
            border-radius: 20px;
            height: 20px;
            overflow: hidden;
            position: relative;
            margin: 10px 0;
        }}
        .xp-bar-fill {{
            height: 100%;
            background: linear-gradient(90deg, {BLUE_HEPATICA}, {BANAISAGI_PURPLE}, {PINK_KATYDID});
            border-radius: 20px;
            transition: width 0.5s ease;
        }}
        .xp-text {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 12px;
            font-weight: 600;
            color: white;
            text-shadow: 0 0 10px rgba(0,0,0,0.5);
        }}
        .timer-display {{
            font-size: 64px;
            font-weight: 700;
            text-align: center;
            font-family: 'Playfair Display', serif;
            color: {PINK_KATYDID};
            text-shadow: 0 0 30px rgba(205,35,130,0.3);
            padding: 20px 0;
        }}
        .timer-progress {{
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            height: 8px;
            overflow: hidden;
            margin: 20px 0;
        }}
        .timer-progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, {BLUE_TOURMALIN}, {PINK_KATYDID});
            border-radius: 10px;
            transition: width 0.1s linear;
        }}
        .badge-item {{
            background: rgba(82,33,150,0.4);
            border: 2px solid #FFD700;
            border-radius: 12px;
            padding: 10px;
            margin: 5px;
            text-align: center;
            display: inline-block;
            width: 120px;
            font-size: 12px;
            transition: all 0.3s ease;
        }}
        .badge-item:hover {{
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(255,215,0,0.2);
        }}
        .badge-item .badge-icon {{
            font-size: 30px;
            display: block;
            margin-bottom: 5px;
        }}
        .badge-item .badge-name {{
            font-weight: 600;
            color: #FFD700;
            font-size: 11px;
        }}
        .badge-item .badge-desc {{
            font-size: 9px;
            color: {FAIRY_LIGHTS};
            opacity: 0.7;
        }}

        .badge-high {{ 
            background: {BANAISAGI_PURPLE}; 
            color: white; 
            padding: 4px 12px; 
            border-radius: 20px; 
            font-size: 12px; 
            font-weight: 700; 
            display: inline-block; 
            box-shadow: 0 0 15px rgba(205,35,130,0.5);
        }}
        .badge-medium {{ 
            background: {BLUE_HEPATICA};    
            color: white; 
            padding: 4px 12px; 
            border-radius: 20px; 
            font-size: 12px; 
            font-weight: 700; 
            display: inline-block; 
            box-shadow: 0 0 15px rgba(92,113,221,0.4);
        }}
        .badge-low {{ 
            background: {CANDIED_BLUEBERRY};
            color: {FAIRY_LIGHTS}; 
            padding: 4px 12px; 
            border-radius: 20px; 
            font-size: 12px; 
            font-weight: 700; 
            display: inline-block; 
        }}

        .badge-akademik {{ 
            background: {BLUE_TOURMALIN};  
            color: #120820; 
            padding: 4px 12px; 
            border-radius: 20px; 
            font-size: 12px; 
            font-weight: 700; 
            display: inline-block; 
            box-shadow: 0 0 15px rgba(95,187,239,0.3);
        }}
        .badge-nonakademik {{ 
            background: {PINK_KATYDID};    
            color: #120820; 
            padding: 4px 12px; 
            border-radius: 20px; 
            font-size: 12px; 
            font-weight: 700; 
            display: inline-block; 
            box-shadow: 0 0 15px rgba(255,98,187,0.3);
        }}

        .rank-badge {{
            display: inline-block; 
            width: 30px; 
            height: 30px; 
            border-radius: 50%; 
            text-align: center; 
            line-height: 30px; 
            font-weight: 700; 
            font-size: 14px;
        }}
        .rank-1 {{ 
            background: linear-gradient(135deg, #FFD700, #FFA500); 
            color: #120820; 
            box-shadow: 0 0 20px rgba(255,215,0,0.6);
        }}
        .rank-2 {{ 
            background: linear-gradient(135deg, #C0C0C0, #888);    
            color: #120820; 
            box-shadow: 0 0 20px rgba(192,192,192,0.4);
        }}
        .rank-3 {{ 
            background: linear-gradient(135deg, #CD7F32, #8B4513); 
            color: white; 
            box-shadow: 0 0 20px rgba(205,127,50,0.4);
        }}
        .rank-other {{ 
            background: {CANDIED_BLUEBERRY}; 
            color: {FAIRY_LIGHTS}; 
            box-shadow: 0 0 10px rgba(82,33,150,0.3);
        }}

        .star-gold {{ 
            color: #FFD700; 
            font-size: 14px; 
            letter-spacing: 2px;
            text-shadow: 0 0 10px rgba(255,215,0,0.3);
        }}

        .dataframe {{
            width: 100%;
            border-collapse: collapse;
            background: rgba(18,8,32,0.95);
            border-radius: 12px;
            overflow: hidden;
            color: {FAIRY_LIGHTS};
            font-size: 13px;
            box-shadow: 0 4px 30px rgba(0,0,0,0.5);
        }}
        .dataframe th {{
            background: linear-gradient(135deg, {CANDIED_BLUEBERRY}, #3a1070);
            color: {FAIRY_LIGHTS};
            padding: 14px 12px;
            font-weight: 700;
            text-align: center;
            border-bottom: 3px solid {PINK_KATYDID};
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .dataframe td {{
            padding: 12px;
            border-bottom: 1px solid rgba(92,113,221,0.15);
            vertical-align: middle;
            text-align: center;
        }}
        .dataframe tr:hover {{
            background: rgba(92,113,221,0.2) !important;
            transform: scale(1.01);
        }}
        .dataframe tbody tr:has(td:contains('🔴 High')) {{
            background: rgba(205,35,130,0.1);
        }}
        .dataframe tbody tr:has(td:contains('🟡 Medium')) {{
            background: rgba(92,113,221,0.08);
        }}
        .dataframe tbody tr:has(td:contains('🟢 Low')) {{
            background: rgba(95,187,239,0.05);
        }}
        .dataframe td:last-child {{
            color: {PINK_KATYDID};
            font-weight: 700;
            text-shadow: 0 0 20px rgba(255,98,187,0.4);
        }}
        .completed-table .dataframe td:last-child {{
            color: #27ae60;
            font-weight: 700;
            text-shadow: 0 0 20px rgba(39,174,96,0.3);
        }}

        .stButton > button {{
            background: linear-gradient(90deg, {BLUE_HEPATICA}, {CANDIED_BLUEBERRY});
            color: white; 
            border: none; 
            border-radius: 25px; 
            padding: 8px 24px; 
            font-weight: 600; 
            transition: all 0.3s ease;
        }}
        .stButton > button:hover {{
            transform: translateY(-2px); 
            box-shadow: 0 5px 20px rgba(92,113,221,0.4);
        }}
        div[data-testid="stMetricValue"] {{ color: {FAIRY_LIGHTS}; }}
        div[data-testid="stMetricLabel"] {{ color: {BLUE_TOURMALIN}; }}

        .priority-box {{
            background: rgba(18,8,32,0.8);
            border-radius: 12px;
            padding: 15px;
            border-left: 4px solid {PINK_KATYDID};
            margin: 10px 0;
        }}
        .blink-text {{
            animation: blinkPink 0.8s infinite alternate;
            font-weight: bold;
        }}
        @keyframes blinkPink {{
            0%   {{ color: {FAIRY_LIGHTS}; }}
            100% {{ color: {PINK_KATYDID}; text-shadow: 0 0 10px {PINK_KATYDID}; }}
        }}
        @keyframes bounce {{
            from {{ transform: translateY(0px); }}
            to   {{ transform: translateY(-15px); }}
        }}
        .formula-box {{
            background: rgba(18,8,32,0.9);
            border: 1px solid {BLUE_HEPATICA};
            border-radius: 14px;
            padding: 16px 20px;
            font-size: 13px;
            color: {FAIRY_LIGHTS};
            line-height: 1.8;
        }}
        .cs-progress {{
            border: 1px solid {BLUE_HEPATICA};
            border-radius: 30px;
            background: rgba(18,8,32,0.8);
            overflow: hidden;
        }}
        .cs-progress-bar {{
            background: linear-gradient(90deg, {BANAISAGI_PURPLE}, {PINK_KATYDID}, {BLUE_TOURMALIN}) !important;
            height: 30px;
            border-radius: 30px;
            text-align: center;
            line-height: 30px;
            color: white;
            font-weight: bold;
            transition: width 0.6s;
            text-shadow: 0 1px 3px rgba(0,0,0,0.5);
        }}
        .stButton > button:active {{
            transform: scale(0.95);
        }}
    </style>
    """


# ─── MAIN APP ────────────────────────────────────────────────────────────────

# ─── JALANKAN MIGRASI SEBELUM INIT DB ──────────────────────────────────
if os.path.exists(DB_NAME):
    migrate_database()

init_db()
insert_sample_tasks()
recalc_all_scores()

st.markdown(get_css(), unsafe_allow_html=True)

st.markdown('<div class="cs-title">CHRONOSCORE</div>', unsafe_allow_html=True)
st.markdown('<div class="cs-sub">Task Priority Dashboard by Kelompok 6</div>', unsafe_allow_html=True)

# ─── TABS ────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📋 Dashboard", "⏱️ Pomodoro", "🧠 Quiz", "🏆 Achievement", "📊 Analisis"])

# ─── TAB 1: DASHBOARD ──────────────────────────────────────────────────────
with tab1:
    col_input, col_display = st.columns([1, 2])

    with col_input:
        with st.container():
            st.markdown('<div class="cs-card">', unsafe_allow_html=True)
            st.markdown("### 📝 Tambah Tugas Baru")

            with st.form("form_tambah_tugas", clear_on_submit=True):
                nama = st.text_input("📝 Nama Tugas:", placeholder="Misal: Laporan Praktikum")
                menit = st.slider("⏱ Estimasi Waktu (Menit):", min_value=5, max_value=500, value=30, step=5)
                deadline = st.date_input("📅 Deadline:", value=None)
                kategori = st.selectbox("📂 Kategori:", options=KATEGORI_LIST)
                difficulty = st.radio("🎯 Tingkat Kesulitan:", options=[1, 2, 3, 4, 5],
                                      format_func=lambda x: f"{bintang(x)} ({x})", index=2)

                if deadline:
                    preview_skor, preview_prio = hitung_skor(difficulty, deadline)
                    st.markdown(f"""
                    <div style='background:rgba(18,8,32,0.9); border-radius:10px; padding:10px; margin:10px 0;'>
                        <small>💡 Estimasi Skor: <b>{preview_skor}</b> ({preview_prio})</small>
                    </div>
                    """, unsafe_allow_html=True)

                submitted = st.form_submit_button("➕ TAMBAH TUGAS", use_container_width=True)
                if submitted:
                    if not nama.strip():
                        st.error("❌ Nama tugas tidak boleh kosong!")
                    else:
                        add_task(nama, menit, deadline, kategori, difficulty)
                        st.success(f"✅ Tugas '{nama}' berhasil ditambahkan!")
                        st.rerun()

            st.markdown("---")
            st.markdown("### ✔️ Selesaikan Tugas")
            with st.form("form_aksi_tugas"):
                task_id = st.number_input("🔢 Masukkan ID Tugas:", min_value=1, step=1)
                submitted_aksi = st.form_submit_button("✔️ TANDAI SELESAI", use_container_width=True)
                if submitted_aksi:
                    sukses, pesan = complete_task_by_id(task_id)
                    if sukses:
                        st.success(pesan)
                        st.balloons()
                        st.rerun()
                    else:
                        st.error(f"❌ {pesan}")

            st.markdown("---")
            if st.button("🗑️ RESET SEMUA TUGAS", use_container_width=True):
                clear_all_tasks()
                insert_sample_tasks()
                st.success("🔄 Database direset ke data contoh.")
                st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    with col_display:
        df = get_all_tasks_df()

        if not df.empty:
            total = len(df)
            selesai = len(df[df['status'] == 'completed'])
            pending = total - selesai
            persen = (selesai / total) if total > 0 else 0

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("📊 Total Tugas", total)
            with col2:
                st.metric("✅ Selesai", selesai)
            with col3:
                st.metric("⏳ Pending", pending)
            with col4:
                st.metric("📈 Progress", f"{persen * 100:.0f}%")

            st.markdown(f"""
            <div class='cs-progress'>
                <div class='cs-progress-bar' style='width:{persen * 100:.1f}%;'>
                    {persen * 100:.1f}%
                </div>
            </div>
            <p style='margin-top:10px;color:{BLUE_TOURMALIN}'>✨ Selesai: <b>{selesai}</b> &nbsp;|&nbsp; Pending: <b>{pending}</b> &nbsp;|&nbsp; Total: <b>{total}</b></p>
            """, unsafe_allow_html=True)

            if selesai == total and total > 0:
                st.balloons()
                st.markdown("""
                <div style="text-align:center;font-size:40px;animation:bounce 0.5s infinite alternate;">😊🌸🎉✨🥳</div>
                <div class='blink-text' style='text-align:center;font-size:22px;'>🌟 SELAMAT! SEMUA TUGAS SELESAI! 🌟</div>
                """, unsafe_allow_html=True)

        if not df.empty:
            df_display = df.copy()
            df_display['skor'] = df_display.apply(
                lambda r: hitung_skor(r['difficulty'] or 3, r['deadline'])[0], axis=1)
            df_display['priority'] = df_display.apply(
                lambda r: hitung_skor(r['difficulty'] or 3, r['deadline'])[1], axis=1)

            pending_df = df_display[df_display['status'] == 'pending'].sort_values('skor', ascending=False).reset_index(
                drop=True)

            if not pending_df.empty:
                st.markdown("#### 🔥 Prioritas Tertinggi")
                top3 = pending_df.head(3)
                cols = st.columns(3)

                rank_colors = ["#FFD700", "#C0C0C0", "#CD7F32"]
                rank_emojis = ["🥇", "🥈", "🥉"]

                for idx, (_, row) in enumerate(top3.iterrows()):
                    with cols[idx]:
                        st.markdown(f"""
                        <div style='
                            background: linear-gradient(135deg, rgba(82,33,150,0.3), rgba(26,5,53,0.5));
                            border-radius: 12px;
                            padding: 15px;
                            border: 2px solid {rank_colors[idx]};
                            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                            text-align: center;
                        '>
                            <div style='font-size: 24px;'>{rank_emojis[idx]}</div>
                            <div style='font-size: 18px; font-weight: 700; color: {rank_colors[idx]};'>
                                {row['name']}
                            </div>
                            <div style='font-size: 14px; color: {FAIRY_LIGHTS};'>
                                Skor: <span style='font-weight: 700; color: {BANAISAGI_PURPLE};'>{row['skor']}</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                st.markdown("---")
                st.markdown("#### 📊 Daftar Tugas Pending")

                display_df = pending_df[
                    ['id', 'name', 'estimated_minutes', 'deadline', 'difficulty', 'skor', 'priority',
                     'category']].copy()
                display_df.columns = ['ID', 'Nama Tugas', 'Menit', 'Deadline', 'Kesulitan', 'Skor', 'Prioritas',
                                      'Kategori']

                display_df['Kesulitan'] = display_df['Kesulitan'].apply(lambda x: bintang(int(x) if x else 3))


                def format_priority(p):
                    if p == 'High':
                        return '🔴 High'
                    elif p == 'Medium':
                        return '🟡 Medium'
                    else:
                        return '🟢 Low'


                display_df['Prioritas'] = display_df['Prioritas'].apply(format_priority)
                display_df.insert(0, 'Rank', range(1, len(display_df) + 1))
                display_df['Status'] = '⏳ Pending'


                def color_score(val):
                    if val >= 65:
                        return f'<span style="color:{BANAISAGI_PURPLE}; font-weight:800; font-size:16px;">{val}</span>'
                    elif val >= 35:
                        return f'<span style="color:{BLUE_HEPATICA}; font-weight:700; font-size:15px;">{val}</span>'
                    else:
                        return f'<span style="color:{BLUE_TOURMALIN}; font-weight:600; font-size:14px;">{val}</span>'


                display_df['Skor'] = display_df['Skor'].apply(color_score)
                table_html = display_df.to_html(escape=False, index=False)
                st.markdown(table_html, unsafe_allow_html=True)

                completed_df = df_display[df_display['status'] == 'completed']
                if not completed_df.empty:
                    st.markdown("---")
                    st.markdown("#### ✅ Tugas Selesai")

                    completed_display = completed_df[['id', 'name', 'priority', 'category']].copy()
                    completed_display.columns = ['ID', 'Nama Tugas', 'Prioritas', 'Kategori']


                    def format_priority_completed(p):
                        if p == 'High':
                            return '🔴 High'
                        elif p == 'Medium':
                            return '🟡 Medium'
                        else:
                            return '🟢 Low'


                    completed_display['Prioritas'] = completed_display['Prioritas'].apply(format_priority_completed)
                    completed_display['Status'] = '✅ Selesai'
                    completed_html = completed_display.to_html(escape=False, index=False)
                    st.markdown(f'<div class="completed-table">{completed_html}</div>', unsafe_allow_html=True)

            else:
                st.success("🎉 Semua tugas sudah selesai! Tidak ada pending.")
        else:
            st.info("📭 Belum ada tugas. Tambahkan tugas baru!")

# ─── TAB 2: POMODORO (DENGAN SOLUSI PERBAIKAN) ────────────────────────────
with tab2:
    st.markdown('<div class="cs-card">', unsafe_allow_html=True)
    st.markdown("### ⏱️ Pomodoro Timer")

    # ─── INPUT TIMER ───────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3)
    with col1:
        focus_time = st.number_input("🎯 Fokus (menit)", min_value=1, max_value=60, value=25, key="focus_time_input")
    with col2:
        break_time = st.number_input("☕ Istirahat (menit)", min_value=1, max_value=30, value=5, key="break_time_input")
    with col3:
        long_break = st.number_input("🔄 Long Break (menit)", min_value=5, max_value=60, value=15, key="long_break_input")

    # ─── TOMBOL APPLY SETTINGS ────────────────────────────────────────
    col_apply, col_empty = st.columns([1, 3])
    with col_apply:
        if st.button("🔄 Apply Timer Settings", use_container_width=True):
            if 'timer_running' in st.session_state and not st.session_state.timer_running:
                st.session_state.timer_seconds = focus_time * 60
                st.session_state.timer_phase = 'focus'
                st.session_state.focus_time = focus_time
                st.session_state.break_time = break_time
                st.session_state.long_break = long_break
                st.success("✅ Timer settings applied!")
                st.rerun()
            else:
                st.warning("⚠️ Stop timer first before changing settings!")

    st.markdown("---")

    # ─── INITIALIZE SESSION STATE ─────────────────────────────────────
    if 'timer_running' not in st.session_state:
        st.session_state.timer_running = False
        st.session_state.timer_phase = 'focus'
        st.session_state.timer_seconds = focus_time * 60
        st.session_state.timer_pomodoros = 0
        st.session_state.focus_time = focus_time
        st.session_state.break_time = break_time
        st.session_state.long_break = long_break

    # ─── SYNC TIMER DENGAN INPUT ─────────────────────────────────────
    if 'focus_time' in st.session_state:
        if st.session_state.focus_time != focus_time:
            if not st.session_state.timer_running:
                st.session_state.timer_seconds = focus_time * 60
                st.session_state.timer_phase = 'focus'
                st.session_state.focus_time = focus_time
            else:
                st.session_state.focus_time = focus_time

    if 'break_time' in st.session_state:
        if st.session_state.break_time != break_time:
            st.session_state.break_time = break_time

    if 'long_break' in st.session_state:
        if st.session_state.long_break != long_break:
            st.session_state.long_break = long_break

    # ─── TAMPILKAN STATISTIK ──────────────────────────────────────────
    pomo_stats = get_pomodoro_stats()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Total Sesi", pomo_stats["total_sessions"])
    with col2:
        st.metric("⏱️ Total Menit", pomo_stats["total_minutes"])
    with col3:
        st.metric("📅 Hari Ini", pomo_stats["today_sessions"])
    with col4:
        st.metric("🕐 Menit Hari Ini", pomo_stats["today_minutes"])

    # ─── TAMPILKAN TIMER ──────────────────────────────────────────────
    if st.session_state.timer_phase == 'focus':
        max_seconds = st.session_state.focus_time * 60
    elif st.session_state.timer_phase == 'break':
        max_seconds = st.session_state.break_time * 60
    else:
        max_seconds = st.session_state.long_break * 60

    timer_seconds = st.session_state.timer_seconds
    if timer_seconds > 0:
        mins = timer_seconds // 60
        secs = timer_seconds % 60
        timer_text = f"{mins:02d}:{secs:02d}"
    else:
        timer_text = "00:00"

    phase_text = {
        'focus': '🎯 Fokus',
        'break': '☕ Istirahat',
        'long_break': '🔄 Long Break'
    }

    phase_colors = {
        'focus': BANAISAGI_PURPLE,
        'break': BLUE_TOURMALIN,
        'long_break': PINK_KATYDID
    }

    progress = ((max_seconds - timer_seconds) / max_seconds * 100) if max_seconds > 0 else 0
    phase_color = phase_colors.get(st.session_state.timer_phase, PINK_KATYDID)

    st.markdown(f"""
    <div style='text-align:center;'>
        <div style='font-size:20px; color:{phase_color}; font-weight:700;'>
            {phase_text.get(st.session_state.timer_phase, 'Fokus')}
        </div>
        <div class='timer-display' style='color:{phase_color};'>{timer_text}</div>
        <div class='timer-progress'>
            <div class='timer-progress-fill' style='width:{min(progress, 100)}%;'></div>
        </div>
        <div style='margin-top:10px;'>
            <span style='background:rgba(255,255,255,0.1); padding:5px 15px; border-radius:20px;'>
                Sesi: {st.session_state.timer_pomodoros}
            </span>
        </div>
        <div style='margin-top:5px; color:{FAIRY_LIGHTS}; font-size:12px; opacity:0.6;'>
            {st.session_state.timer_phase} - {st.session_state.timer_seconds}s remaining
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ─── KONTROL TIMER ──────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("▶️ Mulai", use_container_width=True):
            st.session_state.timer_running = True
            st.rerun()
    with col2:
        if st.button("⏹️ Stop", use_container_width=True):
            st.session_state.timer_running = False
            st.rerun()
    with col3:
        if st.button("🔄 Reset", use_container_width=True):
            st.session_state.timer_running = False
            st.session_state.timer_seconds = st.session_state.focus_time * 60
            st.session_state.timer_phase = 'focus'
            st.rerun()

    # ─── TUGAS UNTUK POMODORO ──────────────────────────────────────────
    df_tasks = get_all_tasks_df()
    pending_tasks = df_tasks[df_tasks['status'] == 'pending']
    if not pending_tasks.empty:
        st.markdown("---")
        st.markdown("### 📌 Pilih Tugas untuk Pomodoro")
        task_options = [f"{row['id']}: {row['name']}" for _, row in pending_tasks.iterrows()]
        selected_task = st.selectbox("Pilih tugas:", task_options, key="pomodoro_task")

        if st.button("✅ Selesaikan Sesi Pomodoro", use_container_width=True):
            task_id = int(selected_task.split(':')[0])
            task_name = pending_tasks[pending_tasks['id'] == task_id]['name'].iloc[0]
            xp = save_pomodoro_session(task_name, st.session_state.focus_time, task_id)
            st.success(f"✅ Sesi Pomodoro selesai! +{xp} XP")
            st.rerun()
    else:
        st.info("📭 Tidak ada tugas pending. Tambahkan tugas terlebih dahulu.")

    # ─── LOGIKA TIMER (COUNTDOWN) ──────────────────────────────────────
    if st.session_state.timer_running and st.session_state.timer_seconds > 0:
        import time as timer_time
        timer_time.sleep(1)
        st.session_state.timer_seconds -= 1
        st.rerun()
    elif st.session_state.timer_running and st.session_state.timer_seconds == 0:
        # Switch phase berdasarkan phase saat ini
        if st.session_state.timer_phase == 'focus':
            st.session_state.timer_pomodoros += 1
            # Cek apakah perlu long break (setiap 4 sesi)
            if st.session_state.timer_pomodoros % 4 == 0:
                st.session_state.timer_phase = 'long_break'
                st.session_state.timer_seconds = st.session_state.long_break * 60
                st.success(f"🎉 {st.session_state.timer_pomodoros} sesi selesai! Waktunya long break! ☕")
            else:
                st.session_state.timer_phase = 'break'
                st.session_state.timer_seconds = st.session_state.break_time * 60
                st.success("🎉 Sesi fokus selesai! Waktunya istirahat! ☕")
        elif st.session_state.timer_phase == 'break':
            st.session_state.timer_phase = 'focus'
            st.session_state.timer_seconds = st.session_state.focus_time * 60
            st.success("🎯 Waktunya fokus lagi! 🚀")
        elif st.session_state.timer_phase == 'long_break':
            st.session_state.timer_phase = 'focus'
            st.session_state.timer_seconds = st.session_state.focus_time * 60
            st.success("🎯 Long break selesai! Kembali fokus! 🚀")
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ─── TAB 3: QUIZ (DENGAN PERBAIKAN LENGKAP) ──────────────────────────────
with tab3:
    st.markdown('<div class="cs-card">', unsafe_allow_html=True)
    st.markdown("### 🧠 Quiz Relaksasi Otak")

    # Inisialisasi state quiz
    if 'quiz_initialized' not in st.session_state:
        st.session_state.quiz_initialized = True
        st.session_state.quiz_questions = None
        st.session_state.quiz_current = 0
        st.session_state.quiz_score = 0
        st.session_state.quiz_answered = False
        st.session_state.quiz_show_result = False
        st.session_state.quiz_is_correct = False
        st.session_state.quiz_completed = False
        st.session_state.quiz_selected_index = None

    col1, col2 = st.columns([2, 1])
    with col2:
        avg_score, total_attempts = get_quiz_stats()
        st.metric("📊 Rata-rata Skor", f"{avg_score:.1f}%")
        st.metric("📝 Total Attempts", total_attempts)

    with col1:
        category = st.selectbox("Pilih Kategori:", ["Semua", "Science", "General", "Math"], key="quiz_category")

        if st.button("🔄 Mulai Quiz Baru", use_container_width=True):
            st.session_state.quiz_questions = get_quiz_questions(None if category == "Semua" else category)
            st.session_state.quiz_current = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answered = False
            st.session_state.quiz_show_result = False
            st.session_state.quiz_is_correct = False
            st.session_state.quiz_completed = False
            st.session_state.quiz_selected_index = None
            st.rerun()

    # Cek apakah quiz sedang berlangsung
    if st.session_state.quiz_questions is not None and not st.session_state.quiz_completed:
        questions = st.session_state.quiz_questions
        current = st.session_state.quiz_current

        if current < len(questions):
            q = questions[current]

            # Progress bar
            st.progress((current) / len(questions), text=f"Progress: {current}/{len(questions)}")

            st.markdown(f"### Pertanyaan {current + 1} dari {len(questions)}")
            st.markdown(f"**{q['question']}**")

            options = q['options']

            # Gunakan key yang stabil
            radio_key = f"quiz_radio_{current}"

            # Jika sudah menjawab, tampilkan jawaban yang dipilih
            if st.session_state.quiz_answered:
                selected = st.session_state.quiz_selected_index
                # Tampilkan radio dengan jawaban yang dipilih (disabled)
                st.radio(
                    "Pilih jawaban:",
                    options,
                    index=selected,
                    key=radio_key,
                    disabled=True
                )
            else:
                selected = st.radio(
                    "Pilih jawaban:",
                    options,
                    index=None,
                    key=radio_key
                )

            col1, col2 = st.columns(2)

            # Tombol Jawab
            with col1:
                if st.button("✅ Jawab", use_container_width=True, key=f"jawab_{current}"):
                    if selected is not None:
                        idx = options.index(selected)
                        st.session_state.quiz_selected_index = idx
                        st.session_state.quiz_show_result = True

                        if idx == q['correct']:
                            st.session_state.quiz_score += 1
                            st.session_state.quiz_is_correct = True
                        else:
                            st.session_state.quiz_is_correct = False

                        st.session_state.quiz_answered = True
                        st.rerun()
                    else:
                        st.warning("⚠️ Pilih jawaban terlebih dahulu!")

            # Tombol Lanjut - disable jika belum menjawab
            with col2:
                lanjut_disabled = not st.session_state.quiz_answered
                if st.button("⏭️ Lanjut", use_container_width=True, key=f"lanjut_{current}", disabled=lanjut_disabled):
                    st.session_state.quiz_current += 1
                    st.session_state.quiz_answered = False
                    st.session_state.quiz_show_result = False
                    st.session_state.quiz_selected_index = None

                    if st.session_state.quiz_current >= len(questions):
                        # Quiz selesai
                        save_quiz_score(st.session_state.quiz_score, len(questions), category)
                        st.session_state.quiz_completed = True
                        st.success(f"🎉 Quiz selesai! Skor: {st.session_state.quiz_score}/{len(questions)}")
                        st.balloons()
                    st.rerun()

            # Tampilkan hasil jawaban
            if st.session_state.quiz_show_result:
                st.markdown("---")
                if st.session_state.quiz_is_correct:
                    st.success("✅ Jawaban Anda BENAR! 🎉")
                else:
                    correct_answer = q['options'][q['correct']]
                    st.error(f"❌ Jawaban Anda SALAH. Jawaban yang benar adalah: **{correct_answer}**")

                st.info(f"💡 Penjelasan: {q['explanation']}")

                # Tampilkan badge untuk jawaban benar
                if st.session_state.quiz_is_correct:
                    st.markdown("🏆 **+1 Poin!**")

        else:
            # Quiz selesai
            st.session_state.quiz_completed = True
            st.rerun()

    # Tampilkan hasil akhir quiz
    if st.session_state.quiz_completed and st.session_state.quiz_questions is not None:
        questions = st.session_state.quiz_questions
        total = len(questions)
        score = st.session_state.quiz_score

        st.markdown("---")
        st.markdown("### 🎉 Quiz Selesai!")

        # Tampilkan skor dengan animasi
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"""
            <div style='text-align:center; padding:20px; background:rgba(82,33,150,0.3); border-radius:15px; border:2px solid {PINK_KATYDID};'>
                <div style='font-size:48px; font-weight:800; color:{PINK_KATYDID};'>
                    {score}/{total}
                </div>
                <div style='font-size:18px; color:{FAIRY_LIGHTS};'>
                    {(score / total) * 100:.0f}%
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Tampilkan pesan berdasarkan skor
        percentage = (score / total) * 100
        st.markdown("---")

        if percentage >= 80:
            st.success(f"🌟 **Luar biasa!** Anda menguasai materi ini dengan baik!")
            st.balloons()
            st.markdown("🏆 **Pertahankan prestasi Anda!**")
        elif percentage >= 60:
            st.info(f"👍 **Bagus!** Anda sudah memahami sebagian besar materi.")
            st.markdown("📚 **Terus belajar untuk hasil yang lebih baik!**")
        elif percentage >= 40:
            st.warning(f"📖 **Cukup!** Perlu lebih banyak belajar lagi.")
            st.markdown("💪 **Jangan menyerah, coba lagi!**")
        else:
            st.error(f"📚 **Perlu belajar lebih giat!**")
            st.markdown("🔄 **Coba lagi quiz ini untuk meningkatkan pemahaman!**")

        # Tombol mulai ulang
        if st.button("🔄 Mulai Quiz Baru", use_container_width=True):
            st.session_state.quiz_questions = None
            st.session_state.quiz_current = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answered = False
            st.session_state.quiz_show_result = False
            st.session_state.quiz_is_correct = False
            st.session_state.quiz_completed = False
            st.session_state.quiz_selected_index = None
            st.rerun()

    elif st.session_state.quiz_questions is None:
        st.info("📝 Klik 'Mulai Quiz Baru' untuk memulai.")

        # Tampilkan statistik quiz sebelumnya
        if total_attempts > 0:
            st.markdown("---")
            st.markdown("### 📊 Statistik Quiz Anda")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("📝 Total Quiz", total_attempts)
            with col2:
                st.metric("📈 Rata-rata Skor", f"{avg_score:.1f}%")

    st.markdown('</div>', unsafe_allow_html=True)

# ─── TAB 4: ACHIEVEMENT ────────────────────────────────────────────────────
with tab4:
    st.markdown('<div class="cs-card">', unsafe_allow_html=True)
    st.markdown("### 🏆 Level & Achievement")

    stats = get_user_stats()

    # Tampilkan stats dalam 4 kolom
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"<div class='level-badge'>Level {stats['level']}</div>", unsafe_allow_html=True)
    with col2:
        st.metric("⭐ XP", stats['xp'])
    with col3:
        st.metric("✅ Tugas Selesai", stats['tasks_completed'])
    with col4:
        st.metric("🔥 Streak", f"{stats['current_streak']} hari")

    # Progress XP ke level berikutnya
    current_level = stats['level']
    next_level = current_level + 1
    current_xp = stats['xp']
    level_xp = LEVEL_THRESHOLDS.get(current_level, 0)
    next_xp = LEVEL_THRESHOLDS.get(next_level, level_xp + 500)

    # Hitung progress
    if next_xp > level_xp:
        progress = min(((current_xp - level_xp) / (next_xp - level_xp) * 100), 100)
    else:
        progress = 0

    # Tampilkan progress bar
    st.markdown(f"""
    <div>
        <div style='display:flex; justify-content:space-between; color:{FAIRY_LIGHTS};'>
            <span>Level {current_level}</span>
            <span>Level {next_level}</span>
        </div>
        <div class='xp-bar-wrap'>
            <div class='xp-bar-fill' style='width:{progress:.1f}%'></div>
            <div class='xp-text'>{stats['xp']} / {next_xp} XP</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tampilkan koleksi lencana
    st.markdown("---")
    st.markdown("### 🎖️ Koleksi Lencana")

    badges = get_earned_badges()

    if badges:
        # Tampilkan lencana dalam grid
        cols = st.columns(4)
        for idx, (name, date_earned, desc) in enumerate(badges):
            with cols[idx % 4]:
                # Icon berdasarkan nama lencana
                icon_map = {
                    "Task Starter": "🌟",
                    "Task Master": "⭐",
                    "Task Legend": "👑",
                    "Speed Demon": "⚡",
                    "Academic Star": "📚",
                    "Non-Academic Star": "🎯",
                    "High Priority": "🔴",
                    "Perfect Streak": "🔥",
                    "Pomodoro Master": "⏱️",
                    "Focus Champion": "🏆"
                }
                icon = icon_map.get(name, "🏅")

                st.markdown(f"""
                <div class='badge-item'>
                    <span class='badge-icon'>{icon}</span>
                    <div class='badge-name'>{name}</div>
                    <div class='badge-desc'>{desc}</div>
                    <div style='font-size:8px; opacity:0.5; color:{FAIRY_LIGHTS};'>
                        {date_earned[:10] if date_earned else ''}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Tampilkan total lencana
        st.markdown(f"""
        <div style='text-align:center; margin-top:20px; color:{BLUE_TOURMALIN};'>
            Total Lencana: <b style='color:{PINK_KATYDID};'>{len(badges)}</b> dari 10
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("🏅 Belum ada lencana. Selesaikan tugas untuk mendapatkan lencana!")

        # Tampilkan daftar lencana yang bisa didapat
        st.markdown("### 📋 Daftar Lencana yang Tersedia")
        cols = st.columns(4)
        for idx, (name, desc) in enumerate(BADGE_REQUIREMENTS.items()):
            with cols[idx % 4]:
                st.markdown(f"""
                <div style='
                    background: rgba(82,33,150,0.2);
                    border: 1px dashed {BLUE_HEPATICA};
                    border-radius: 10px;
                    padding: 10px;
                    margin: 5px;
                    text-align: center;
                    opacity: 0.6;
                '>
                    <div style='font-size: 24px;'>🔒</div>
                    <div style='font-weight: 600; color:{FAIRY_LIGHTS}; font-size:11px;'>{name}</div>
                    <div style='font-size:9px; color:{BLUE_TOURMALIN};'>{desc}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ─── TAB 5: ANALISIS ──────────────────────────────────────────────────────
with tab5:
    df = get_all_tasks_df()
    if df.empty:
        st.info("📭 Belum ada data untuk dianalisis.")
    else:
        df['skor'] = df.apply(lambda r: hitung_skor(r['difficulty'] or 3, r['deadline'])[0], axis=1)
        df['kat_norm'] = df['category'].apply(norm_kat)

        st.markdown("### 📊 Analisis Visual")

        col1, col2, col3 = st.columns(3)

        with col1:
            fig, ax = plt.subplots(figsize=(4, 3.5), facecolor=BG_MAIN)
            ax.set_facecolor(BG_MAIN)
            kat_count = df.groupby('kat_norm').size().reindex(KATEGORI_LIST, fill_value=0)
            if kat_count.sum() > 0:
                colors = [KATEGORI_COLORS.get(k, BLUE_TOURMALIN) for k in kat_count.index]
                wedges, texts, autotexts = ax.pie(
                    kat_count.values, labels=kat_count.index,
                    autopct='%1.0f%%', startangle=140, colors=colors,
                    pctdistance=0.72, wedgeprops=dict(linewidth=2.5, edgecolor=BG_MAIN),
                    textprops={'color': FAIRY_LIGHTS, 'fontsize': 9}
                )
                for at in autotexts:
                    at.set_color('white');
                    at.set_fontsize(10);
                    at.set_fontweight('bold')
                ax.set_title('Distribusi Tugas', color=PINK_KATYDID, fontsize=11, fontweight='bold', pad=10)
            st.pyplot(fig)
            plt.close(fig)

        with col2:
            fig, ax = plt.subplots(figsize=(4, 3.5), facecolor=BG_MAIN)
            ax.set_facecolor(BG_MAIN)
            skor_mean = df.groupby('kat_norm')['skor'].mean().reindex(KATEGORI_LIST, fill_value=0)
            bars = ax.bar(
                skor_mean.index, skor_mean.values,
                color=[KATEGORI_COLORS.get(k, BLUE_TOURMALIN) for k in skor_mean.index],
                width=0.4, edgecolor=BG_MAIN, linewidth=1.5
            )
            ax.set_ylim(0, 100)
            ax.set_title('Rata-rata Skor Prioritas', color=PINK_KATYDID, fontsize=11, fontweight='bold', pad=10)
            ax.tick_params(colors=FAIRY_LIGHTS, labelsize=9)
            ax.set_ylabel('Skor', color=BLUE_TOURMALIN, fontsize=9)
            for bar in bars:
                height = bar.get_height()
                if height > 0:
                    ax.text(bar.get_x() + bar.get_width() / 2., height + 2,
                            f'{height:.0f}', ha='center', va='bottom', color=FAIRY_LIGHTS, fontweight='bold',
                            fontsize=10)
            ax.axhline(65, color=BANAISAGI_PURPLE, linestyle='--', linewidth=1.2, alpha=0.8, label='High ≥65')
            ax.axhline(35, color=BLUE_HEPATICA, linestyle='--', linewidth=1.2, alpha=0.8, label='Medium ≥35')
            ax.legend(fontsize=7, facecolor=BG_MAIN, labelcolor=FAIRY_LIGHTS, edgecolor='#2a1050')
            st.pyplot(fig)
            plt.close(fig)

        with col3:
            fig, ax = plt.subplots(figsize=(4, 3.5), facecolor=BG_MAIN)
            ax.set_facecolor(BG_MAIN)

            pending_counts = []
            completed_counts = []
            for kat in KATEGORI_LIST:
                kat_df = df[df['kat_norm'] == kat]
                pending_counts.append(len(kat_df[kat_df['status'] == 'pending']))
                completed_counts.append(len(kat_df[kat_df['status'] == 'completed']))

            x = range(len(KATEGORI_LIST))
            width = 0.45
            bars1 = ax.bar(x, pending_counts, width, label='Pending', color=BLUE_HEPATICA, alpha=0.9, edgecolor=BG_MAIN,
                           linewidth=1.5)
            bars2 = ax.bar(x, completed_counts, width, bottom=pending_counts, label='Selesai', color='#27ae60',
                           alpha=0.8, edgecolor=BG_MAIN, linewidth=1.5)

            for bar in bars1 + bars2:
                height = bar.get_height()
                if height > 0:
                    ax.text(bar.get_x() + bar.get_width() / 2., bar.get_y() + height / 2.,
                            f'{int(height)}', ha='center', va='center', color='white', fontweight='bold', fontsize=10)

            ax.set_xticks(x)
            ax.set_xticklabels(KATEGORI_LIST, color=FAIRY_LIGHTS, fontsize=9)
            ax.set_title('Pending vs Selesai', color=PINK_KATYDID, fontsize=11, fontweight='bold', pad=10)
            ax.tick_params(colors=FAIRY_LIGHTS, labelsize=9)
            ax.set_ylabel('Jumlah Tugas', color=BLUE_TOURMALIN, fontsize=9)
            ax.legend(fontsize=8, facecolor=BG_MAIN, labelcolor=FAIRY_LIGHTS, edgecolor='#2a1050')
            st.pyplot(fig)
            plt.close(fig)

        st.markdown("---")
        st.markdown("### ⚙️ Rumus Perhitungan Skor Prioritas")
        st.markdown(f"""
        <div class='formula-box'>
            <b style='color:{PINK_KATYDID};'>Skor (0–100) = Skor Kesulitan + Skor Urgensi Deadline</b><br><br>
            <b>Skor Kesulitan</b> = (tingkat_kesulitan / 5) × 50 → maks 50 poin<br>
            &nbsp;&nbsp;⭐×1→10 &nbsp;⭐×2→20 &nbsp;⭐×3→30 &nbsp;⭐×4→40 &nbsp;⭐×5→50<br><br>
            <b>Skor Urgensi Deadline:</b><br>
            &nbsp;&nbsp;<span style='color:{BANAISAGI_PURPLE};'>● Sudah lewat / hari ini → 50</span><br>
            &nbsp;&nbsp;<span style='color:{BANAISAGI_PURPLE};'>● 1–3 hari → 40</span><br>
            &nbsp;&nbsp;<span style='color:{BLUE_HEPATICA};'>● 4–7 hari → 25</span><br>
            &nbsp;&nbsp;<span style='color:{BLUE_TOURMALIN};'>● 8–14 hari → 15</span><br>
            &nbsp;&nbsp;<span style='color:{FAIRY_LIGHTS};'>● >14 hari → 5</span><br>
            &nbsp;&nbsp;<span style='color:{FAIRY_LIGHTS};'>● Tanpa deadline → 0</span><br><br>
            <b>Klasifikasi:</b><br>
            <span class='badge-high'>🔴 High (≥65)</span>
            <span class='badge-medium'>🟡 Medium (35–64)</span>
            <span class='badge-low'>🟢 Low (&lt;35)</span>
        </div>
        """, unsafe_allow_html=True)

# ─── FOOTER ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: {BLUE_TOURMALIN}; font-size: 12px;'>© 2024 ChronoScore - Task Priority Dashboard | Kelompok 6</p>",
    unsafe_allow_html=True
)