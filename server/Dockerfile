FROM node:latest
WORKDIR /usr/src/app

COPY ./package*.json ./
COPY ./requirements.txt ./

RUN apt update 
RUN apt -y install python3-pip
RUN pip3 install -r requirements.txt
RUN npm install

COPY ./ .

EXPOSE 3000
CMD ["npm", "start"]

