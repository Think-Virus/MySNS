# 🐦 **MySNS - A Simple Twitter Clone (Django)**  

This project is a **Twitter-like SNS clone** aimed at **learning Django** and **enhancing development skills**.  
It was originally developed in **2021**, and has been restructured for public release by removing sensitive information.  

### ▶ [Watch Demo](https://1drv.ms/v/c/699aeea76de52c4e/EaDQ-0AW0ABDrl6NEotQGiQBQyBHtNbw64PwpLZ6OdIz7w?e=smCevy)

---

## **📌 Key Features**  
### 🏠 **Home (Tweet Features)**
- Post tweets with optional tags  
- View, edit, and delete tweets  
- Tag-based tweet search  

### 👤 **User Management**
- User authentication (Sign-up, Login, Logout)  
- View user list and profiles  
- Follow and unfollow users  


## **🚀 How to Run the Project**  
### **1️⃣ Set Up the Environment**  
```bash
# Clone the repository
git clone https://github.com/Think-Virus/MySNS.git
cd MySNS

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # (For Windows: venv\Scripts\activate)

# Install required dependencies
pip install -r requirements.txt
```

### **2️⃣ Configure Environment Variables**  
Create a `.env` file in the project root and add the following:  
```
SECRET_KEY=your_secret_key
DEBUG=True
```

### **3️⃣ Run Database Migrations**  
```bash
python manage.py migrate
```

### **4️⃣ Start the Server**  
```bash
python manage.py runserver
```
- Open `http://127.0.0.1:8000/` in your browser.  

---

## **📂 Project Directory Structure**  
```
MySNS/
│   manage.py
│   requirements.txt
│   .env
│
├── mysns/                 # Django project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL routing
│
├── tweet/                 # Tweet functionality
│   ├── models.py          # Tweet data model
│   ├── views.py           # Tweet-related views
│   ├── urls.py            # URL routing for tweets
│   ├── templates/tweet/   # Tweet-related templates
│
├── user/                  # User functionality
│   ├── models.py          # User data model
│   ├── views.py           # User-related views
│   ├── urls.py            # URL routing for users
│   ├── templates/user/    # User-related templates
│
├── templates/             # Shared templates
│   ├── base.html          # Base layout
│   ├── home.html          # Main homepage
│
├── db.sqlite3             # SQLite database (for development)
└── static/                # Static files (CSS, JS, Fonts)
```


## **🛠 Tech Stack**  
- **Backend:** Django (Python 3.8+)  
- **Database:** SQLite3 (Development)  
- **Frontend:** Bootstrap 5  
- **Libraries:**  
  - `django-taggit` (Tagging support)  
  - `django-auth` (User authentication)  


## **📝 API & URL Structure**  
| Feature | URL | Description |
|---------|-----|------------|
| **User Management** | `/sign-up/` | User registration |
|  | `/sign-in/` | User login |
|  | `/logout/` | User logout |
|  | `/user/` | View user list |
|  | `/user/follow/<id>/` | Follow/unfollow a user |
| **Tweet Management** | `/tweet/` | View and create tweets |
|  | `/tweet/<id>/` | View tweet details |
|  | `/tweet/delete/<id>/` | Delete a tweet |
| **Comments** | `/tweet/comment/<id>/` | Add a comment to a tweet |
|  | `/tweet/comment/delete/<id>/` | Delete a comment |
| **Tagging System** | `/tag/` | View tag cloud |
|  | `/tag/<tag>/` | View tweets by tag |

## 📜 License  
This project is licensed under the MIT License.  

Additionally, this project makes use of third-party open-source libraries, including:  
- `django-taggit` (MIT License) → https://github.com/jazzband/django-taggit  

Please ensure compliance with respective licenses when modifying or redistributing this project.

---

✅ **This project has been modified to remove sensitive credentials before being made public.**  
If you have any suggestions or improvements, feel free to contribute! 🚀
