#!/bin/bash

# Function to show help
show_help() {
    echo "Usage: ./start_grid.sh [OPTIONS]"
    echo "Start Selenium Grid and run tests."
    echo ""
    echo "Options:"
    echo "  -h, --help                 Show this help message"
    echo "  -b, --browser BROWSERS     Browsers to run tests on (comma-separated, e.g., 'chrome,firefox')"
    echo "  --headless                 Run browsers in headless mode"
    echo "  -k, --keyword PATTERN      Only run tests matching the given substring expression"
    echo ""
    echo "Example:"
    echo "  ./start_grid.sh -b chrome,firefox --headless"
}

# Default values
BROWSERS="chrome"
HEADLESS=""
KEYWORD=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -b|--browser)
            BROWSERS="$2"
            shift 2
            ;;
        --headless)
            HEADLESS="--headless"
            shift
            ;;
        -k|--keyword)
            KEYWORD="-k $2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Start Selenium Grid
echo "Starting Selenium Grid..."
docker-compose up -d selenium-hub chrome firefox

# Wait for Grid to be ready
echo "Waiting for Selenium Grid to be ready..."
sleep 10

# Set environment variable for Selenium Grid URL
export SELENIUM_GRID_URL="http://localhost:4444/wd/hub"
echo "Using Selenium Grid at: $SELENIUM_GRID_URL"

# Run tests
echo "Running tests with parameters: browsers=$BROWSERS, headless=$HEADLESS, keyword=$KEYWORD"
docker-compose run --rm test-runner ./run_tests.sh -b $BROWSERS $HEADLESS $KEYWORD

# Stop Grid after tests (optional, comment out if you want to keep it running)
echo "Stopping Selenium Grid..."
docker-compose down 