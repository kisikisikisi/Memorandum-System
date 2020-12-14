@ECHO OFF
ECHO Runing starter.lisp
cd "/root/actr6/actr6"
sbcl --dynamic-space-size 10000 --load "/root/actr6/actr6/distr-model/starter.lisp"
PAUSE