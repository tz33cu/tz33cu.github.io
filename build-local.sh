#!/bin/bash
# Build Hugo site for local/department server deployment
# Sets permissive file permissions so the web server can read the output

umask 022
hugo --environment local "$@"

# Fix permissions on the published output
chmod -R a+rX /Users/tianzheng/Library/CloudStorage/Dropbox/Tian_Site/tzstats-2025-group/public
