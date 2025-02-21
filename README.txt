# Streamlit Google Sheets App

This is a Streamlit web application that allows users to interact with Google Sheets data in real-time. The app is built using Python and the Streamlit framework, with Google Sheets serving as the backend database.

## Features
- Fetch data from Google Sheets and display it in an interactive table.
- Filter data based on user selections.
- Update and save data back to Google Sheets.
- User-friendly UI with dropdowns, buttons, and editable fields.

## Prerequisites
Before running the app, ensure you have the following installed:
- Python 3.9+
- Google Cloud service account key (JSON file)
- Required Python libraries

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/streamlit-gsheet-app.git
cd streamlit-gsheet-app
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Google Sheets API
- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project and enable the Google Sheets API and Google Drive API.
- Create a **Service Account** and download the JSON credentials file.
- Move the JSON file to your project folder and rename it **service_account.json**.

### 5. Run the Application
```bash
streamlit run app.py
```

## Deployment
### Option 1: Deploy on Streamlit Cloud (Free)
1. Push your code to **GitHub**.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **New App** → Select your repository.
4. Enter `app.py` as the entry file and click **Deploy**.

### Option 2: Deploy on Google App Engine
1. Enable App Engine on GCP.
2. Create an `app.yaml` file:
   ```yaml
   runtime: python39
   entrypoint: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```
3. Deploy the app:
   ```bash
   gcloud app deploy
   ```

## License
This project is licensed under the MIT License.

## Author
**Your Name**  
GitHub: [Your GitHub Profile](https://github.com/YOUR_USERNAME)

