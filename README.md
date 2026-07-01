# Telegram Media Downloader

A Python script that automatically connects to your Telegram account and downloads specific types of media (audio, PDF, etc.) from a Telegram group or a specific forum topic. 

## Features
- **Chronological Downloading**: Fetches media from the oldest to the newest, renaming files sequentially (e.g., `001_filename.m4a`, `002_filename.mp3`).
- **Topic Support**: Can target a specific subtopic inside a Telegram Supergroup (Forum).
- **Resume Capability**: Checks if a file already exists before downloading, meaning you can stop and restart the script anytime without re-downloading existing files.
- **Configurable File Types**: Easily filter exactly what types of files you want to keep (`.mp3`, `.pdf`, etc.).

## Prerequisites
- Python 3.8+
- A Telegram account
- Your Telegram `API_ID` and `API_HASH` (You can get these by logging into [my.telegram.org](https://my.telegram.org)).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Telegram_Media_Downloader.git
   cd Telegram_Media_Downloader
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # (On Linux/macOS)
   # Or on Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   - Copy `.env.example` to a new file named `.env`:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and fill in your `API_ID`, `API_HASH`, and configure your `GROUP_NAME` and `BASE_DOWNLOAD_DIR`. 
   - If you want to download from a specific topic, provide the `TOPIC_ID` (you can find this at the end of the topic link, e.g., `4411` in `https://t.me/group_name/4411`).

## Usage

Run the script inside your virtual environment:

```bash
python media_downloader.py
```

The first time you run it, you will be prompted to enter your Telegram phone number and the login code sent to you via Telegram. This will generate a local `session_downloader.session` file so you don't have to log in next time.

## Safety Note
This script uses your personal Telegram account to download files. **Do not share your `.env` file or your `session_downloader.session` file with anyone**, as it grants full access to your Telegram account.

## Contributing
Contributions are always welcome! If you have any ideas, suggestions, or bug fixes, feel free to contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
MIT
