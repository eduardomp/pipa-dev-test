FROM renovate/yarn:latest as build-stage

LABEL maintainer="Eduardo Medeiros Pereira - edu.medeirospereira@gmail.com"
LABEL description="Dockerfile for Vue applications"

USER root

RUN adduser --disabled-password --gecos '' vue \
    && adduser vue sudo \
    && echo '%sudo ALL=(ALL:ALL) ALL' >> /etc/sudoers

RUN mkdir -p /app && \
    chown vue /app

USER vue 

WORKDIR /app

COPY . .

RUN cd /app && \
    yarn install && \
    yarn build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]