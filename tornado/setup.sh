#!/bin/bash

LANG=C

# like NAME#VERSION#MUST, for eg: python3#3.2#yes
SYSTEM_PACKAGES="python3-pip::yes \
		python3::yes \
		nginx:1.6.3:yes \
		python3-tornadostreamform \
		openssh-server::yes \
		python3-tornado:3.0:yes \
		ntpdate::yes \
		rsync \
		zip::yes"


install_source_debian7()
{
	SOURCE_FILE=/etc/apt/sources.list

	if [ -f $SOURCE_FILE ] && cat $SOURCE_FILE | grep "OCTAUTO" > /dev/null; then
		return
	fi

	echo "#OCTAUTO" > $SOURCE_FILE
	echo "deb http://mirrors.163.com/debian/ wheezy main non-free contrib" >> $SOURCE_FILE
	echo "deb http://mirrors.163.com/debian/ wheezy-updates main non-free contrib" >> $SOURCE_FILE
	echo "deb http://mirrors.163.com/debian/ wheezy-backports main non-free contrib" >> $SOURCE_FILE
	echo "deb http://debian.cn99.com/debian wheezy main" >> $SOURCE_FILE

	apt-get update
}

check_package_version()
{
	THIS_VERSION=$(echo $1 | sed 's/1://g' | sed 's/+/./g') 
	EXPECTED_VERSION=$2
	PACK_NAME=$3

	echo "this_version: $THIS_VERSION" >> $LOGFILE
	echo "expected_version: $EXPECTED_VERSION" >> $LOGFILE

	THIS_FIRST=$(echo $THIS_VERSION | awk -F'.' '{print $1}')
	THIS_SECOND=$(echo $THIS_VERSION | awk -F'.' '{print $2}')

	if [ "$THIS_FIRST" = "" ] || [ "$THIS_SECOND" = "" ]; then
		echo "False"
		echo "got a bad version for $PACK_NAME: $THIS_VERSION, Please update it manually" >> $LOGFILE
		return
	fi

	EXPECTED_FIRST=$(echo $EXPECTED_VERSION | awk -F'.' '{print $1}')
	EXPECTED_SECOND=$(echo $EXPECTED_VERSION | awk -F'.' '{print $2}')

	THIS=$(expr $THIS_FIRST \* 10000 + $THIS_SECOND \* 100)
	EXPECTED=$(expr $EXPECTED_FIRST \* 10000 + $EXPECTED_SECOND \* 100)

	if [ "$EXPECTED" -gt "$THIS" ]; then
		echo "False"
		return
	fi

	echo "True"

}

get_platform_info()
{
	if [ -f /etc/debian_version ]; then
		PLATFORM_TYPE="debian"
		PLATFORM_VERSION=$(cat /etc/debian_version | awk -F'.' '{print$1}')
	elif [ -f /etc/centos-release ]; then
		PLATFORM_TYPE="centos"
		PLATFORM_VERSION=$(cat /etc/centos-release | cut -b 16- | awk -F '.' '{print $1}')
	else
		PLATFORM_TYPE=$PLATFORM_UNKNOWN
		PLATFORM_VERSION="0"
	fi
}

install_pkg()
{
	if [ "$INSTALL_NOW" != "yes" ]; then
		return
	fi

	PACK_NAME=$1
	FIRST_PART=$(echo $PACK_NAME | awk -F'-' '{print$1}')
	SECOND_PART=$(echo $PACK_NAME | awk -F'-' '{print$2}')

	echo ""
	echo -e "[\e[33m Installing package $PACK_NAME \e[0m]"
	if [ "$FIRST_PART" = "python3" ] && [ "$SECOND_PART" != "" ] && [ "$SECOND_PART" != "pip" ] && [ "$SECOND_PART" != "dev" ]; then
		if [ "$SECOND_PART" = "tornado" ]; then
			pip-3.2 install $SECOND_PART==4.3
		else
			pip-3.2 install $SECOND_PART
		fi
	else
		apt-get install $PACK_NAME -y
	fi
	echo -e "[\e[31m Installing package $PACK_NAME Finish \e[0m]"
	echo ""
}

