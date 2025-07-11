#!/bin/bash
set -e

# Activate virtual environment
source /home/trim/Documents/GitHub/GEO-INFER/GEO-INFER-SPACE/repo/osc-geo-h3grid-srv/venv/bin/activate

# Add GEO-INFER-SPACE/src to PYTHONPATH for tests to find shared modules
export PYTHONPATH="/home/trim/Documents/GitHub/GEO-INFER/GEO-INFER-SPACE/src/geo_infer_space/osc_geo/src:$PYTHONPATH"

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Install the current repository in editable mode
echo "Installing current repository in editable mode..."
pip install -e .

# Run tests if test_script is provided
if [ -f "test.sh" ]; then
    echo "Running tests for osc-geo-h3grid-srv..."
    # Use the venv's pytest
    /home/trim/Documents/GitHub/GEO-INFER/GEO-INFER-SPACE/repo/osc-geo-h3grid-srv/venv/bin/pytest tests/
else
    echo "No test script found for osc-geo-h3grid-srv, skipping tests."
fi
