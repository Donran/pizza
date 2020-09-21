# Use the official image as a parent image.
FROM python:latest

# Run the command inside your image filesystem.
RUN apt update && apt upgrade && apt install -yqq curl jq sudo firefox-esr npm

# Installs some python packages we use
RUN pip3 install selenium==4.0.0a6.post2 requests

RUN npm install -g less css-validator html-validator fs glob
