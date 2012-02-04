#!/bin/bash

TARGET_DIR='../compiled'

java -jar ~/util/closure/compiler.jar --compilation_level SIMPLE_OPTIMIZATIONS --js src/util-svg.js src/vectors.js src/wikistave-core.js --js_output_file $TARGET_DIR/wikistave.js
