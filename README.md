# Insurance Policy Aggregator

## Overview
The Insurance Policy Aggregator is a tool to:
- Aggregate insurance policy data from multiple brokers into a unified format.
- Generate detailed reports and actionable insights for decision-making.
- Provide a user-friendly frontend for easy interaction.

  
## Frontend Previews

### Homepage
The application's homepage allows you to filter broker data and explore features.


![image](https://github.com/user-attachments/assets/a12dc47a-d09a-42af-99a5-843ec3146cb1)
![image](https://github.com/user-attachments/assets/8b53bb58-d83a-4c3c-a191-4a2585b9997e)

### Report Page
The report page displays aggregated data, actionable metrics, and visualized insights.


![image](https://github.com/user-attachments/assets/baa42cc4-547f-4892-9e5c-4a1e86cdd988)

---
---

## Features
- **Data Aggregation**: Combines data from multiple brokers seamlessly.
- **Detailed Reports**: Metrics like total policies, unique customers, and average policy duration.
- **Secure Data**: Ensures data integrity and compliance.

---

## Steps to Run the Project

### 1. **Clone the Repository**
```bash
git clone https://github.com/Insurance_aggregator_WebApp.git


###  Navigate to the Project Directory**

cd insurance_aggregator
```

### 2. **Set Up the Environment**
```bash
# Install Python (if not already installed): https://www.python.org/downloads
# Install virtualenv
pip install virtualenv

# Create and activate a virtual environment
# On Linux/Mac
virtualenv venv
source venv/bin/activate

# On Windows
virtualenv venv
venv\Scripts\activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Place Broker Data**
Ensure the broker CSV files (`broker1.csv`, `broker2.csv`) are placed in the `brokerdata/` folder.

### 5. **Run the Application**
```bash
python app.py
```
The application will run at `http://127.0.0.1:5000`.

### 6. **Access the Application**
Open a browser and navigate to `http://127.0.0.1:5000`. Use the filters and explore the reports generated.

---
## 7. Running Tests with Pytest

### 1. Install Pytest
Make sure pytest is installed in your environment:
```bash
pip install pytest
```

### 2. Run All Tests
To verify the functionality of the project, run the following command from the project directory:
```bash
pytest
```

### 3. View Test Results
Once pytest runs, it will display the results of all unit tests, including pass/fail statuses.

![image](https://github.com/user-attachments/assets/2c6f9528-74df-4e43-ad3f-b2bbc29b3862)


## File Structure
Here is the organized file structure of the project:

```
insurance_aggregator/
│
├── app.py                   # Main application logic
├── data_ingestion.py        # Data loading logic
├── data_normalisation.py    # Data normalization logic
├── data_aggregation.py      # Data aggregation logic
├── reporting.py             # Reporting utilities
├── requirements.txt         # Python dependencies
├── data/                   # Folder for broker CSV files
│   ├── broker1.csv
│   ├── broker2.csv
├── static/                  # Static assets (CSS, images)
│   ├── style.css            # Styling for frontend
│   ├── screenshots/         # Screenshots for README
│       ├── homepage.png
│       ├── report_page.png
│   ├── icons/
│       ├── home-icon.svg
├── templates/               # HTML templates
│   ├── index.html           # Homepage
│   ├── report.html          # Report page
```

---




