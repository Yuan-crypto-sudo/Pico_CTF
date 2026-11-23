#!/bin/bash

./run | grep -oE "academy{.*}" --color=none
