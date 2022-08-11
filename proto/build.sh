#!/bin/bash

for entry in "./*.proto"
do
    echo $entry
    python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. $entry
done