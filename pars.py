from pyrogram import Client
import xlsxwriter
import time
import datetime
from config import api_id, api_hash


def fetch_messages_from_chats(chat_links, keywords):
    # Create a new Pyrogram client
    client = Client("my_session")

    # Create a new Excel workbook and worksheet
    workbook = xlsxwriter.Workbook('messages.xlsx')
    worksheet = workbook.add_worksheet()

    # Write headers to the worksheet
    worksheet.write_row(0, 0, ["Ключевое слово", "Чат", "Ссылка на чат", "Дата и время", "Текст сообщения"])

    # Initialize row counter
    row = 1

    # Log in to the client
    with client:

        # Initialize start time
        start_time = time.time()

        # Get current date
        current_date = datetime.date.today()

        # Iterate over each chat link and fetch messages containing keywords
        for link in chat_links:
            try:
                # Extract the chat username or ID from the link
                chat_identifier = link.split("/")[-1]

                # Fetch the chat information
                try:
                    chat = client.get_chat(chat_identifier)
                except:
                    print(f"Skipping chat link: {link}. User is not a member of the chat.")
                    continue
                chat_id = chat.id

                # Fetch messages containing the keywords in the chat
                for keyword in keywords:

                    messages = client.search_messages(chat_id, keyword)

                    # Write messages to the worksheet
                    for message in messages:
                        # Check if the message is from today
                        if message.date.date() == current_date:
                            date_time = message.date.strftime("%Y-%m-%d %H:%M:%S")
                            worksheet.write(row, 0, keyword)
                            worksheet.write(row, 1, chat.title)
                            worksheet.write(row, 2, link)  # Add the chat link
                            worksheet.write(row, 3, date_time)
                            worksheet.write(row, 4, message.text)
                            row += 1

                # Sleep for 20 seconds between iterations
                time.sleep(20)

            except Exception as e:
                print(f"Error processing chat link: {link}")
                print(f"Error message: {str(e)}")
                print()
                continue

    # Close the workbook
    workbook.close()
    # Сообщение о записи данных в файл
    print("All data has been written to messages.xlsx")
    # Calculate execution time
    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time} seconds")


# List of chat links
chat_links = [
    "https://t.me/thailand_popychiki_znakomstva",
    "https://t.me/phuket_thailand_chat",
    "https://t.me/phuket_kypi_prodai",
    "https://t.me/mama_phuket",
    "https://t.me/phuket_crypto_mafia",
    "https://t.me/phuket_krasota_devyshki",
    "https://t.me/phuket_services",
    "https://t.me/phuket",
    "https://t.me/phuket_talk",
    "https://t.me/phuketvse",
    "https://t.me/smelovtai",
    "https://t.me/REALPHUKET",
    "https://t.me/phuketrai",
    "https://t.me/BB_Phuket",
    "https://t.me/Phuketpa",
    "https://t.me/gophuket",
    "https://t.me/ttb_phuket_women",
    "https://t.me/phuket_official",
    "https://t.me/itphuket",
    "https://t.me/forum_phuket",
    "https://t.me/forum_thailand",
    "https://t.me/thailand_woman",
    "https://t.me/phuket_deti",
    "https://t.me/tailand_medicina",
    "https://t.me/tailand_viza",
    "https://t.me/tailand_nedvijimost",
    "https://t.me/phket",
    "https://t.me/+KmvadDL4sF0xNGIy",
    "https://t.me/peredelanoconf",
]

# List of keywords to search for
keywords = [
    "Пластич хирург",
    "Пластич херург",
    "Блефаропласт",
    "Убрать живот",
    "Липосакц",
    "Жир отсос",
    "Жир отсас",
    "Винир",
    "Гинеколог",
    "гениколог",
    "Хирург",
    "Херург",
    "Узи",
    "кров сдат",
    "анализ",
    "Обследовани",
    "чек ап",
    "Check up",
    "Почки",
    "живот",
    "грудь",
    "Стоматолог",
    "зубн",
    "пломб",
    "коронк",
    "имплант",
    "отбели",
    "коррекц зрен",
    "хрусталик",
    "Пересад волос",
    "ортопед",
    "замен сустав",
    "операц сустав",
    "Беременност",
    "роды",
    "Бангкок госпитал",
    "Сирирож госпитал",
    "Bangkok hospital",
    "Bumrungrad hospital",
    "врач",
]


# Call the function
fetch_messages_from_chats(chat_links, keywords)
