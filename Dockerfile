from python:3.9.2


WORKDIR python-docker 


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY . .
#RUN set FLASK_APP=main.py 
#CMD [ "python3", "-m" , "flask", "run"]
#CMD [ "python3","main.py", "--host=0.0.0.0"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
