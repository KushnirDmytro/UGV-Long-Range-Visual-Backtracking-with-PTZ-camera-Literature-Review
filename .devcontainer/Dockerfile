FROM ubuntu:latest

# Stop apt from asking to get Dialog frontend
ENV DEBIAN_FRONTEND=noninteractive

ENV PROJ_NAME="UGV-Long-Range-Visual-Backtracking-with-PTZ-camera-Literature-Review"
ENV PROJ_DIR_NAME=${PROJ_NAME}

# Install initial packages
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils sudo

# Accept build arguments for UID and GID, with defaults
# Assuming that UID and GID are the same and uequal to 1000
ARG USER_ID=1000
ARG GROUP_ID=1000

# Create a non-root user with specified UID and GID if they don't exist
RUN \
    group_name="latexer" && \
    if getent group "${GROUP_ID:-1000}" ; then \
        group_name="$(getent group "${GROUP_ID:-1000}" | cut -d: -f1)"; \
    else \
        groupadd -g "${GROUP_ID:-1000}" "${group_name}"; \
    fi && \
    user_name="latexer" && \
    if id -u "${USER_ID:-1000}" >/dev/null 2>&1; then \
        user_name="$(id -nu "${USER_ID:-1000}")"; \
    else \
        useradd -m -s /bin/bash -u "${USER_ID:-1000}" -g "${group_name}" "${user_name}"; \
    fi && \
    echo "${user_name} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers


# Set ownership for the workspace directory
RUN mkdir -p /workspaces/${PROJ_DIR_NAME}\
    && chown -R "${USER_ID:-1000}:${GROUP_ID:-1000}" /workspaces/${PROJ_DIR_NAME}

# Switch to non-root user
USER "${user_name}"
WORKDIR /workspaces/${PROJ_DIR_NAME}

# Install necessary packages
RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    git procps openssh-client \
    biber \
    \
    texlive-bibtex-extra \
    \
    make curl\
    chktex latexmk \
    python3-pygments python3-pkg-resources \
    \
    texlive-latex-base \
    texlive-extra-utils \
    texlive-latex-extra \
    texlive-latex-recommended \
    \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    \
    texlive-lang-chinese \
    texlive-lang-japanese \
    texlive-science \
    texlive-humanities \
    && sudo apt-get autoremove -y \
    && sudo apt-get clean -y \
    && sudo rm -rf /var/lib/apt/lists/*

    # texlive-xetex \ # extra compilers that are not needed
    # texlive-luatex

# Install Perl modules
RUN sudo curl -L http://cpanmin.us | sudo perl - App::cpanminus \
    && sudo cpanm Log::Dispatch::File \
    && sudo cpanm YAML::Tiny \
    && sudo cpanm File::HomeDir \
    && sudo cpanm Unicode::GCString

# Restore apt-get dialog
# Set environment variables
ENV DEBIAN_FRONTEND=dialog \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8
