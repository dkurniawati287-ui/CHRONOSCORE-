import streamlit as st
import sqlite3
from datetime import datetime, timedelta, date
import pandas as pd
import matplotlib.pyplot as plt
import random

# ─── CONFIG PAGE ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="ChronoScore", layout="wide")

# ─── KATEGORI ────────────────────────────────────────────────────────────────
KATEGORI_LIST = ["Akademik", "Non Akademik"]

# ─── WARNA ───────────────────────────────────────────────────────────────────
BG_MAIN = "#0D1117"
CARD_BG = "#161B22"
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#8B949E"
NEON_PINK = "#FF0A6C"
NEON_PURPLE = "#8338EC"
TEMP_COLD = "#00B4D8"
TEMP_WARM = "#F4A261"
TEMP_HOT = "#E76F51"
TEMP_BURNING = "#D90429"
TEMP_CORE = "#FF006E"

BLUE_TOURMALIN = "#5FBBEF"
BLUE_HEPATICA = "#5C71DD"
CANDIED_BLUEBERRY = "#522196"
BANAISAGI_PURPLE = "#CD2382"
PINK_KATYDID = "#FF62BB"

KATEGORI_COLORS = {"Akademik": BLUE_TOURMALIN, "Non Akademik": PINK_KATYDID}
DB_NAME = "tasks.db"

# ─── SESSION STATE ───────────────────────────────────────────────────────────
if "badges" not in st.session_state:
    st.session_state.badges = []
if "game_score" not in st.session_state:
    st.session_state.game_score = 0
if "current_quiz" not in st.session_state:
    st.session_state.current_quiz = None

# ─── DATA KUIS ────────────────────────────────────────────────────────────────
KUIS_DATA = [
    {"soal": "Mana yang lebih berat: 1kg kapas atau 1kg besi?", "opsi": ["Kapas", "Besi", "Sama berat"],
     "jawaban": "Sama berat"},
    {"soal": "Air dalam bentuk padat disebut...", "opsi": ["Uap", "Es", "Plasma"], "jawaban": "Es"},
    {"soal": "Jika ada 3 apel dan kamu mengambil 2, berapa apel yang kamu miliki?", "opsi": ["1", "2", "3"],
     "jawaban": "2"},
]


def get_random_quiz():
    return random.choice(KUIS_DATA)


if st.session_state.current_quiz is None:
    st.session_state.current_quiz = get_random_quiz()


# ─── FUNGSI GET WARNA BERDASARKAN SKOR ────────────────────────────────────────
def get_temp_color(score):
    if score >= 80:
        return {"bg": TEMP_CORE, "glow": NEON_PINK, "icon": "🔥"}
    elif score >= 60:
        return {"bg": TEMP_BURNING, "glow": "#FF0A6C", "icon": "⚡"}
    elif score >= 40:
        return {"bg": TEMP_HOT, "glow": "#E76F51", "icon": "🌡️"}
    elif score >= 20:
        return {"bg": TEMP_WARM, "glow": "#F4A261", "icon": "💧"}
    else:
        return {"bg": TEMP_COLD, "glow": "#00B4D8", "icon": "❄️"}


# ─── DATABASE ─────────────────────────────────────────────────────────────────
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
    conn.commit()
    conn.close()


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
    priority = "High" if skor >= 65 else "Medium" if skor >= 35 else "Low"
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
    df = pd.read_sql_query(
        "SELECT id, name, estimated_minutes, deadline, priority, category, difficulty, status FROM tasks", conn)
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
        c.execute("SELECT status FROM tasks WHERE id=?", (task_id,))
        row = c.fetchone()
        if row is None:
            return False, "ID tidak ditemukan"
        if row[0] != 'pending':
            return False, "Tugas sudah selesai"
        now = datetime.now().isoformat()
        c.execute("UPDATE tasks SET status='completed', completed_at=? WHERE id=?", (now, task_id))
        conn.commit()

        # Cek badge
        if "🔥 First Fusion" not in st.session_state.badges:
            st.session_state.badges.append("🔥 First Fusion")

        return True, "Tugas selesai! +10 XP"
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def insert_sample_tasks():
    df = get_all_tasks_df()
    if df.empty:
        sample = [
            ("Belajar UAP", 100, "2026-06-12", "Akademik", 4),
            ("Menulis Ilmiah", 60, "2026-06-10", "Akademik", 3),
            ("Video Resume", 90, "2026-06-13", "Non Akademik", 3),
        ]
        for nama, menit, deadline, kat, diff in sample:
            add_task(nama, menit, deadline, kat, diff)


init_db()
insert_sample_tasks()

# ─── CSS ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

