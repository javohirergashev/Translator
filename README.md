# Translator
A full-stack translator app with Python backend and React/Vite frontend, deployed on Vercel.
Practice project for connecting front-end, back-end, and deployment workflow.

## About the API

This project uses MyMemory Translation API, which provides translations between languages.
The API supports a wide range of language pairs and returns JSON responses with:
- responseData.translatedText – the translated text
- responseStatus – HTTP-like status for translation requests
- responseDetails – additional info about the translation result or errors

## Features

- Translate text between languages using a Python API
- Frontend built with React + Vite
- Backend built in Python (Flask/AWS Lambda style)
- Deployed on Vercel

## Tech Stack

- **Backend:** Python, Requests, dotenv
- **Frontend:** React, Vite
- **Deployment:** Vercel

## Project Structure

Translator/

|-- api/

│---- translator.py

│---- test.py

|-- frontend/

│----- src/

│----- package.json

|-- README.md

|-- .gitignore

|-- requirements.txt

