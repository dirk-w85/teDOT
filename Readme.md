# teDOT - Visualize your PoV Setup

## Intro
I´m lazy and didn´t want to do PoV Setup drawings in PowerPoint. 

## Problem this solves
- Quick creation of drawing in Mermaid Code (can be used in a variety of Tool)
- Display major Test and Alert Settings
- Helps to indentify Configuration Inconsitency

## Usage

### Test Diagram creation
To generate Test Diagrams use the "teDOTbyLabels.py" script. (Your API Token is requried as input)
It will create a Mermaid Diagram per Test Label configured. 

```
python3 teDOTbyLabels.py <TOKEN>
```


### Alert Diagram creation
To generate ALert Diagrams use the "teDOTbyAlerts.py" script. (Your API Token is requried as input)

```
python3 teDOTbyAlerts.py <TOKEN>
````