.stApp {{
    background: linear-gradient(135deg, {BG_MAIN} 0%, #0a0c10 100%);
    font-family: 'Orbitron', monospace;
}}

.cs-title {{
    font-family: 'Orbitron', monospace;
    font-size: 2.5em;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, {TEMP_COLD}, {NEON_PINK}, {TEMP_CORE});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
}}

.cs-sub {{
    text-align: center;
    color: {TEXT_SECONDARY};
    margin-bottom: 30px;
}}

.cs-card {{
    background: {CARD_BG};
    border-radius: 16px;
    padding: 20px;
    margin: 10px 0;
    border: 1px solid {NEON_PURPLE};
}}

/* Animasi heat bar */
@keyframes heatWave {{
    0% {{ background-position: 0% 50%; }}
    100% {{ background-position: 200% 50%; }}
}}

.heat-bar {{
    height: 8px;
    border-radius: 10px;
    transition: width 0.5s ease;
    background: linear-gradient(90deg, {TEMP_COLD}, {TEMP_WARM}, {TEMP_HOT}, {TEMP_CORE});
    background-size: 200% 100%;
    animation: heatWave 2s linear infinite;
}}

/* Animasi pulse untuk high priority */
@keyframes pulse {{
    0% {{ box-shadow: 0 0 5px {NEON_PINK}; }}
    50% {{ box-shadow: 0 0 20px {NEON_PINK}; }}
    100% {{ box-shadow: 0 0 5px {NEON_PINK}; }}
}}

.pulse-card {{
    animation: pulse 1.5s infinite;
    border: 1px solid {NEON_PINK};
}}

/* Task item */
.task-item {{
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
    transition: all 0.3s ease;
}}

.task-item:hover {{
    transform: translateX(5px);
}}

.badge-item {{
    background: linear-gradient(135deg, {TEMP_BURNING}, {NEON_PINK});
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
    color: white;
    display: inline-block;
    margin: 3px;
}}

.badge-high {{ background: {TEMP_CORE}; color: white; padding: 4px 12px; border-radius: 20px; font-size: 11px; }}
.badge-medium {{ background: {TEMP_WARM}; color: white; padding: 4px 12px; border-radius: 20px; font-size: 11px; }}
.badge-low {{ background: {TEMP_COLD}; color: white; padding: 4px 12px; border-radius: 20px; font-size: 11px; }}
.badge-akademik {{ background: {BLUE_TOURMALIN}; color: white; padding: 3px 10px; border-radius: 20px; font-size: 11px; }}
.badge-nonakademik {{ background: {PINK_KATYDID}; color: white; padding: 3px 10px; border-radius: 20px; font-size: 11px; }}

.stButton > button {{
    background: linear-gradient(90deg, {NEON_PURPLE}, {NEON_PINK});
    color: white;
    border: none;
    border-radius: 10px;
    padding: 8px 20px;
    font-weight: 600;
    transition: all 0.3s ease;
}}

.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 0 15px {NEON_PINK};
}}

.stMetricValue {{ color: {NEON_PINK} !important; }}
.stMetricLabel {{ color: {TEXT_SECONDARY} !important; }}

