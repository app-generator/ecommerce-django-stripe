FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY unsecure.conf /etc/nginx/conf.d

# USER root

# RUN mkdir -p /vol/static
# RUN chmod 755 /vol/static

# USER nginx
