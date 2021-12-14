FROM python:3.9

# Set the working directory
WORKDIR /news-code

# Copy the file from the local host to the filesystem of the container
COPY requirements.txt ./
 
# Install requirements.txt.
RUN pip3 install -r requirements.txt
 
# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .
 
# Run the crawler when the container launches.
CMD ["python3", "./trigger_gazeta_do_povo.py"]