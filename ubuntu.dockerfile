FROM gustavovinicius/guspy:apacheairflow
WORKDIR /var/www/html
ENTRYPOINT ["tail", "-f", "/dev/null"]