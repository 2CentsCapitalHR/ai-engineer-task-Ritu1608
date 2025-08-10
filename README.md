*****************************Corporate Agent: An AI Legal Assistant for ADGM******************************
This project is an intelligent assistant designed to streamline the process of preparing legal documents for company incorporation in the Abu Dhabi Global Market (ADGM). It acts as an AI-powered paralegal, reviewing your documents for accuracy and completeness.

*****************************Key Features*****************************
Automated Document Checklist: Verifies if you have submitted all required documents for company incorporation.

Identifies Legal Red Flags: Scans documents for common errors like incorrect legal jurisdictions or missing clauses.

Direct In-Document Comments: Adds comments in red text directly into your Word document, showing you exactly where the issues are.

Powered by a Smart Knowledge Base: The agent's analysis is grounded in official ADGM regulations, ensuring its advice is relevant and reliable.

*****************************Project Structure*****************************
This project is organized into a few key files and folders that work together:

knowledge_base/: This is where you place all the source ADGM legal documents (.pdf, .docx). This folder acts as the textbook for our AI.

knowledge.py: A one-time script that reads all the documents from the knowledge_base/ folder and creates the agent's "brain."

faiss_index/: This folder is the agent's "brain" or memory. It's created by the script above and contains the vectorized knowledge from the legal documents, allowing for fast and intelligent searching.

app.py: This is the main application file. It runs the user interface and contains all the logic for analyzing documents, checking for missing files, and generating the final report.

requirements.txt: This file lists all the Python packages the project needs to run. The setup process uses this file to install all dependencies automatically.

*****************************Local Setup Guide*****************************
Follow these steps to get the project running on your machine.

*****************************1. Clone the Project

git clone YOUR_GITHUB_REPO_URL
cd your-repo-name

*****************************2. Set Up a Virtual Environment

*****************************# Create the environment
python -m venv venv

*****************************# Activate on Windows
venv\Scripts\activate

*****************************# Activate on macOS/Linux
source venv/bin/activate

*****************************3. Install Dependencies

pip install -r requirements.txt

*****************************4. Build the Agent's Knowledge Base ("Brain")
This step feeds the agent the ADGM rules. You only need to do this once.

Place your source ADGM documents in the knowledge_base/ folder.

Run the script below and enter your Google API Key when prompted.

python create_knowledge_base.py

This will create the faiss_index/ folder.

***************************** How to Use the Application*****************************
Run the App: With your environment activated, run the main application file from your terminal.

python app.py

Open in Browser: Navigate to the local URL provided (usually http://127.0.0.1:7860).

Analyze Your Documents:

Enter your Google API Key(AIzaSyCGHdBz6syMGFKI73DXXCAjjNsOKlWItrk).

Upload your .docx file(s).

Click the "Analyze" button.

Review the Results: You'll receive a JSON summary of the findings and a download link for the reviewed Word document.
