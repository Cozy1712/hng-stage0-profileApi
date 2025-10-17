#  HNG13 Stage 0 — 🐍 Django Profile API

## 📋 Description
A simple Django RESTful API endpoint `/me` that returns dynamic user information along with a random cat fact fetched from an external API.

---

## ## 🎯 Objective
Build a REST API endpoint that demonstrates:

- JSON response formatting  
- External API integration  
- Dynamic data (current UTC timestamp & cat facts)  
- Error handling and clean Django design 

## 🧩 Endpoint Summary
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | /me | Returns your profile info + random cat fact |

---

## 🧠 Tech Stack
- **Language:** Python
- **Framework:** Django
- **External API:** [Cat Fact API](https://catfact.ninja/fact)

## 📦 Project Structure
```
profileApi/
│
├── core/                    # Main Django app
│   ├── views.py             # Contains the /me endpoint logic
│   ├── urls.py              # App routing configuration
│
├── profileApi/              # Django project settings
│   ├── settings.py          # Configuration settings
│   ├── urls.py              # Root routing
│
├── manage.py                # Django command-line tool
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```


## ⚙️ Setup Instructions
### Clone and setup
```bash
git clone https://github.com/Cozy1712/hng-stage0-profileApi.git
cd hng-stage0-profileApi

**2. Create and Activate a Virtual Environment**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the development server
```bash
python manage.py runserver
```
### 5. Access the endpoint
Open your browser or API testing tool (like Postman) and visit:
```
Your app will be running at: 👉 (http://127.0.0.1:8000/me) [(https://profileapi-46kr.onrender.com)]

```
---
### 🧰 Tools & Libraries
| Library | Purpose |
|----------|----------|
| Django | Framework for building the RESTful API |
| Requests | HTTP client for calling external APIs |

## 🔍 Example Response
**Endpoint:** GET /me

```json
{
  "status": "success",
  "user": {
    "email": "kolakabiru14@gmail.com",
    "name": "Kabiru Kolawole",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-16T09:12:34.567890+00:00",
  "fact": "Cats sleep for 70% of their lives."
}
```
## 🧩 Code Explanation

### `/me` Endpoint Logic
1. Fetch a random cat fact from the external API using `requests.get()`  
2. Handle errors gracefully (e.g., API down or timeout)  
3. Build the response JSON including:
   - `status`: Always `"success"`  
   - `user`: Profile info (email, name, stack)  
   - `timestamp`: Current UTC time in ISO 8601 format  
   - `fact`: The fetched cat fact  
4. Return JSON response with `JsonResponse` and proper `application/json` content type

## 🧱 Error Handling
If the external API fails or times out:  
A fallback message like `"Unable to fetch cat fact right now. Please try again later."` is returned instead of crashing the app.

## 🧭 Additional Features
- Dynamic UTC timestamps on each request  
- Graceful error handling for API calls  
- Clean Django code structure  
- Uses built-in Django `JsonResponse` for response formatting
