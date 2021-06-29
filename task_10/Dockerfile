FROM centos:latest

RUN yum install httpd -y

RUN yum install net-tools -y

COPY hi.html /var/www/html

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND" ]


