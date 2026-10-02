FROM python:3.14.7
WORKDIR /usr/src/app
COPY inventory_manager.py .
CMD ["python", "inventory_manager.py"]