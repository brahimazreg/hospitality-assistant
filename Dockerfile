# 1. Use an official Python image
FROM python:3.11-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy the dependencies file
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the project files
COPY . .

# 6. Expose application ports
EXPOSE 8000 8501