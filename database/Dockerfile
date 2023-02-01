# Use the official PostgreSQL image as a base
FROM postgres:latest

# Set the environment variables for the PostgreSQL user and password
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 19990521a
# the table name 
ENV POSTGRES_DB nameInfo 

# Expose the PostgreSQL port (default is 5432)
EXPOSE 5432

# Start the PostgreSQL service
CMD ["postgres"]
