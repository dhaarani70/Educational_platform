
# Education Platform

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Team Members](#team-members)
- [Acknowledgement](#acknowledgement)

## Overview
The Education Platform is a web application designed to facilitate educational growth by connecting students with various learning resources, mentors, and training opportunities. The platform provides a user-friendly interface to access vital educational information and services, helping students navigate their academic journeys more effectively.

## Features
- **Learning Materials:** Browse and access a variety of educational materials, including books and videos.
- **Mentor Profiles:** View detailed information about mentors, including their specializations and contact details.
- **Student and Teacher Information:** Access profiles for students and teachers, including grades and subjects taught.
- **Tuition and Activity Centers:** Discover local tuition and activity centers, along with their offerings and locations.
- **Training Opportunities:** Explore available training centers and the courses they offer.

## Technologies Used
- **Flask:** A micro web framework for Python.
- **HTML/CSS:** For structuring and styling the web application.
- **JavaScript:** For any client-side scripting (if applicable).
- **Git:** For version control.
- **Bootstrap (optional):** For responsive design and layout (if used).

## Installation
To set up the Education Platform locally, follow these detailed steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```
   
2. **Navigate to the project directory:**
   ```bash
   cd <project-directory>
   ```

3. **Install required packages:**
   Ensure you have Flask installed. You can install it via pip:
   ```bash
   pip install Flask
   ```

4. **Add images:**
   - Download your desired background image and save it in the `static` directory of your project (e.g., `static/background.jpg`).
   - Ensure any other images are also stored in the `static` directory as required by the HTML files.

5. **Run the application:**
   Start the Flask development server with the following command:
   ```bash
   python app.py
   ```

6. **Open your web browser:**
   Visit `http://127.0.0.1:5000` to access the application.

## Usage
After launching the application, you can navigate through different sections using the links provided in the navigation menu. Each section allows you to view relevant information about learning materials, mentors, students, teachers, school details, tuition centers, activity centers, and training centers.

## Project Structure
```
/education-platform
│
├── app.py                  # Main application script
├── static                  # Directory for static files (CSS, images)
│   ├── style.css           # Stylesheet for the application
│   └── background.jpg      # Background image (example)
│
└── templates               # Directory for HTML templates
    ├── index.html         # Homepage template
    ├── learning_materials.html  # Learning materials template
    ├── mentors.html       # Mentors template
    ├── students.html      # Students template
    ├── teachers.html      # Teachers template
    ├── school_details.html # School details template
    ├── tuition_centers.html # Tuition centers template
    ├── activity_centers.html # Activity centers template
    └── training_centers.html  # Training centers template
```

## Team Members
This project is developed by:
- Dhaarani S
- Akalya S
- Lakshayaa A
- Niroshini A

## Acknowledgement
We would like to thank the online resources and repositories that provided valuable insights and tools to aid in the development of this project. Your contributions have been instrumental in bringing this platform to life.
