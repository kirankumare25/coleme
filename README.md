# 🎤 J. Cole Verse Generator

This is a fun web application for J. Cole fans! Whenever a button is pressed, the website dynamically displays a random verse or quote from J. Cole's discography.

The application is containerized using Docker, making it simple to deploy and run locally.

---

## 🚀 Getting Started

Follow these steps to get the application running on your local machine using Docker.

### Prerequisites

You must have [Docker](https://www.docker.com/get-started) installed on your system.

### Installation and Running

Use the following commands in your terminal to clone the repository and build/run the Docker container.

#### Step 1: Clone the Repository

Clone the project to your local machine:

```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name

docker build -t jcole-app .

docker run -d -p 8080:80 jcole-app