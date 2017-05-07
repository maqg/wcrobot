all::
	./build_dbcache.pl ${DB_NAME} > mysql.xml
	python3 ../bin/initial.py
	./init_db.sh
	./dump.sh

clean::
	rm -rf *.xml
	rm -rf *.example
	rm -rf *.auto
