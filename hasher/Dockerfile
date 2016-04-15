FROM resin/raspberrypi3-python
RUN pip install Flask
COPY hasher.py /
CMD ["python", "hasher.py"]
EXPOSE 80
