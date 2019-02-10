FROM romilly/rpi-docker-tensorflow
ENV TF_CPP_MIN_LOG_LEVEL=2

ADD "." "/work"
WORKDIR "/work"
