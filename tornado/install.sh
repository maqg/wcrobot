#!/bin/sh

mkdir -p /etc/nginx/conf.d/
rm -rf /etc/nginx/sites-enabled/*

cp nginx.center /etc/nginx/conf.d/center.conf
cp crt/server.key /etc/nginx/.
cp crt/server.crt /etc/nginx/.

if [ -x /etc/init.d/nginx ]; then
	/etc/init.d/nginx restart
fi

if [ -d /etc/supervisor/conf.d/ ]; then
	cp tornado.conf /etc/supervisor/conf.d/
	/etc/init.d/supervisor restart
	supervisorctl restart all
fi

