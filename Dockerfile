
# Use official Ubuntu image as base
FROM ubuntu:latest

# Install dependencies and clean up :-
# && \ at the end of a line means the command continues on the next line
# rm -rf /var/lib/apt/lists/*  delete all the files in the directory( /var/lib/apt/lists/ ),which are downloaded by apt-get update,to reduce image size

RUN apt-get update && \
    apt-get install -y cowsay fortune fortune-mod netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Ensure /usr/games is in PATH (to find cowsay and fortune) :-
# On Ubuntu, cowsay and fortune binaries are installed under /usr/games, which is not always in $PATH inside Docker containers.
ENV PATH="/usr/games:${PATH}"

# Set working directory
WORKDIR /app

# Copy wisecow.sh script into the working directory :-
COPY wisecow.sh .

# Convert CRLF to LF and Make the script executable :-
# sed -i 's/\r$//' wisecow.sh ( wisecow.sh script has Windows-style line endings (CRLF) instead of Unix/Linux line endings (LF). this can cause issues when running the script in a Unix/Linux environment. The sed command is used to convert the line endings from CRLF to LF.)
# +x means add execute permission
RUN sed -i 's/\r$//' wisecow.sh && chmod +x wisecow.sh

# Expose the application port :-
EXPOSE 4499

# Start the application :-
CMD ["./wisecow.sh"]



