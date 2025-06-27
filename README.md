# warehouse_counting
Project to  practice AI/ML 
# 📦 AI-Powered Warehouse Inventory Management System

An AI/ML-based system that automates and optimizes inventory management in warehouses, go-downs, and factories. Powered by **YOLOv8**, **Django**, and **efficient data structures**, this tool helps track material flow in real-time and generates end-of-day reports.

---

## 🚀 Features

### 🔍 Real-Time Inventory Detection
- Detects and counts **inflow** and **outflow** of materials using webcam feed.
- Object detection with **YOLOv8** + OpenCV.

### 📊 End-of-Day Reporting
- Summarizes stock movement.
- Auto-generated reports with charts and graphs using Matplotlib & Pandas.

### 🧠 Smart Data Handling
- 📘 Hash Maps: For quick inventory lookup.
- 📚 Stacks & Queues: Maintain chronological flow logs.
- 🌳 Tree Structures: Categorize products hierarchically.

---

## 🛠️ Tech Stack

| Component        | Technology Used           |
|------------------|---------------------------|
| 👁️ Object Detection | YOLOv8, OpenCV             |
| 🧠 Backend Logic   | Python, DSA                |
| 🌐 Web Framework  | Django                     |
| 📦 Database       | SQLite3                    |
| 📈 Reports        | Pandas, Matplotlib         |
| 🖥️ UI             | HTML, CSS (Django Templates) |

---

## 🖥️ System Architecture

[ Webcam ] → [ YOLOv8 Detection ] → [ Django Backend ]
↘
[ Database + DSA ]
↘
[ Dashboard + Reporting ]

## 📂 Folder Structure

```bash
warehouse_aiml/
├── detection/
│   ├── yolo.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── dashboard.html
├── warehouse_aiml/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
├── manage.py
└── requirements.txt



##📥 Setup Instructions</H5>


#1.Clone the Repository
git clone https://github.com/gunn2522/warehouse_counting.git
cd warehouse_counting

#2.Create Virtual Environment & Install Dependencies
python -m venv .venv
.venv\Scripts\activate     # (on Windows)
pip install -r requirements.txt

#3.Run Migrations
python manage.py migrate

#4.Run the Server
python manage.py runserver

#5.Open Web App
Navigate to: http://localhost:8000



##  📅 Coming Soon
✅ Barcode/QR Code support

✅ CSV Import/Export

✅ Live Analytics Dashboard

✅ SMS/Email Notifications for low stock



##   🙋‍♀️ About the Developer
Gunn Malhotra
🎓 Tech Enthusiast | Founder | Building smarter systems
📱 Instagram | 📧 Connect on LinkedIn soon



##  📄 License

This project is licensed under the [MIT License](LICENSE).




