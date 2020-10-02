# Use the official image as a parent image.
FROM ubuntu:20.04

# Run the command inside your image filesystem.
RUN export DEBIAN_FRONTEND="noninteractive"
RUN apt update && apt-get install -y tzdata
RUN ln -fs /usr/share/zoneinfo/Europe/Stockholm /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata


RUN apt update && apt upgrade && apt install -yqq curl jq sudo firefox ruby-full build-essential zlib1g-dev python3 python3-pip



# Installs some python packages we use
RUN pip3 install selenium requests

RUN gem install jekyll bundler jekyll-less therubyracer
