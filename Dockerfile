FROM python
ENV semantix_port=7500

COPY ConstiVorfuehrungDevice.py /var
COPY requirements /var
RUN python -m pip install -r /var/requirements
EXPOSE 9999
CMD python /var/ConstiVorfuehrungDevice.py ${semantix_port}