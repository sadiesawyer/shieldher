# shieldher# ShieldHer

ShieldHer is a cybersecurity platform designed to help protect women and students from online harassment, manipulation, and digital abuse. The platform uses AI to assess messages for threats, helps users find legal and support resources nearby, and offers secure incident logging with the option to export reports for authorities or school staff.

## Goals

- Help users recognize red flags in digital communication.
- Provide a calm, supportive AI tool that explains potential risks in messages.
- Make it easy to locate legal resources or advocacy organizations based on location.
- Allow users to securely log and export incidents for reporting purposes.
- Prioritize user privacy and security at every step.

## Tech Stack

**Backend**
- FastAPI (Python)
- SQLAlchemy with SQLite for local development
- Google Gemini API for threat scanning
- Google Maps API for resource lookup
- PyJWT for token-based authentication
- passlib (bcrypt) for password hashing

**Frontend** (in progress)
- React
- JSX
- (Potentially) Tailwind CSS or CSS Modules

## Design Decisions

- The app uses modular endpoints for message analysis, resource search, and incident reporting.
- All sensitive user actions are protected by a basic login system using JWT tokens.
- Passwords are hashed with bcrypt before storage.
- A `.env` file is used to securely manage API keys and configuration settings.
- Incident logs are tied to user accounts and designed to eventually support image uploads and report export.

## Upcoming Features

- Image upload support for screenshots and evidence
- PDF export for incident logs
- Frontend UI for login, scanning, and reviewing incidents
- Admin view for advocates or legal professionals
- Breach alert system for compromised emails
- Multi-language support for broader accessibility

## Current Status

The backend is functional, including login, signup, threat scanning, and incident logging. Frontend development is starting soon. The focus so far has been on building secure, well-structured backend infrastructure.

## Contact

Developed by Sadie Sawyer. For questions or suggestions, contact sadiesawyer1@icloud.com.
