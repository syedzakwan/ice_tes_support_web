from python:3.9.2

ENV http_proxy=http://proxy-png.intel.com:911
ENV https_proxy=http://proxy-png.intel.com:912
ENV ftp_proxy=http://proxy-png.intel.com:911
ENV socks_proxy=http://proxy-png.intel.com:1080
ENV no_proxy localhost,.intel.com,*.intel.com,10.0.0.0/8


WORKDIR python-docker 


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY . .
#RUN set FLASK_APP=main.py 
#CMD [ "python3", "-m" , "flask", "run"]
#CMD [ "python3","main.py", "--host=0.0.0.0"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
