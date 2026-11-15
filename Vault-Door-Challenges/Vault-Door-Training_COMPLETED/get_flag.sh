#!/bin/bash

echo "academy{$(cat VaultDoorTraining.java | grep -oE 'w4[a-zA-Z0-9_]*')}"
