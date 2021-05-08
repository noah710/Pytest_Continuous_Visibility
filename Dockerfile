FROM python:rc-alpine

# this is used to ensure the headless prep script only runs in the container
ENV sooper_sekret_key=1

# py deps
RUN pip3 install selenium pytest requests twilio pyyaml

# chromedriver deps
RUN apk update && apk add --no-cache bash \
    alsa-lib \
    at-spi2-atk \
    atk \
    cairo \
    cups-libs \
    dbus-libs \
    eudev-libs \
    expat \
    flac \
    gdk-pixbuf \
    glib \
    libgcc \
    libjpeg-turbo \
    libpng \
    libwebp \
    libx11 \
    libxcomposite \
    libxdamage \
    libxext \
    libxfixes \
    tzdata \
    libexif \
    udev \
    xvfb \
    zlib-dev \
    chromium \
    chromium-chromedriver \
    vim

COPY tests /tests
COPY deploy /deploy
COPY server.py /server.py
COPY server_params.yaml /server_params.yaml

ENTRYPOINT [ "/deploy/entrypoint.sh" ]
