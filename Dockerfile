FROM nginx:latest
RUN rm -rf /etc/nginx/conf.d/default.conf
ADD root/nginx/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 8000
EXPOSE 80
CMD nginx -g daemon