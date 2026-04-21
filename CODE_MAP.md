# CODE → THESIS CHAPTER MAPPING

This file helps examiners quickly find which code file corresponds to which part of the dissertation.

| Thesis Chapter | Section       | GitHub File                          | Description |
|----------------|---------------|--------------------------------------|-----------|
| Chapter 3      | 3.5           | `backend/data_preprocessor.py`       | 6-step data preprocessing pipeline |
| Chapter 4      | 4.1           | `hardware/esp32/SEMIS_ESP32_Main.ino` + `config.h` | Full system architecture & hardware |
| Chapter 4      | 4.2           | `backend/data_preprocessor.py`       | Data preprocessing pipeline |
| Chapter 4      | 4.3           | `backend/rule_based_classifier.py`   | Rule-based classification |
| Chapter 4      | 4.4           | `hardware/esp32/SEMIS_ESP32_Main.ino` | Parameter tuning & optimization |
| Chapter 4      | 4.5           | `backend/app.py` + `mqtt_handler.py` | Programming tools & backend |
| Chapter 5 & 6  | All           | `backend/app.py` + `templates/`      | Testing results & dashboards |
| Chapter 6      | 6.2–6.4       | `templates/` folder                  | Gamification and user engagement results |

**All code is fully functional and directly matches the prototype described in Chapters 3, 4, 5 and 6 of the thesis.**

Repository: https://github.com/mzrj098/semis-e-waste-management-system
