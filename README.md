# 10bis PhoneScraper

The 10bis PhoneScraper is a Python-based tool that enables the scraping of phone data from the 10bis platform. It provides a convenient way to extract phone numbers associated with user accounts on 10bis for further analysis or data processing.

## Purpose

The primary purpose of the 10bis PhoneScraper is to gather phone data from the 10bis platform efficiently. By leveraging web scraping techniques, the tool automates the process of retrieving phone numbers linked to user accounts. This can be particularly useful for various purposes such as marketing research, data analysis, or building contact lists.

## Features

- **User Authentication**: The tool authenticates with the 10bis platform using the provided email address.
- **Data Retrieval**: It retrieves phone data associated with the authenticated user's account.
- **Data Filtering**: The tool allows users to filter the data based on additional parameters such as name, family name, gender, etc.
- **Database Integration**: The extracted data can be stored and managed in a Microsoft Access database for easy access and further analysis.

## Installation

To use the 10bis PhoneScraper, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/10bis-phonescraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 10bis-phonescraper
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Make sure you have the necessary access credentials and permissions to use the 10bis platform.

2. Update the `datapath.txt` file with the correct path to your Microsoft Access database file.

3. Run the script:

   ```bash
   python phonescraper.py
   ```

4. Follow the prompts to provide the required information, such as your email address, name, family name, and gender.

5. The script will initiate the scraping process and retrieve phone data from the 10bis platform based on the provided parameters.

6. The results, including user information associated with the retrieved phone numbers, will be displayed in the console.

## Configuration

The following configuration options are available in the project:

- `datapath.txt`: Update the file with the correct path to your Microsoft Access database file.

## Contributing

Contributions to the 10bis PhoneScraper project are welcome. If you encounter any issues, have ideas for improvements, or want to add new features, feel free to submit a pull request.
