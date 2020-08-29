FROM python:3

WORKDIR /usr/src/app

COPY src/requirements.txt .
RUN apt install chromium-chromedriver 
RUN pip install --no-cache-dir -r requirements.txt
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/

CMD [ "python", "./bot.py" ]

