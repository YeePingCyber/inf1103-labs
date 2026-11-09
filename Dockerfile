FROM python:3.14.7
WORKDIR /usr/src/app
COPY Inventory.py .
COPY FileHandling.py .
COPY Product.py .
COPY DigitalProduct.py .
COPY PhysicalProduct.py .
COPY Product.py .
COPY CanBeShipped.py .
COPY Order.py .
COPY OrderLine.py .
COPY main.py .
CMD ["python", "main.py"]