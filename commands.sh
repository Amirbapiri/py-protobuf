#!/usr/bin/env bash
# Enumeration
protoc -I=enum/ --python_out=enum enum/enum.proto

# Complex
protoc -I=complex/ --python_out=complex complex/complex.proto