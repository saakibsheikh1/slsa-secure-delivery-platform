
FROM nginx:1.28-alpine

COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /tmp/client_temp \
             /tmp/proxy_temp \
             /tmp/fastcgi_temp \
             /tmp/uwsgi_temp \
             /tmp/scgi_temp \
    && chown -R nginx:nginx /tmp \
    && rm -f /etc/nginx/conf.d/default.conf

USER nginx

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
