FROM apache/airflow:2.5.3-python3.10

USER root
# Install OpenJDK-11
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
        procps \
        openjdk-11-jre-headless \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

USER airflow
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

