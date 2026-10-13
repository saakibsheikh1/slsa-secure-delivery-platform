FROM alpine:3.23

RUN apk add --no-cache nginx=1.28.3-r7
RUN addgroup -S -g 101 nginx
RUN adduser -S -D -H -u 101 -G nginx nginx
RUN mkdir -p /run/nginx /var/lib/nginx/tmp /tmp/client_temp /tmp/proxy_temp /tmp/fastcgi_temp /tmp/uwsgi_temp /tmp/scgi_temp
RUN chown -R nginx:nginx /run/nginx /var/lib/nginx /usr/share/nginx/html /tmp

COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf

USER 101:101

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]