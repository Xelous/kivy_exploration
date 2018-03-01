# Install necessary system packages
sudo apt-get install -y python-pip build-essential git python python-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev libgstreamer1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good

sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get install ffmpeg

sudo add-apt-repository ppa:kivy-team/kivy
sudo apt-get install python-kivy

sudo apt-get install python3-kivy