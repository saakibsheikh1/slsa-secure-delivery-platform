FROM alpine:3.23

USER root

RUN apk update && apk add --no-cache nginx=1.28.3-r7 && apk info -v nginx && nginx -v 2>&1 && rm -rf /var/cache/apk/*

COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /tmp/client_temp /tmp/proxy_temp /tmp/fastcgi_temp /tmp/uwsgi_temp /tmp/scgi_temp && chown -R nginx:nginx /tmp && chown -R nginx:nginx /usr/share/nginx/html

USER nginx

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]