query_package()
{
	PACK_NAME=$1
	FIRST_PART=$(echo $PACK_NAME | awk -F'-' '{print$1}')
	SECOND_PART=$(echo $PACK_NAME | awk -F'-' '{print$2}')

	if [ "$FIRST_PART" = "python3" ] && [ "$SECOND_PART" != "" ] && [ "$SECOND_PART" != "pip" ] && [ "$SECOND_PART" != "dev" ]; then
		if [ ! -x /usr/bin/pip-3.2 ]; then
			if [ "$INSTALL_NOW" != "yes" ]; then
				echo "pip3 not install, with \"apt-get install python3-pip\" to install" >> $LOGFILE
				return 1
			else
				install_pkg "python3-pip"
				if [ "$?" != 0 ]; then
					echo "pip3 not install, with \"apt-get install python3-pip\" to install" >> $LOGFILE
					return 1
				fi
			fi
		fi
		RETMSG=$(pip-3.2 freeze 2>/dev/null | grep -w $SECOND_PART | sed 's/=/ /g')
		RET=$?
		if [ "$INSTALL_NOW" = "yes" ]; then
			if [ "$RETMSG" = "" ] || [ "$RET" != 0 ]; then
				install_pkg "$PACK_NAME"
			fi
			RETMSG=$(pip-3.2 freeze 2>/dev/null | grep -w $SECOND_PART | sed 's/=/ /g')
			VERSION=$(echo $RETMSG | awk -F' ' '{print $2}')
			if [ "$VERSION" = "" ]; then
				echo "package $PACK_NAME install failed, please fix it manually" >> $LOGFILE
				return 1
			fi
		fi
		RETMSG=$(pip-3.2 freeze 2>/dev/null | grep -w $SECOND_PART | sed 's/=/ /g')
	else
		RETMSG=$(dpkg-query --show $PACK_NAME 2>/dev/null)
		RET=$?
		if [ "$INSTALL_NOW" = "yes" ]; then
			if [ "$RETMSG" = "" ] || [ "$RET" != 0 ]; then
				install_pkg "$PACK_NAME"
			fi
			RETMSG=$(dpkg-query --show $PACK_NAME 2>/dev/null)
			VERSION=$(echo $RETMSG | awk -F' ' '{print $2}')
			if [ "$VERSION" = "" ]; then
				echo "package $PACK_NAME install failed, please fix it manually" >> $LOGFILE
				return 1
			fi
		fi
		RETMSG=$(dpkg-query --show $PACK_NAME 2>/dev/null)
	fi

	if [ "$?" != 0 ]; then
		echo "Check Installation \"$PACK_NAME\" Failed" >> $LOGFILE
		return 1
	fi

	VERSION=$(echo $RETMSG | awk -F' ' '{print $2}')
	if [ "$RETMSG" = "" ] || [ "$VERSION" = "" ]; then
		echo "Check Installation \"$PACK_NAME\" Failed" >> $LOGFILE
		return 1
	fi

	return 0
}

install_bs()
{
	mkdir -p /etc/nginx/conf.d/
	cp nginx.bstorage /etc/nginx/conf.d/bstorage.conf

	if [ -d crt ]; then
		cp crt/server.key /etc/nginx/.
		cp crt/server.crt /etc/nginx/.
	else
		cp ../crt/server.key /etc/nginx/.
		cp ../crt/server.crt /etc/nginx/.
	fi

	sed -i '/client_max_body_size 100G;/d' /etc/nginx/nginx.conf 
	sed -i '/types_hash_max_size/a\\tclient_max_body_size 100G;' /etc/nginx/nginx.conf

	if [ -x /etc/init.d/nginx ]; then
		/etc/init.d/nginx restart
	fi

	return 0
}

