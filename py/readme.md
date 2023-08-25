# Idea - typtap

## description:
* small programm to write notes, with live preview + export to different file formats

## flow 
* read file
* analyse (break down into token, with profiles, etc.)
* change token based on differant commands
* represent in window (live preview)
* and do it again
* export in to file format (.md, .pdf, etc.) when needed

## structur
* util:
  * inclues all the templates for the structure of the project
  * class for profiles
  * tree/ list for the structure
  * classes for the different patterns
* file:
  * handels file reading saving, etc
* analysis:
  * analysis takes file content from "file.go" and divides it into tokens
* graphic:
  * handels all the real-time preview
* pdf:
  * takes the tokens and makes a pdf

## syntax - idea
### basic-text:
* text
```
basic text we need no extra syntax
```
* header
```
$h a very nice header
```
* bulletpoint
```
$p a very nice bulletpoint
```
* code
```
$c some code until it ends $c
```
* bold
```
$b some bold text $b
```
### variables:
* new profile
```
#init smallText
```
* change size
```
#set smallText-size:5p
```
* change color
```
#set smallText-color:#ffffff
```
* use profile
```
#use smallText
```
* change defaults
```
#default pageSizeWidth:30cm
#default pageSizeHeight:20cm
```