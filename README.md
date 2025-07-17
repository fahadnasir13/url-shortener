URL Shortener API – Innovaxel Assignment

This is a simple RESTful API built using **Python (Flask)** and **MongoDB Atlas** that allows users to shorten long URLs and manage them.

## 🚀 Features

- Create a new short URL
- Retrieve the original URL
- Update the long/original URL
- Delete the short URL
- Get access statistics (how many times the short URL has been used)

## 📦 Tech Stack

- **Backend**: Python, Flask
- **Database**: MongoDB Atlas (NoSQL)
- **Environment Management**: `venv`, dotenv
- **API Testing**: Postman

## 🛠️ Setup Instructions

1. **Clone the Repository**:

```bash
git clone https://github.com/fahadnasir13/fahad-innovaxel-nasir.git
cd fahad-innovaxel-nasir
Create Virtual Environment:

bash

python -m venv venv
Activate Virtual Environment:

Windows:

bash

venv\Scripts\activate
Linux/macOS:

bash

source venv/bin/activate
Install Dependencies:

bash

pip install -r requirements.txt
Set up .env file:

Create a .env file in the root directory and add your MongoDB URI:

ini

MONGO_URI=your_mongo_connection_string_here
Run the Application:

bash

python app.py
App will run on: http://localhost:5000

📬 API Endpoints
1. Create Short URL
http

POST /shorten
Body: { "url": "https://example.com" }
2. Get Original URL
http

GET /shorten/<shortCode>
3. Update URL
http

PUT /shorten/<shortCode>
Body: { "url": "https://new-url.com" }
4. Delete URL
http

DELETE /shorten/<shortCode>
5. Get Stats
http

GET /shorten/<shortCode>/stats
🧪 Testing with Postman
You can use Postman or VS Code Postman Extension to test endpoints by sending JSON requests to http://localhost:5000.

📁 Branch Strategy
main: Contains only the README.md

dev: Full working application with all endpoints


👨‍💻 Author
Fahad Nasir
Email: fahadnasir1311@gmail.com
GitHub: https://github.com/fahadnasir13