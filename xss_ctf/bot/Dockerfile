FROM joyzoursky/python-chromedriver:3.7

WORKDIR /app
COPY src/bot.py /app/bot.py

# install selenium
RUN pip install selenium==3.8.0 requests==2.24.0 mysql-connector-python

# Add docker-compose-wait tool
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

CMD ["sh", "-c", "/wait && python bot.py"]
