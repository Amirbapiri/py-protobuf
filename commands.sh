#!/usr/bin/env bash
protoc -I=enum/ --python_out=enum enum/enum.proto