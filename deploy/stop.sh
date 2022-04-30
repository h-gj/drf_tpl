if [$(docker ps | grep ':8005' | awk '{print $1}') = '']
then
	echo "No running container with port 8005."
else
	docker stop $(docker ps | grep ':8005' | awk '{print $1}')
fi

# https://www.cyberciti.biz/faq/unix-linux-bash-script-check-if-variable-is-empty/