check_packages_by_system()
{
	TYPE=$1

	THIS_RESULT=0

	echo ""
	echo "Ckecking $TYPE"

	IN_PACKAGES=$SYSTEM_PACKAGES

	for package in $IN_PACKAGES; do

		PACK_NAME=$(echo $package | awk -F':' '{print $1}')
		EXPECTED_VERSION=$(echo $package | awk -F':' '{print $2}')
		MUST=$(echo $package | awk -F':' '{print $3}')

		query_package $PACK_NAME
		RET="$?"
		if [ "$RET" != "0" ]; then
			if [ "$MUST" = "yes" ]; then
				echo -e "Check $TYPE package of $PACK_NAME [\e[1;31m FAILED \e[0m]"
				THIS_RESULT=1
			else
				echo -e "Check $TYPE package of $PACK_NAME [\e[1;33m WARNING \e[0m]"
			fi
		else
			THIS_VERSION=$(echo $RETMSG | awk -F' ' '{print $2}')
			if [ "$EXPECTED_VERSION" != "" ]; then
					VERSION_OK=$(check_package_version "$THIS_VERSION" "$EXPECTED_VERSION" "$PACK_NAME")
					if [ "$VERSION_OK" != "True" ]; then
						if [ "$MUST" = "yes" ]; then
							echo -e "Check $TYPE package of $PACK_NAME [\e[1;31m FAILED \e[0m], least good version [$EXPECTED_VERSION], installed version [$THIS_VERSION]"
							THIS_RESULT=1
						else
							echo -e "Check $TYPE package of $PACK_NAME [\e[1;33m WARNING \e[0m], least good version [$EXPECTED_VERSION], installed version [$THIS_VERSION]"
						fi
					else
						echo -e "Check $TYPE package of $PACK_NAME, version $THIS_VERSION [\e[1;32m OK \e[0m]"
					fi
			else
				echo -e "Check $TYPE package of $PACK_NAME, version $THIS_VERSION [\e[1;32m OK \e[0m]"
			fi
		fi
	done

	return $THIS_RESULT
}

check_packages()
{
	RESULT=0

	check_packages_by_system "SERVER"
	if [ "$?" != 0 ]; then
		RESULT=1
	fi

	return $RESULT
}

PLATFORM_TYPE_DEBIAN="debian"
PLATFORM_TYPE_CENTOS="centos"

PLATFORM_TYPE=
PLATFORM_VERSION=
PLATFORM_UNKNOWN="unknown"

INSTALL_NOW="no"
if [ "$1" = "-y" ]; then
	INSTALL_NOW="yes"
fi

LOGFILE=/var/log/rvm_install.log

echo ""
echo "Running installation scripts"

date > $LOGFILE

echo "Begin to install" >> $LOGFILE

get_platform_info
if [ "$PLATFORM_TYPE" = $PLATFORM_UNKNOWN ]; then
	echo -e "Now only CentOS 6.X/7.X and Debian 7.X are supported"
	exit 1
fi

if [ "$PLATFORM_TYPE" = $PLATFORM_TYPE_DEBIAN ] && [ "$PLATFORM_VERSION" = "7" ] && [ "$INSTALL_NOW" = "yes" ]; then
	install_source_debian7
fi

RETMSG=

check_packages
RET=$?
if [ $RET != 0 ]; then
	echo ""
	echo -e "\e[1;31mWARNING: Some packages not installed or versions not match, \nplease fix it\e[0m"
	echo ""
	echo -e "\e[1;31mInstall failed, please check log file /var/log/rvm_install.log. \e[0m"
	echo ""
	exit 0
fi

install_bs
if [ "$?" = 0 ]; then
	echo ""
	echo -e "\e[1;32mInstall OK, REBOOT to FINISH installation! \e[0m"
	echo ""
	exit 0
else
	echo ""
	echo -e "\e[1;31mInstall failed, please check log file /var/log/rvm_install.log. \e[0m"
	echo ""
fi

echo "Finish to install" >> $LOGFILE
