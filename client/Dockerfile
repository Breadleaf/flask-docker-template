FROM ubuntu:latest

WORKDIR /app

RUN \
	apt upgrade \
	&& apt update -y \
	&& apt install -y \
		build-essential \
		python3 \
		python3-pip \
		python3-dev \
		python3-venv

RUN rm -rf /var/lib/apt/lists/*

COPY . .

RUN ["make", "setup"]

EXPOSE 3000

CMD ["make", "start-no-setup"]
