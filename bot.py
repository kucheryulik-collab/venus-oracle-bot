import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ------------ ПРОГНОЗ НА ДЕНЬ ------------
def get_daily_forecast():
    return (
        "🔮 *Прогноз на сегодня*\n\n"
        "Сегодня усиливается энергия ясности. Хороший день для переписки с клиентами, "
        "выстраивания границ, финансовых решений и внутренних инсайтов.\n\n"
        "Совет дня: доверься интуиции, она сегодня особенно точна."
    )


# ------------ КОМАНДЫ БОТА ------------
async def start(update, context):
    await update.message.reply_text(
        "Привет, я Оракул Венеры 🔮\n"
        "Напиши /today чтобы получить прогноз на день."
    )

async def today(update, context):
    forecast = get_daily_forecast()
    await update.message.reply_markdown(forecast)

async def echo(update, context):
    await update.message.reply_text("Я слышу тебя. Чтобы получить прогноз — напиши /today.")

# ------------ ЗАПУСК БОТА ------------
def main():
    token = os.environ.get("TELEGRAM_TOKEN")

    if not token:
        raise ValueError("❌ TOKEN NOT FOUND! Добавь TELEGRAM_TOKEN в Render → Environment")

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("today", today))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == "__main__":
    main()
