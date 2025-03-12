#!/bin/bash
for i in {1..10}; do
  curl -X GET http://a3aed2698f5214d76a8e508d1b3bf8e4-1291846440.us-east-1.elb.amazonaws.com:8080/
  echo
done
