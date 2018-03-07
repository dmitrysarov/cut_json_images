FROM ubuntu:16.04


RUN apt-get update && apt-get install python-pip git -y --no-install-recommends
RUN apt-get update && apt-get install \
    python-pip python3-pip python-dev python-tk python3-tk libgtk2.0-dev \ 
    git curl -y --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install -U setuptools \
&& pip install scikit-image click 
RUN git clone https://github.com/dmitrysarov/cut_json_images.git 
WORKDIR cut_json_images

