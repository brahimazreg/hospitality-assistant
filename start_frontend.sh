#!/bin/sh
set -e

exec streamlit run app/streamlit_app.py \
    --server.address 0.0.0.0 \
    --server.port "${PORT:-10000}"