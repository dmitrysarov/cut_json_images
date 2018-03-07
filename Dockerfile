FROM ubuntu:16.04


RUN apt-get update && apt-get install python-pip git -y --no-install-recommends
RUN apt-get update && apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev -y --no-install-recommends 

RUN pip install --upgrade pip && pip install -U setuptools \
&& pip install scikit-image click 
RUN git clone https://github.com/dmitrysarov/cut_json_images.git 
WORKDIR cut_json_images

