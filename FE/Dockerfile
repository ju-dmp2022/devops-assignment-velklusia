# Stage: Serve static frontend with Nginx
FROM nginx:alpine

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy static files into the Nginx web root
COPY . .

# Optional: Add dynamic config file used by frontend JavaScript
RUN echo "window.config = { remoteServerAddress: 'http://localhost:5001', webServerAddress: 'http://localhost:8080' };" > /usr/share/nginx/html/config.js

# Optional: Replace default nginx config if needed
COPY nginx.conf.template /etc/nginx/nginx.conf

# Expose the frontend port
EXPOSE 8080

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
