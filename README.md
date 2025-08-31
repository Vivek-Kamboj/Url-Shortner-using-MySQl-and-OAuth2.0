# 🔗 URL Shortener with OAuth

A modern, secure URL shortening service built with Flask, featuring Google OAuth authentication and MySQL database storage.

## ✨ Features

- **🔐 Secure Authentication**: Google OAuth 2.0 integration for user login
- **🗄️ Database Storage**: MySQL backend for storing URLs and user data
- **🎨 Modern UI**: Clean, responsive Bootstrap-based interface
- **🔒 User Sessions**: Secure session management for authenticated users
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices

## 🛠️ Tech Stack

- **Backend**: Flask (Python web framework)
- **Authentication**: Authlib (OAuth 2.0 implementation)
- **Database**: MySQL
- **Frontend**: HTML, Bootstrap 5
- **HTTP Client**: Requests library

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher
- MySQL server installed and running
- Google OAuth 2.0 credentials (Client ID and Client Secret)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd url-shortener-with-oauth
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MySQL database**
   ```sql
   CREATE DATABASE url_shortener;
   USE url_shortener;
   
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(255) UNIQUE NOT NULL,
       name VARCHAR(255),
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   
   CREATE TABLE urls (
       id INT AUTO_INCREMENT PRIMARY KEY,
       original_url TEXT NOT NULL,
       short_code VARCHAR(10) UNIQUE NOT NULL,
       user_id INT,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (user_id) REFERENCES users(id)
   );
   ```

4. **Configure the application**
   - Copy `url_shortener/config.json.example` to `url_shortener/config.json`
   - Fill in your MySQL database credentials
   - Add your Google OAuth credentials

## ⚙️ Configuration

Update the `url_shortener/config.json` file with your credentials:

```json
{
    "mysql_host": "localhost",
    "mysql_user": "your_username",
    "mysql_pass": "your_password",
    "mysql_db": "url_shortener",
    "google_client_id": "your_google_client_id",
    "google_client_secret": "your_google_client_secret",
    "secret_key": "your_secret_key_for_sessions"
}
```

### Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google+ API
4. Go to Credentials → Create Credentials → OAuth 2.0 Client IDs
5. Set the authorized redirect URI to: `http://localhost:5000/callback`
6. Copy the Client ID and Client Secret to your config file

## 🏃‍♂️ Running the Application

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Login with Google**
   Click the "Login with Google" button to authenticate

4. **Shorten URLs**
   Enter any long URL and get a shortened version

## 📁 Project Structure

```
url-shortener-with-oauth/
├── url_shortener/
│   ├── __init__.py
│   ├── app.py
│   ├── config.json
│   ├── templates/
│   │   └── index.html
│   └── static/
├── requirements.txt
└── README.md
```

## 🔧 API Endpoints

- `GET /` - Main page (login form or URL shortener)
- `GET /google_login` - Redirects to Google OAuth
- `GET /callback` - OAuth callback handler
- `POST /` - Creates shortened URL
- `GET /logout` - Logs out user and clears session

## 🗄️ Database Schema

### Users Table
- `id`: Primary key
- `email`: User's email address (unique)
- `name`: User's display name
- `created_at`: Account creation timestamp

### URLs Table
- `id`: Primary key
- `original_url`: The long URL to be shortened
- `short_code`: Generated short code for the URL
- `user_id`: Foreign key to users table
- `created_at`: URL creation timestamp

## 🔒 Security Features

- **OAuth 2.0**: Secure authentication via Google
- **Session Management**: Flask session handling
- **SQL Injection Protection**: Parameterized queries
- **HTTPS Ready**: Configured for production deployment

## 🚀 Deployment

For production deployment:

1. **Set environment variables** instead of config.json
2. **Use a production WSGI server** like Gunicorn
3. **Enable HTTPS** with SSL certificates
4. **Set up a reverse proxy** (Nginx/Apache)
5. **Configure proper logging**

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues:

1. Check the configuration file
2. Verify MySQL connection
3. Ensure Google OAuth credentials are correct
4. Check Flask application logs

## 🔮 Future Enhancements

- [ ] URL analytics and click tracking
- [ ] Custom short codes
- [ ] URL expiration dates
- [ ] Bulk URL shortening
- [ ] API endpoints for external integration
- [ ] Rate limiting
- [ ] Admin dashboard

---

**Made with ❤️ using Flask, OAuth, and MySQL**
