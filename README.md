# 🎤 J. Cole Verse Generator

This is a fun web application for J. Cole fans! Whenever a button is pressed, the website dynamically displays a random verse or quote from J. Cole's discography. This application requires an **API Key** to function correctly.

The application is containerized using Docker, making it simple to deploy and run locally.

---

## 🚀 Getting Started

Follow these steps to get the application running on your local machine using Docker.

### Prerequisites

You must have [Docker](https://www.docker.com/get-started) installed on your system.

### 🔑 Step 1: Generate Your API Key

The application requires an API Key, likely sourced from Google Studio.

1.  Navigate to **Google Studio** (or the relevant service).
2.  Follow the instructions to **generate your API Key**.
3.  Keep this key handy, as you will need to set it as an environment variable.

---

### 💻 Step 2: Installation and Running

Use the following commands in your terminal to clone the repository, build the image, and run the container.

#### 2.1 Clone the Repository

```Bash
git clone [https://github.com/kirankumare25/coleme.git]
cd coleme
```
---
### 2.2 Build the Docker Image

```Bash
docker build -t jcole-app .

```

### 2.3 Run the Container with the API Key
IMPORTANT: Replace "YOUR_GENERATED_API_KEY_HERE" with the actual key you obtained in Step 1.

```bash
docker run -d -p 8080:8080 jcole-app
```