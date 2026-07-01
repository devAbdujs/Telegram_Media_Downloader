import os
from dotenv import load_dotenv
from telethon import TelegramClient

# Load environment variables from .env file
load_dotenv()

# 1. Telegram API Credentials
API_ID = int(os.getenv('API_ID', 0))
API_HASH = os.getenv('API_HASH', '')

# 2. Telegram Group and Topic Configuration
GROUP_NAME = os.getenv('GROUP_NAME', '')

# Optional: If you only want to download from a specific subtopic/thread
_topic_id = os.getenv('TOPIC_ID')
TOPIC_ID = int(_topic_id) if _topic_id else None

# 3. Configured Paths
BASE_DOWNLOAD_DIR = os.getenv('BASE_DOWNLOAD_DIR', './downloads')
ALLOWED_EXTENSIONS = ('.mp3', '.aac', '.m4a', '.pdf')

# Create the folder automatically if it doesn't exist
os.makedirs(BASE_DOWNLOAD_DIR, exist_ok=True)

# Stores the login session safely inside your new project folder
client = TelegramClient('session_downloader', API_ID, API_HASH)

async def main():
    print("Connecting to Telegram...")
    async for dialog in client.iter_dialogs():
        if dialog.name == GROUP_NAME:
            entity = dialog.entity
            print(f"Found group: {dialog.name}")
            break
    else:
        print(f"Could not find a group named '{GROUP_NAME}'")
        return

    print("Gathering message history in chronological order...")
    valid_messages = []

    # reverse=True fetches from oldest upload to newest upload
    kwargs = {'reverse': True}
    if TOPIC_ID:
        kwargs['reply_to'] = TOPIC_ID

    async for message in client.iter_messages(entity, **kwargs):
        if message.document and message.file.name:
            filename_lower = message.file.name.lower()
            if filename_lower.endswith(ALLOWED_EXTENSIONS):
                valid_messages.append(message)

    total_files = len(valid_messages)
    print(f"Found {total_files} matching files to process.")
    
    audio_counter = 1
    download_count = 0

    for message in valid_messages:
        original_name = message.file.name

        # Dynamically adjusts padding (001, 002...) based on total count
        padding = max(3, len(str(total_files)))
        prefix = str(audio_counter).zfill(padding)
        
        # Combines the chronological index number with the original filename
        numbered_name = f"{prefix}_{original_name}"
        save_path = os.path.join(BASE_DOWNLOAD_DIR, numbered_name)
        audio_counter += 1

        # Check if file already exists so you can safely resume later
        if os.path.exists(save_path):
            print(f"Skipping (already exists): {os.path.basename(save_path)}")
            continue

        print(f"Downloading [{audio_counter-1}/{total_files}]: {os.path.basename(save_path)}...")
        await message.download_media(file=save_path)
        download_count += 1

    print(f"\nSuccess! Downloaded {download_count} new files to {BASE_DOWNLOAD_DIR}")

with client:
    client.loop.run_until_complete(main())
