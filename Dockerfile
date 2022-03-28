FROM python
COPY ConstiVorfuehrungDevice.py /var
COPY requirements /var
RUN python -m pip install -r /var/requirements
EXPOSE 9999
CMD python /var/ConstiVorfuehrungDevice.py