FROM resin/raspberrypi3-python
RUN pip install Flask
COPY rng.py /
CMD ["python", "rng.py"]
EXPOSE 80
