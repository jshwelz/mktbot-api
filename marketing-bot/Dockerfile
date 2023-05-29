FROM node:18.16.0-alpine
WORKDIR /marketing-bot

COPY package.json package-lock.json ./
RUN npm install 
RUN npm install react-scripts@3.4.1 -g 
COPY . ./
EXPOSE 5173