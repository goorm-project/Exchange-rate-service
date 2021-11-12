#Dockerfile With Client

FROM node:16-alpine3.12

RUN mkdir -p /app

ADD . /app

WORKDIR /app/client

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]