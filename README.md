# 🎓 CampusOS 
> **The centralized operating system for university communication.**


CampusOS is a modern, unified web platform designed to eliminate the fragmentation of college communication. It replaces messy WhatsApp groups and buried emails with a single, role-based "Source of Truth."

---

## 🏗️ Project Status: UNDER CONSTRUCTION
This project is currently being developed for a hackathon. 
> [!IMPORTANT]
> Some interactive elements (buttons/links) are currently placeholders. To view the UI, you must run the Flask server and navigate to the routes manually.

---

## 🚀 The Vision
College students face "Information Overload." **CampusOS** segments data so that a 1st-year Mechanical student doesn't get notifications meant for a 4th-year CS student. 



---

## ✨ Key Features

### 👤 For Students
- **Personalized Feed:** View notices filtered by your Year, Branch, and Department.
- **Academic Dashboard:** Quick access to schedule and attendance.
- **Smart Notices:** Categorized by Academics, Events, and Exams.

### 🏛️ For Faculty & Admin
- **Precision Targeting:** Post notices to specific batches or the entire campus.
- **Classroom Booking:** Real-time room availability and reservation system.
- **Attendance Hub:** Manage daily lectures and student presence.

---



## 🧰 Tech Stack

- **Backend:** Python, Flask  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Frontend:** HTML, Tailwind CSS, JavaScript  
- **Templating Engine:** Jinja2  
- **Version Control:** Git & GitHub  

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

```bash
# Clone the repository
git clone https://github.com/your-username/CampusOS.git
cd CampusOS

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```


## 📂 Project Structure & Navigation
#### The project is in development phase so you might need to enter the url to visit the pages but constant improvement is being done. Also every content on the website is completely fake.
To view specific pages, start the Flask server and enter these URLs:

| Page Name | Flask Route (URL) | Description |
| :--- | :--- | :--- |
| **Landing Page** | `/` | Hero section & Project Overview |
| **Faculty Dashboard** | `/faculty_dashboard` | Overview of notices & engagement |
| **Post Notice** | `/post_notice` | Targeting & Announcement creator |
| **My Classes** | `/myclasses` | Faculty schedule & attendance |
| **Book Room** | `/classrooms` | Room availability finder |
| **Student Dashboard** | `/dashboard` | Student-side overview |
| **Login Pages** | `/login` | Authentication portal |

**Folder Directory:**
```text
CampusOS/
├── app.py                  # Flask Logic & SQLite Configuration
├── login_credentials.db     # SQLAlchemy Database
├── src/
│   └── js/script.js        # Frontend interactions
└── templates/              # Jinja2 HTML Templates  
    ├── index.html          
    ├── faculty_dashboard.html
    ├── post_notice.html
    ├── myclasses.html
    └── ... (other html files)
```

USE:<br>
This **fake** data for student login<br>
email: abcd_1@gmail.com<br>
password: abcd_1_1<br>
This **fake** data for faculty login<br>
username: efgh_11@gmail.com<br>
password: efgh_11_1