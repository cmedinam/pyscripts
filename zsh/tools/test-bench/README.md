# CPU Test and benchmark tools and procedure


----

## Style Notes

* $: Console command
* ~: Run graphical application

----

## Stress Test

### Tools installation

    $ sudo apt install stress
    $ sudo apt install stress-ng
    $ sudo apt install s-tui stress (*)

(*) Not found in Ubuntu 18.04.4 LTS, Bionic

### Tools usage example

    $ stress --cpu 2
    $ stress-ng --cpu 4
    $ stress-ng --cpu 4 --all
    ~ s-tui

For further info, please use command --help argument or man pages.


----

## CPU Benchmark 

### Tools installation

    $ sudo apt install hardinfo
    $ sudo apt install sysbench
    $ sudo apt install p7zip-full

### Tools usage example

    ~ hardinfo
    $ sysbench cpu --threads=2 run
    $ 7z b -mmt1
    $ 7z b

