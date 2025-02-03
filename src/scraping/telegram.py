from telethon import TelegramClient
from dotenv import load_dotenv
import os
import csv
import logging

logging.basicConfig(filename='scraping.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

api_id = os.getenv('APP_ID')
api_hash = os.getenv('APP_API_HASH')

client = TelegramClient("medical_data_warehouse", api_id, api_hash)

channels = [
    'https://t.me/DoctorsET',   
    'https://t.me/CheMed123',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/yetenaweg',
    'https://t.me/EAHCI'
]

async def main():
    await client.start()
    print("Client started")

    media_dir = 'photos'
    os.makedirs(media_dir, exist_ok=True)

    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])


        for channel in channels:
            await scrape_channel(channel,writer,media_dir) 
            logging.info(f"Scraped data from {channel} channel")

async def scrape_channel(channel_link,writer,media_dir):
    try:
        channel = await client.get_entity(channel_link)
        channel_title = channel.title
        async for message in client.iter_messages(channel, limit=1000):
            media_path = None
            if message.media and hasattr(message.media, 'photo'):
                filename = f"{channel_title}_{message.id}.jpg"
                media_path = os.path.join(media_dir, filename)
                await client.download_media(message.media, media_path)
            writer.writerow([channel_title, channel_link, message.id, message.message, message.date, media_path])
    except Exception as e:
        logging.error(f"Error scraping channel {channel_link}: {e}")

if __name__ == "__main__":
    client.loop.run_until_complete(main())
   



