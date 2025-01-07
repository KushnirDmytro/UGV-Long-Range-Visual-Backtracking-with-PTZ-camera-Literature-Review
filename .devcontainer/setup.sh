#!/bin/bash

# Update user and group IDs to match the host system
sudo usermod -u $(id -u) latexer
sudo groupmod -g $(id -g) latexer
sudo chown -R latexer:latexer /workspaces/${PROJ_DIR_NAME}

# Execute any additional setup commands if necessary
exec "$@"

# # Update package lists and install necessary LaTeX packages
# sudo apt-get update
# sudo apt-get install -y \
#     texlive-latex-recommended \
#     texlive-latex-extra \
#     texlive-fonts-recommended \
#     texlive-fonts-extra \
#     texlive-science \
#     texlive-humanities \
#     texlive-bibtex-extra
#     # texlive-xetex \ # we don't need that compilers
#     # texlive-luatex
