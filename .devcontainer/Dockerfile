FROM python:3.9-slim

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl git netcat \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /var/cache/apt/archives/*.deb

# Install task
RUN sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d

# Install devtools
RUN python3.9 -m pip install poetry pre-commit commitizen

# Set git config
RUN git config --global http.proxy ""
