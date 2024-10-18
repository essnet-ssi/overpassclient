FROM python:3.12.6-bookworm

ENV PATH_CODE=/opt/hbits/overpassclient

COPY docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY python/* /opt/hbits/overpassclient/

### user
RUN useradd -u 1000 overpassclient -g nogroup --create-home

# change user and workdir
USER overpassclient
WORKDIR ${PATH_CODE}

CMD ["bash"]
