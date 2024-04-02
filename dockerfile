FROM ubuntu
RUN apt update
RUN apt -y install python3 python3-pip
RUN mkdir app
ADD . /app

RUN chmod +rx /app/startup.sh
CMD /app/startup.sh ; sleep infinity
