FROM joyzoursky/python-chromedriver:3.7

WORKDIR /app
COPY src/bot.py /app/bot.py

# install selenium
RUN pip install selenium==3.8.0 requests==2.24.0

CMD ["python", "bot.py"]
