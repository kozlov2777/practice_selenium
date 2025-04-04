#!/bin/bash

# Function to show help
show_help() {
    echo "Usage: ./run_tests.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -h, --help                 Show this help message"
    echo "  -b, --browser BROWSERS     Browsers to run tests on (comma-separated, e.g., 'chrome,firefox')"
    echo "  --headless                 Run browsers in headless mode"
    echo "  -v, --verbose              Increase verbosity"
    echo "  -m, --markers MARKERS      Only run tests with the specified markers"
    echo "  -k, --keyword PATTERN      Only run tests matching the given substring expression"
    echo ""
    echo "Environment variables:"
    echo "  SELENIUM_GRID_URL          URL of the Selenium Grid (defaults to http://selenium-hub:4444/wd/hub)"
    echo ""
    echo "Example:"
    echo "  ./run_tests.sh -b chrome,firefox --headless -v"
}

# Default values
BROWSERS="chrome"
HEADLESS=""
VERBOSE=""
MARKERS=""
KEYWORD=""

# Check if SELENIUM_GRID_URL is set, otherwise set a default
if [ -z "$SELENIUM_GRID_URL" ]; then
    export SELENIUM_GRID_URL="http://selenium-hub:4444/wd/hub"
fi

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
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
        -v|--verbose)
            VERBOSE="-v"
            shift
            ;;
        -m|--markers)
            MARKERS="-m $2"
            shift 2
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

# Construct the command
CMD="python -m pytest --browser=$BROWSERS $HEADLESS $VERBOSE $MARKERS $KEYWORD"

# Output information
echo "Running tests with the following settings:"
echo "Browsers: $BROWSERS"
echo "Grid URL: $SELENIUM_GRID_URL"
echo "Command: $CMD"

# Execute the command
eval $CMD
