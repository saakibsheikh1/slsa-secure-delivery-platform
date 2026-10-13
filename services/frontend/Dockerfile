FROM nginx:1.28-alpine

USER root

RUN apk update && apk upgrade --no-cache && rm -rf /var/cache/apk/*

COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /tmp/client_temp /tmp/proxy_temp /tmp/fastcgi_temp /tmp/uwsgi_temp /tmp/scgi_temp && chown -R nginx:nginx /tmp

USER nginx

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]