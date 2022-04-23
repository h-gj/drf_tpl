FROM python:3.6
COPY ../ /drf_tpl
WORKDIR /drf_tpl
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
ENTRYPOINT /bin/bash ./deploy/start.sh
