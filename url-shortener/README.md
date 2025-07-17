# URL Shortener

A simple URL shortening service built using **Python (Flask)** and **MongoDB Atlas**. The application provides a RESTful API and a minimal frontend to shorten long URLs and track access statistics.

## ✨ Features

* Create short URLs from long ones
* Retrieve the original long URL
* Redirect to long URLs using the short code
* Update the long/original URL
* Delete short URLs
* View stats: number of times a short URL was accessed

## 🧰 Tech Stack

* **Backend**: Python, Flask
* **Database**: MongoDB Atlas (NoSQL)
* **Frontend**: HTML, CSS, JavaScript
* **Environment**: `venv`, `python-dotenv`
* **Testing**: Postman (for API endpoints)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 2. Create a Virtual Environment & Activate It

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your MongoDB connection string:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
```

### 5. Run the Server

```bash
python app.py
```

Server will run at `http://localhost:5000`

### 6. Open Frontend

Open `index.html` in your browser to use the simple interface.

---

## 🔧 API Endpoints

### POST `/shorten`

**Request:**

```json
{
  "url": "https://www.example.com/some/long/url"
}
```

**Response:**

```json
{
  "id": "1",
  "url": "https://www.example.com/some/long/url",
  "shortCode": "abc123",
  "createdAt": "...",
  "updatedAt": "..."
}
```

### GET `/shorten/<shortCode>`

Returns the original URL or 404 if not found.

### PUT `/shorten/<shortCode>`

Update the long URL.

```json
{
  "url": "https://new-url.com"
}
```

### DELETE `/shorten/<shortCode>`

Deletes the short URL.

### GET `/shorten/<shortCode>/stats`

Returns access statistics:

```json
{
  "accessCount": 10,
  ...
}
```

---

## 📱 Screenshots

<img width="1908" height="834" alt="image" src="https://github.com/user-attachments/assets/09743c2e-3259-4c42-8b52-8a8b8fd4a418" />


---

## 👤 Author

**Fahad Nasir**

* GitHub: [@fahadnasir13](https://github.com/fahadnasir13)

---

## 🙌 Acknowledgements

* Innovaxel assignment challenge
* MongoDB Atlas free tier
* Flask official documentation

---

## 📖 License

MIT License. Feel free to use or improve this project with attribution.
