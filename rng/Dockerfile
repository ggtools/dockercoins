FROM resin/raspberrypi2-python
RUN pip install Flask
COPY rng.py /
CMD ["python", "rng.py"]
EXPOSE 80
