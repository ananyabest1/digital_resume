from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Portfolio | Ananya Singh"
PAGE_ICON = ":wave:"
NAME = "Ananya Singh"
DESCRIPTION = """
Aspiring Software Engineer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success. I am enthusiastic about learning new technologies, with a particular interest in Flutter app development and problem-solving.
"""
EMAIL = "ananyasinghfl21@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ananyasingh2592/",
    "GitHub": "https://github.com/ananyabest1",
}
PROJECTS = {
    "🏆 Book Exchange App": "It's an app designed to facilitate book exchanges by connecting users with others in their college or nearby vicinity who are in search of specific books",
    "🏆 Cycle Resale App": "It's an application that assists college students in selling their bicycles to one another. Users can upload images of their bicycles for resale and also browse through available listings to make purchases within their college community.",
    "🏆 Info Guild App": "This app contains information about different types of scholarships, hackathons, internships, and open-source opportunities available for students with an innovative feature of an AI chatbot embedded in the app.",
}

# --- SET PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- NAVIGATION LINKS ---
st.write('\n')
cols = st.columns(4)
cols[0].markdown("[About](#about)", unsafe_allow_html=True)
cols[1].markdown("[Projects](#projects)", unsafe_allow_html=True)
cols[2].write(f"[LinkedIn]({SOCIAL_MEDIA['LinkedIn']})")
cols[3].write(f"[GitHub]({SOCIAL_MEDIA['GitHub']})")

# --- ABOUT SECTION ---
st.write('\n')
st.write("---")
st.markdown("<h2 id='about'>About</h2>", unsafe_allow_html=True)
st.write(
    """
    I am an aspiring software engineer with a strong foundation in computer science and a passion for developing innovative solutions.
    I have experience in various programming languages and technologies, and I am always eager to learn and take on new challenges.
    """
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Strong hands-on experience in C++, Dart, and Python
- ✔️ Proficient in app development (Flutter, Dart, and FireBase)
- ✔️ Worked with different databases and on cloud
- ✔️ Excellent teamwork and communication skills
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python, C++, Dart , FireBase , NodeJS , MySQL 
- 🌐 App Development: Flutter , Dart , FireBase
- 🗄️ Databases: MySQL, PostgreSQL, MongoDB
"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write("🎓 **Computer Science and Engineering**")
st.write("Vellore Institute Of Technology, 2025")
st.write("Relevant Coursework: Algorithms, Data Structures, Computer Network, Database Management Systems, Operating System.")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---
st.write("🚧", "**App developer Intern | CodeAlpha**")
st.write("01/2024 - 02/2024")
st.write(
    """
- ► Developed and maintained app applications using Dart and FireBase
- ► Collaborated with the design team to implement user-friendly interfaces
- ► Conducted code reviews and provided feedback to peers
"""
)

# --- JOB 2 ---
st.write('\n')
st.write("🚧", "**Python Developer | InternArmy**")
st.write("12/2023 - 01/2024")
st.write(
    """
- ► Assisted in the development of different projects
- ► Analyzed large datasets to extract meaningful insights
- ► Collaborated with the design team to implement user-friendly interfaces
"""
)

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.write("---")
st.markdown("<h2 id='projects'>Projects & Accomplishments</h2>", unsafe_allow_html=True)
for project, description in PROJECTS.items():
    st.write(f"**{project}**")
    st.write(description)

# --- FOOTER ---
st.write('\n')
st.write("---")
st.write("Thank you for visiting my portfolio! Feel free to [contact me](mailto:youremail@example.com) for any inquiries.")
