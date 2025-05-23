FROM node:18-alpine

WORKDIR /usr/src/app

# install deps
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# copy rest of source
COPY . ./

# expose port
EXPOSE 3000

# start dev server
CMD ["yarn", "start"]