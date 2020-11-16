FROM alpine:3.11.6
RUN apk add python vim tcpdump tshark curl nghttp2 iptables bash
COPY  tcp-server.py /tcp-server.py
COPY  tcp-client.py /tcp-client.py
COPY  udp-server.py /udp-server.py
COPY  udp-client.py /udp-client.py
COPY  CONTAINER_README /README
