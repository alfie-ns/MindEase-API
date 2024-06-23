#!/bin/bash

# PostgreSQL configuration
DB_NAME="mindease_db"
DB_USER="alfie"
SYSTEM_USER=$(whoami)

# Function to get password securely
get_password() {
    read -s -p "Enter PostgreSQL password for $SYSTEM_USER: " DB_PASSWORD
    echo
}

# Function to setup database
setup_database() {
    echo "Setting up database..."
    get_password

    # Create user
    psql -U $SYSTEM_USER -d postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';" || true
    echo "User $DB_USER created or already exists."

    # Create database
    psql -U $SYSTEM_USER -d postgres -c "CREATE DATABASE $DB_NAME;" || true
    echo "Database $DB_NAME created or already exists."

    # Grant privileges
    psql -U $SYSTEM_USER -d postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
    echo "Privileges granted to $DB_USER on $DB_NAME."

    echo "Database setup completed."
}

# Main menu
while true; do
    echo ""
    echo "PostgreSQL Management Script"
    echo "1. Setup/Verify Database"
    echo "2. Exit"
    read -p "Choose an option: " choice

    case $choice in
        1) setup_database ;;
        2) echo "Exiting..."; exit 0 ;;
        *) echo "Invalid option. Please try again." ;;
    esac
done