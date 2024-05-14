FROM python:3.12-bullseye

WORKDIR /app
ENV HOME=/app
# Install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt update -y
RUN apt install -y google-chrome-stable

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python3.12 src/recap_collector.py
