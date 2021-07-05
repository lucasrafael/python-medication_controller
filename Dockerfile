FROM python:3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

COPY requirements.txt .

# Install system dependency (gettext for Internationalization)
# ---
# $ django-admin makemessages --locale pt_BR
# $ django-admin compilemessages --settings=locale
# ---
RUN apt-get update && apt-get install -y gettext

RUN pip install -r requirements.txt

RUN chmod +x entry_point.sh

# Arguments are in docker-compose.yml
ARG user
ARG group
ARG uid
ARG gid

RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${gid} -s /bin/sh ${user}

RUN chown -Rv ${user}:${group} . 

# Switch to user
USER ${uid}:${gid}

EXPOSE 8000

CMD [ "./entry_point.sh" ]