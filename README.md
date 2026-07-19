# TrafficFluid-Sim Boundary Controller

Implementation of a boundary controller for lane-free autonomous vehicle traffic using TrafficFluid-Sim.

## Project Overview

This project reproduces and evaluates the boundary controller proposed in the paper:

> "Controlling Automated Vehicles on Large Lane-Free Roundabouts"

The controller computes a desired lateral position based on road boundary distances and applies corrective lateral control to maintain safe vehicle motion.

## Features

- Boundary-aware lateral controller
- Desired lateral position computation
- Lateral error calculation
- Controller logging
- Parameter sensitivity analysis
- Performance evaluation

## Experiments

Four controller configurations were evaluated.

| Safety Margin | Average Error (m) | Maximum Error (m) | Controller Corrections |
|---------------|-------------------|-------------------|------------------------|
| 0.2 m | 0.0003 | 0.218 | 8,516 |
| 0.5 m | 0.0053 | 0.594 | 102,115 |
| 1.0 m | 0.0412 | 1.535 | 341,191 |
| 1.5 m | 0.1375 | 2.736 | 738,078 |

## Average Lateral Error

![Average Error](graphs/avg_error.png)

---

## Maximum Lateral Error

![Maximum Error](graphs/max_error.png)

---

## Controller Corrections

![Corrections](graphs/corrections.png)

---

# Key Findings

- Successfully implemented the boundary-aware lateral controller from the research paper.
- Evaluated controller performance under multiple safety margin configurations.
- Generated quantitative performance metrics and visualization plots.
- Observed that increasing the safety margin results in larger lateral deviations and more frequent controller interventions.

---

# Future Work

- Reproduce additional experiments from the paper.
- Compare the proposed controller with alternative steering strategies.
- Extend the implementation to lane-free roundabout scenarios.
- Investigate controller tuning for improved stability and reduced corrections.

## Repository Structure

```
src/
    LaneFree.cpp

analysis/
    analyze_controller.py

graphs/
    avg_error.png
    max_error.png
    corrections.png

screenshots/
```

## Results

The controller successfully maintains vehicles within lane-free road boundaries while adapting to different safety margins.

Increasing the safety margin increases controller intervention frequency and lateral deviation, demonstrating the expected controller behavior.

## Author

Pankhuri
Research Intern
IIT Mandi