/* Tabs */
.stTabs [data-baseweb="tab"] {{
    background: {CARD_BG};
    border-radius: 10px;
    padding: 8px 16px;
    color: {TEXT_SECONDARY};
}}
.stTabs [aria-selected="true"] {{
    background: linear-gradient(90deg, {NEON_PURPLE}, {NEON_PINK});
    color: white;
}}
</style>
""", unsafe_allow_html=True)


# ─── HELPER ───────────────────────────────────────────────────────────────────
def bintang(n):
    return "★" * n + "☆" * (5 - n)


def norm_kat(k):
    if not k: return "Non Akademik"
    return "Akademik" if k == "Akademik" else "Non Akademik"


# ─── MAIN DASHBOARD ──────────────────────────────────────────────────────────
st.markdown('<div class="cs-title">⚡ CHRONOSCORE</div>', unsafe_allow_html=True)
st.markdown('<div class="cs-sub">Task Priority Dashboard | Kelompok 6</div>', unsafe_allow_html=True)

col_input, col_display = st.columns([1, 2])

with col_input:
    with st.container():
        st.markdown('<div class="cs-card">', unsafe_allow_html=True)
        st.markdown("### 📝 Tambah Tugas")

        with st.form("form_tambah", clear_on_submit=True):
            nama = st.text_input("Nama Tugas", placeholder="Contoh: Laporan Praktikum")
            menit = st.slider("Estimasi Waktu (Menit)", 5, 500, 30, 5)
            deadline = st.date_input("Deadline", value=None)
            kategori = st.selectbox("Kategori", KATEGORI_LIST)
            difficulty = st.radio("Kesulitan", [1, 2, 3, 4, 5], format_func=lambda x: f"{bintang(x)}", index=2)

            if deadline:
                skor_preview, _ = hitung_skor(difficulty, deadline)
                temp = get_temp_color(skor_preview)
                st.markdown(f"""
                <div style='background: #1a1a2e; border-radius: 10px; padding: 10px; margin: 10px 0; text-align: center;'>
                    <span style='font-size: 24px;'>{temp['icon']}</span>
                    <span style='font-size: 20px; font-weight: bold; color: {temp["bg"]};'>{skor_preview}°C</span>
                    <div class='heat-bar' style='width: {skor_preview}%; margin-top: 5px;'></div>
                </div>
                """, unsafe_allow_html=True)

            submitted = st.form_submit_button("➕ Tambah", use_container_width=True)
            if submitted and nama.strip():
                add_task(nama, menit, deadline, kategori, difficulty)
                st.success(f"✅ '{nama}' ditambahkan!")
                st.rerun()

        st.markdown("---")
        st.markdown("### ✅ Selesaikan Tugas")

        with st.form("form_selesai"):
            task_id = st.number_input("ID Tugas", min_value=1, step=1)
            if st.form_submit_button("✓ Selesai", use_container_width=True):
                success, msg = complete_task_by_id(task_id)
                if success:
                    st.success(msg)
                    st.balloons()
                    st.rerun()
                else:
                    st.error(msg)

        st.markdown("---")
        if st.button("🔄 Reset Semua", use_container_width=True):
            clear_all_tasks()
            insert_sample_tasks()
            st.session_state.badges = []
            st.success("Reset berhasil!")
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

with col_display:
    df = get_all_tasks_df()

    if not df.empty:
        total = len(df)
        selesai = len(df[df['status'] == 'completed'])

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("📊 Total", total)
        c2.metric("✅ Selesai", selesai)
        c3.metric("⏳ Pending", total - selesai)
        c4.metric("🏆 Badges", len(st.session_state.badges))

        if total > 0:
            st.progress(selesai / total)

    tab1, tab2, tab3, tab4 = st.tabs(["📋 Daftar Tugas", "📅 Jadwal", "📊 Grafik", "🎮 Game"])

    with tab1:
        if df.empty:
            st.info("Belum ada tugas. Tambah tugas baru!")
        else:
            df['skor'] = df.apply(lambda r: hitung_skor(r['difficulty'] or 3, r['deadline'])[0], axis=1)
            df['priority'] = df.apply(lambda r: hitung_skor(r['difficulty'] or 3, r['deadline'])[1], axis=1)

            pending_df = df[df['status'] == 'pending'].copy().sort_values('skor', ascending=False)
            completed_df = df[df['status'] == 'completed'].copy()

            # Top 3 Prioritas
            if not pending_df.empty:
                st.markdown("### 🔥 Prioritas Tertinggi")
                top3 = pending_df.head(3)
                cols = st.columns(3)
                for idx, (_, row) in enumerate(top3.iterrows()):
                    skor = row['skor']
                    temp = get_temp_color(skor)
                    pulse_class = "pulse-card" if skor >= 80 else ""

                    with cols[idx]:
                        st.markdown(f"""
                        <div class='{pulse_class}' style='background: {CARD_BG}; border-radius: 15px; padding: 15px; text-align: center; border-left: 4px solid {temp["bg"]};'>
                            <div style='font-size: 2em;'>{temp['icon']}</div>
                            <div><b>{row['name']}</b></div>
                            <div style='color: {temp["bg"]}; font-size: 1.2em;'>{skor}°C</div>
                            <div>{bintang(int(row['difficulty'] or 3))}</div>
                        </div>
                        """, unsafe_allow_html=True)
                st.markdown("---")

            # Semua tugas
            st.markdown("### 📋 Semua Tugas")
            for _, row in pending_df.iterrows():
                skor = row['skor']
                temp = get_temp_color(skor)

                st.markdown(f"""
                <div class='task-item' style='background: {CARD_BG}; border-left: 4px solid {temp["bg"]};'>
                    <div style='display: flex; justify-content: space-between; flex-wrap: wrap;'>
                        <div>
                            <b>#{row['id']} - {row['name']}</b>
                        </div>
                        <div>
                            <span class='badge-{"akademik" if row["category"] == "Akademik" else "nonakademik"}'>{row['category']}</span>
                            <span class='badge-{row["priority"].lower()}'>{row['priority']}</span>
                        </div>
                    </div>
                    <div style='margin-top: 8px;'>
                        <small>⏱ {row['estimated_minutes']} menit | 📅 {row['deadline'] or 'Tidak ada'}</small>
                        <span style='float: right;'>{bintang(int(row['difficulty'] or 3))}</span>
                    </div>
                    <div style='margin-top: 8px;'>
                        <span style='color: {temp["bg"]};'>Suhu: {skor}°C {temp['icon']}</span>
                        <div class='heat-bar' style='width: {min(skor, 100)}%; margin-top: 5px;'></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            if not completed_df.empty:
                st.markdown("### ✅ Selesai")
                for _, row in completed_df.head(3).iterrows():
                    st.markdown(f"""
                    <div style='background: rgba(0,180,216,0.1); padding: 8px; border-radius: 8px; margin: 5px 0; opacity: 0.6;'>
                        <b>#{row['id']} - {row['name']}</b> ✓ Selesai
                    </div>
                    """, unsafe_allow_html=True)

    with tab2:
        pending = df[df['status'] == 'pending'].copy() if not df.empty else pd.DataFrame()
        if pending.empty:
            st.success("🎉 Tidak ada tugas untuk hari ini!")
        else:
            pending['skor'] = pending.apply(lambda r: hitung_skor(r['difficulty'] or 3, r['deadline'])[0], axis=1)
            pending = pending.sort_values('skor', ascending=False)

            total_menit = 8 * 60
            used = 0
            mulai = datetime.strptime("09:00", "%H:%M")

            st.markdown("#### 📅 Jadwal Hari Ini (08:00 - 16:00)")

            for _, row in pending.iterrows():
                dur = row['estimated_minutes']
                skor = row['skor']
                temp = get_temp_color(skor)

                if used + dur <= total_menit:
                    selesai_t = mulai + timedelta(minutes=dur)
                    st.markdown(f"""
                    <div style='background: {temp["bg"]}; padding: 10px; border-radius: 10px; margin: 8px 0; color: white;'>
                        <b>{mulai.strftime('%H:%M')} – {selesai_t.strftime('%H:%M')}</b><br>
                        {row['name']} ({dur} menit) | Suhu: {skor}°C {temp['icon']}
                    </div>
                    """, unsafe_allow_html=True)
                    mulai = selesai_t
                    used += dur
                else:
                    st.warning(f"⚠️ {row['name']} tidak muat di jadwal")

            st.info(f"⏱️ Total: {used / 60:.1f} jam dari 8 jam")

    with tab3:
        if df.empty:
            st.info("Belum ada data")
        else:
            df['skor'] = df.apply(lambda r: hitung_skor(r['difficulty'] or 3, r['deadline'])[0], axis=1)

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

            # Pie chart
            kategori_count = df['category'].value_counts()
            ax1.pie(kategori_count.values, labels=kategori_count.index, autopct='%1.0f%%',
                    colors=[BLUE_TOURMALIN, PINK_KATYDID])
            ax1.set_title('Distribusi Kategori')

            # Bar chart
            skor_mean = df.groupby('category')['skor'].mean()
            ax2.bar(skor_mean.index, skor_mean.values, color=[BLUE_TOURMALIN, PINK_KATYDID])
            ax2.set_title('Rata-rata Skor')
            ax2.set_ylabel('Skor (°C)')

            st.pyplot(fig)
            plt.close(fig)

    with tab4:
        st.markdown('<div class="cs-card">', unsafe_allow_html=True)
        st.markdown("## 🎮 Chrono Quiz")

        st.markdown(f"""
        <div style='background: linear-gradient(90deg, {NEON_PURPLE}, {NEON_PINK}); padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 20px;'>
            <span style='font-size: 1.2em;'>🏆 SKOR ANDA</span><br>
            <span style='font-size: 2em; font-weight: bold;'>{st.session_state.game_score} XP</span>
        </div>
        """, unsafe_allow_html=True)

        q = st.session_state.current_quiz
        st.markdown(f"### 🤔 {q['soal']}")

        with st.form("quiz_form"):
            jawaban = st.radio("Pilih jawaban:", q['opsi'], index=0)
            if st.form_submit_button("🚀 Jawab", use_container_width=True):
                if jawaban == q['jawaban']:
                    st.session_state.game_score += 10
                    st.success(f"✅ Benar! +10 XP (Total: {st.session_state.game_score})")
                else:
                    st.error(f"❌ Salah! Jawaban: {q['jawaban']}")
                st.session_state.current_quiz = get_random_quiz()
                st.rerun()

        # Tampilkan badge
        if st.session_state.badges:
            st.markdown("### 🏅 Badges")
            for badge in st.session_state.badges:
                st.markdown(f'<span class="badge-item">{badge}</span>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)