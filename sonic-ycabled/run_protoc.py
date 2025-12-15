#!/usr/bin/env python
"""Helper script to run grpc_tools.protoc with proper venv."""
import sys
from grpc_tools import protoc

sys.exit(protoc.main(sys.argv))
