# SEMIS - Smart E-Waste Management Information System

**Masters Thesis Project**  
University of the West of Scotland (2026)

A complete IoT-based Smart E-Waste Management prototype with sensors, MQTT, cloud backend, rule-based classification, gamification, and 3 dashboards.

## Folder Structure
- `hardware/esp32/` → ESP32 code (sensors + MQTT)
- `backend/` → Python Flask dashboard + data processing
- `database/` → MySQL schema (create later)
- `templates/` → HTML dashboard pages

## Key Features (as described in thesis)
- 96.4% packet delivery inside metal bins (Faraday Cage solution)
- Rule-based waste classification (Hazardous / Recyclable / Reusable)
- Gamification with points and badges
- Three user dashboards (Citizen, Recycler, Regulator)
- Full end-to-end tracking from bin to recycling

## How to Run the Prototype
1. Clone this repository
2. `cd backend`
3. `pip install -r requirements.txt`
4. Update `config.py` with your MySQL password
5. Run `python app.py`
6. Open browser → go to `http://127.0.0.1:5000`

## Code-to-Thesis Mapping
See `CODE_MAP.md` file

**Full Source Code for the dissertation is available here.**
