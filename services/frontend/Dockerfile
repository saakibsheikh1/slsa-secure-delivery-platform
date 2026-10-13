FROM alpine:3.23

RUN apk add --no-cache nginx=1.28.3-r7 
 && addgroup -S -g 101 nginx 
 && adduser -S -D -H -u 101 -G nginx nginx 
 && mkdir -p /run/nginx /var/lib/nginx/tmp 
 && chown -R nginx:nginx /run/nginx /var/lib/nginx /usr/share/nginx/html

COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /tmp/client_temp /tmp/proxy_temp /tmp/fastcgi_temp /tmp/uwsgi_temp /tmp/scgi_temp 
 && chown -R nginx:nginx /tmp

USER 101:101

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]