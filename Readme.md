# teDOT - Visualize your PoV Setup

## Intro
I´m lazy and don´t want to do PoV Setup drawings in PowerPoint. 

## Problem this solves
- Quick creation of Mermaid Code (can be used in a variety of Tools)
- Display Cloud&Enterprise Agent Tests and Alert Rules
- Helps to indentify Configuration inconsitency

## Usage

### Test Diagram creation
To generate Test Diagrams use the "teDOTbyLabels.py" script. (Your API Token is requried as input)
It will create a Mermaid Diagram per Test Label configured. 

```
python3 teDOTbyLabels.py <TOKEN>
```


### Alert Diagram creation
To generate Alert Diagrams use the "teDOTbyAlerts.py" script. (Your API Token is requried as input)
It will create a Mermaid Diagram per Alert Rule. 

```
python3 teDOTbyAlerts.py <TOKEN>
````


