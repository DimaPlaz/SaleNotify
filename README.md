# Steam Sale Notifier
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![FastAPI Version](https://img.shields.io/badge/FastAPI-0.100.0-green)
![Aiogram Version](https://img.shields.io/badge/Aiogram-3.1.0-red)
![Tortoise ORM Version](https://img.shields.io/badge/TortoiseORM-0.20.0-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


**Steam Sale Notifier** is a tool designed to automatically track game discounts on the Steam platform. If you've ever missed a sale for a game you've had your eye on, this project is here to solve that problem.

## How Does It Work?

1. **Connect with the Bot:** Go to Telegram and find the channel [@SteamSaleNotifyBot](https://t.me/SteamSaleNotifyBot).
2. **Set Up Tracking:** Once you've pressed `start`, follow the bot's instructions: click on `search`, locate the game you're interested in, and subscribe to its notifications.
3. **Await Notifications:** As soon as there's a discount for your tracked game on Steam, the bot will promptly notify you.

## Technical Details

- **Programming Language:** Python
- **Framework:** FastAPI
- **ORM:** Tortoise
- **Database:** PostgreSQL
- **Additional Tools:** Redis, Celery
- **Telegram Bot:** Built with the [Aiogram](https://docs.aiogram.dev/en/dev-3.x/) library

This project combines the power of FastAPI for rapid, robust backend operations, Tortoise for ORM, PostgreSQL for secure data storage, and Redis and Celery for efficient asynchronous processing. The Telegram bot operates swiftly and reliably, thanks to the Aiogram library.

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/DimaPlaz/SaleNotify.git
```

### 2. Navigate to the Directory
```bash
cd SaleNotify
```

### 3. Copy the Environment File
Make a copy of the environment example file. You'll need to fill in the necessary configurations in the .env file:
```bash
cp devops/.env-example devops/.env
```

### 4. Build the Docker Image
```bash
docker build -f devops/Dockerfile -t sale_service .
```

### 5. Run with Docker Compose
```bash
docker compose -f devops/docker-compose.yaml --env-file=devops/.env up -d
```
After these steps, the service should be up and running. Ensure the .env file is properly configured before starting the service.

## Contributing

1. Fork the project.
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Open a pull request.
