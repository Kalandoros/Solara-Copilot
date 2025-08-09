# Use a lightweight official Python image
FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Copy requirements (if you have additional dependencies, add them to requirements.txt)
COPY requirements.txt ./

# Install dependencies (Solara and any others)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port Solara will serve on
EXPOSE 7860

# Run the Solara app
CMD ["solara", "run", "sol.py", "--host=0.0.0.0", "--production"]
