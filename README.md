# Personalized Medication Adherence Assistant

This project is a Streamlit web app that uses a custom Hugging Face model to generate personalized medication schedules and advice for chronic disease management.

## Features
- User-friendly web interface with Streamlit
- Secure Hugging Face API key management using dotenv
- Utilizes a custom LLM hosted on Hugging Face Hub
- Generates personalized medication schedules and advice based on user input

## Setup Instructions

### 1. Clone the Repository
Clone this project to your local machine:
```bash
git clone <your-repo-url>
cd Medieval
```

### 2. Create and Activate a Virtual Environment (Recommended)
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Hugging Face API Key
1. Go to https://huggingface.co/settings/tokens and create a new access token (read access is sufficient).
2. Create a `.env` file in the project root with the following content:
   ```env
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
   ```

### 5. Run the Streamlit App
```bash
streamlit run apps.py
```

The app will open in your browser. Enter your medication details and click "Generate Schedule & Advice" to get personalized recommendations.

## Notes
- The first run may take a few minutes as the model is downloaded from Hugging Face Hub.
- Ensure your system has enough RAM and, if possible, a GPU for faster inference.
- For any issues with model loading, check your Hugging Face token and internet connection.

## File Structure
- `apps.py` — Main Streamlit app
- `requirements.txt` — Python dependencies
- `.env` — (Not committed) Your Hugging Face API key

## License
This project is for educational and research purposes. Please consult your healthcare provider before making any medical decisions.
