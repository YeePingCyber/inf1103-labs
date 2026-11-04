FROM python:3.14.7
WORKDIR /usr/src/app
COPY Inventory.py .
COPY FileHandling.py .
COPY Product.py .
COPY CanBeShipped.py .
COPY main.py .
CMD ["python", "main.py"]