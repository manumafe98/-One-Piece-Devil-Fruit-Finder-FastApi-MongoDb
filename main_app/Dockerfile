FROM python:3.11

# Create the workdir
WORKDIR /code

# Copy the code to the workdir
COPY . /code

# Install the app requirements
RUN pip install -r requirements.txt

# Expose the app port
EXPOSE 8888

# Run the app
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8888"]
