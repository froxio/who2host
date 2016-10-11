# who2host
Simplified WIP

## Synopsis/Motivation (from about page)

At the end of a long streaming session it's hard to find another stream to host. Recycling viewers to smaller, quality streams helps those streams grow and enriches the twitch community as a whole. What Who2Host strives to accomplish is making the diamond-in-the-rough streams easier to find. Who2Host also accommodates the average end user by making it easier to find fresh streamers to watch.

## Installation/Startup
- Pip dependencies are listed in requirements.txt (taken from pip freeze, use discretion)
- RabbitMQ is used as the celery broker and must be installed ([dl page](http://www.rabbitmq.com/download.html)). If needed, more info on RabbitMQ/Celery can be found on [Celery's page](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#installation-configuration).
- Celery and Celerybeat are used to pull data and update the database. To start the service: ```$ celery -A twitchapp worker -B```. Updates happen every 30 minutes (defined in settings.py as ```CELERYBEAT_SCHEDULE```).

## License
Mozilla Public License Version 2.0
