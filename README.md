# monitoring-background-processes
# CPU Monitoring and Logging Script

## Overview
This project is a cross-platform CPU monitoring script written in Python. It collects CPU utilization data for running processes, identifies high CPU–consuming processes based on a configurable threshold, and logs the results in a structured JSON format. The solution works on both Windows and Linux systems.

## Key Features

### Cross-Platform Log Directory Creation
The script detects the operating system using Python’s `platform` module and creates a `monitor_logs` directory on the Desktop for easy access.

### CPU Utilization Collection
Uses the `psutil` library to retrieve running processes. An initial CPU reading followed by a short delay ensures accurate CPU usage percentages.

### Threshold-Based Filtering
Processes consuming more than a defined CPU threshold are flagged. For demonstration purposes, the threshold is set to **5%**.

### Optional Manual Intervention
The script does not automatically terminate processes. It prints the **process ID (PID)** and **process name**, allowing the user to manually decide how to handle them.

### Sorting and Top Process Selection
Processes are sorted in **descending order of CPU usage**, and the **top 10 CPU-consuming processes** are selected for logging.

### Structured Logging
The selected processes are written to a **timestamped JSON log file**, making logs readable and easy to analyze.

### Log Retention and Cleanup
A garbage-cleaning function deletes log files older than the configured retention period. For demo purposes, the retention time is set to **86400 seconds (1 day)**.

### Error Handling
Includes exception handling for missing processes, permission issues, and file access problems to improve stability.

## Requirements
- **Python 3.x**
- **psutil** library

## How to Run
1. Clone the repository  
2. Install dependencies:
   ```bash
   pip install psutil
