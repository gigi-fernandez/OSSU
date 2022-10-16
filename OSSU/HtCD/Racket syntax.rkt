;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |Racket syntax|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;libraries: procedure "require [library]"
(require 2htdp/image)

; *** IF YOU EVER RUN INTO TROUBLE UNDERSTANDING FLOW OF
;     EXECUTION, USE THE STEPPER (UPPER RIGHT CORNER) ***

;constants: procedure "define [name] [value]"
;;(define RADIUS 40)

;functions are defined close to constants: procedure "define ([name] [param]) [body]"
;;(define (ring c)
  ;;(circle (+ 1 RADIUS) "outline" c))

;BSL treats images like primitives, and includes some functions like 'above', 'overlay', etc
;;(above
 (circle RADIUS "solid" "white")
 ;;(ring "green")
 ;;(ring "purple"))

;'ifs' and boolean expresions. 'if' procedure: if [bool expression] [true case] [false case]
(if (= (+ 10 2 0) (* 3 4))
    "That is very true my friend"
    "WRONG")

;cond is a way to assess multiple options for a condition (sort of like a switch)
;Syntax:
;(cond [Q A]
;      [Q A]
;      [Q A])