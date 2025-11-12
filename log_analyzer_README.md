# 🔍 Log Analyzer (Python)

This project reads a log file and counts the number of **ERROR** and **WARNING** messages.

---

## 🧠 Features
- Detects `"ERROR"` and `"WARNING"` lines  
- Displays a summary with total counts  
- Handles missing file errors gracefully  

---

## 🚀 How to Run
1. Save your log file (e.g., `system.log`)  
2. Run the script:

```bash
python log_analyzer.py
INFO - System started  
WARNING - Low disk space  
ERROR - Failed to connect to database  
ERROR - Timeout occurred  
📊 Log Analysis Summary:
Errors found: 2  
Warnings found: 1  
✅ Analysis completed successfully.
