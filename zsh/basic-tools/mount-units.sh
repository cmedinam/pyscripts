#!/bin/zsh

mkdir /tmp/shared0; mount -t 9p -o trans=virtio shared0 /tmp/shared0 \
	                          -o version=9p2000.L,posixacl,cache=mmap
mkdir /tmp/shared1; mount -t 9p -o trans=virtio shared1 /tmp/shared1 \
	                          -o version=9p2000.L,posixacl,cache=mmap
